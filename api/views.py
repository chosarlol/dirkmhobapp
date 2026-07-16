from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import json
import re
import time

from .models import UserProfile, Restaurant, MenuItem, Order, OrderItem, ChatMessage


# ── Helpers ────────────────────────────────────────────────────────────────────

def _json(data, status=200):
    return JsonResponse(data, status=status)


def _get_role(user):
    """Return the effective role string for a Django User."""
    if user.is_superuser:
        return 'superadmin'
    try:
        return user.profile.role
    except UserProfile.DoesNotExist:
        return 'moderator' if user.is_staff else 'customer'


def _check_auth(request, allowed_roles):
    """
    Return (True, None) when the request passes auth.
    Return (False, error_response) when it fails.
    allowed_roles can be a string or a tuple/list.
    """
    if not request.user.is_authenticated:
        return False, _json({'error': 'Authentication required'}, 401)
    if isinstance(allowed_roles, str):
        allowed_roles = (allowed_roles,)
    role = _get_role(request.user)
    if role not in allowed_roles:
        return False, _json({'error': 'Permission denied'}, 403)
    try:
        if request.user.profile.is_banned:
            return False, _json({'error': 'Account suspended'}, 403)
    except UserProfile.DoesNotExist:
        pass
    return True, None


# ── Auth ───────────────────────────────────────────────────────────────────────

@csrf_exempt
def admin_login_api(request):
    """Universal login — works for customers, shop owners, and admins."""
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return _json({'error': 'Invalid JSON'}, 400)

    identifier = data.get('username', '').strip()
    password   = data.get('password', '').strip()

    # Support email-based login: look up the actual username first
    if '@' in identifier:
        try:
            identifier = User.objects.get(email__iexact=identifier).username
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            pass  # fall through — authenticate will fail and return the right error

    user = authenticate(request, username=identifier, password=password)
    if not user:
        return _json({'error': 'Invalid credentials'}, 400)

    profile, _ = UserProfile.objects.get_or_create(user=user, defaults={'role': 'customer'})
    if profile.is_banned:
        return _json({'error': 'Account suspended'}, 403)

    role = _get_role(user)
    login(request, user)
    return _json({
        'status': 'success',
        'user': {
            'id':       user.id,
            'username': user.username,
            'email':    user.email,
            'name':     user.get_full_name() or user.username,
            'role':     role,
        }
    })


@csrf_exempt
def logout_api(request):
    logout(request)
    return _json({'status': 'ok'})


@csrf_exempt
def signup_api(request):
    """POST /api/signup/ — create a new customer account."""
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return _json({'error': 'Invalid JSON'}, 400)

    name     = data.get('name', '').strip()
    email    = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not name or not email or not password:
        return _json({'error': 'name, email, and password are required'}, 400)
    if len(password) < 6:
        return _json({'error': 'Password must be at least 6 characters'}, 400)
    if User.objects.filter(email__iexact=email).exists():
        return _json({'error': 'An account with this email already exists'}, 400)

    # Derive username from email prefix, ensure uniqueness
    base     = re.sub(r'[^a-z0-9_]', '', email.split('@')[0].lower()) or 'user'
    username = base
    counter  = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1

    name_parts = name.split()
    user = User.objects.create_user(
        username   = username,
        email      = email,
        password   = password,
        first_name = name_parts[0],
        last_name  = ' '.join(name_parts[1:]),
    )
    UserProfile.objects.create(user=user, role='customer')

    return _json({
        'status':   'created',
        'username': username,
        'name':     name,
        'email':    email,
        'role':     'customer',
    }, 201)


def me_api(request):
    """Return the currently logged-in user's info."""
    if not request.user.is_authenticated:
        return _json({'is_authenticated': False, 'authenticated': False})
    role = _get_role(request.user)
    user_obj = {
        'id':       request.user.id,
        'username': request.user.username,
        'email':    request.user.email,
        'name':     request.user.get_full_name() or request.user.username,
        'role':     role,
    }
    return _json({
        # New flat format (used by checkRole in HTML pages)
        'is_authenticated': True,
        'id':       request.user.id,
        'role':     role,
        'username': request.user.username,
        'name':     request.user.get_full_name() or request.user.username,
        'email':    request.user.email,
        # Backward-compat nested format
        'authenticated': True,
        'user': user_obj,
    })


# ── Super Admin — Stats ────────────────────────────────────────────────────────

def admin_stats(request):
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    return _json({
        'total_orders':         Order.objects.count(),
        'total_revenue':        float(Order.objects.aggregate(r=Sum('total'))['r'] or 0),
        'active_restaurants':   Restaurant.objects.filter(status='active').count(),
        'pending_restaurants':  Restaurant.objects.filter(status='pending').count(),
        'total_users':          User.objects.count(),
    })


# ── Super Admin — Users ────────────────────────────────────────────────────────

def admin_users(request):
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    rows = []
    for u in User.objects.all().order_by('-date_joined'):
        try:
            p      = u.profile
            role   = p.role
            banned = p.is_banned
        except UserProfile.DoesNotExist:
            role   = 'customer'
            banned = False
        # Django superusers always display as superadmin regardless of UserProfile
        if u.is_superuser:
            role = 'superadmin'
        rows.append({
            'id':        u.id,
            'username':  u.username,
            'email':     u.email,
            'name':      u.get_full_name() or u.username,
            'role':      role,
            'is_banned': banned,
            'joined':    u.date_joined.strftime('%Y-%m-%d'),
        })
    return _json({'users': rows})


@csrf_exempt
def admin_user_action(request, user_id, action):
    ok, err = _check_auth(request, 'superadmin')
    if not ok:
        return err
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        target = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return _json({'error': 'User not found'}, 404)
    profile, _ = UserProfile.objects.get_or_create(user=target)
    if action == 'ban':
        profile.is_banned = True
        profile.save()
        return _json({'status': 'banned'})
    if action == 'unban':
        profile.is_banned = False
        profile.save()
        return _json({'status': 'unbanned'})
    if action == 'set_driver':
        profile.role = 'driver'
        profile.save()
        return _json({'status': 'set as driver'})
    if action == 'set_customer':
        profile.role = 'customer'
        profile.save()
        return _json({'status': 'set as customer'})
    return _json({'error': 'Unknown action'}, 400)


# ── Super Admin — Restaurants ──────────────────────────────────────────────────

def admin_restaurants(request):
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    rows = []
    for r in Restaurant.objects.select_related('owner').order_by('-created_at'):
        rows.append({
            'id':           r.id,
            'name':         r.name,
            'owner':        r.owner.username,
            'owner_email':  r.owner.email,
            'cuisine_type': r.cuisine_type,
            'status':       r.status,
            'rating':       float(r.rating),
            'menu_count':   r.menu_items.count(),
            'created':      r.created_at.strftime('%Y-%m-%d'),
        })
    return _json({'restaurants': rows})


@csrf_exempt
def admin_restaurant_action(request, restaurant_id, action):
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    try:
        r = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Restaurant not found'}, 404)
    if request.method == 'POST' and action in ('approve', 'suspend'):
        if action == 'approve':
            r.status = 'active'
            r.is_approved = True
        else:
            r.status = 'suspended'
            r.is_approved = False
        r.save()
        return _json({'status': r.status, 'is_approved': r.is_approved})
    if request.method == 'DELETE' and action == 'delete':
        r.delete()
        return _json({'status': 'deleted'})
    return _json({'error': 'Invalid request'}, 400)


# ── Super Admin — Orders ───────────────────────────────────────────────────────

def admin_orders(request):
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    rows = []
    for o in Order.objects.prefetch_related('items').order_by('-created_at')[:200]:
        rows.append({
            'id':             o.id,
            'order_ref':      o.order_ref,
            'customer':       o.customer_name or o.customer_email or '(guest)',
            'restaurant':     o.restaurant_name,
            'total':          float(o.total),
            'discount':       float(o.discount),
            'promo_code':     o.promo_code,
            'payment_method': o.payment_method,
            'status':         o.status,
            'items_count':    o.items.count(),
            'created':        o.created_at.strftime('%Y-%m-%d %H:%M'),
        })
    return _json({'orders': rows})


# ── Shop Owner — Restaurant registration / profile ─────────────────────────────

@csrf_exempt
def shop_restaurant(request):
    ok, err = _check_auth(request, ('shop_owner', 'superadmin'))
    if not ok:
        return err

    if request.method == 'GET':
        try:
            r = Restaurant.objects.get(owner=request.user)
            return _json({'restaurant': {
                'id':             r.id,
                'name':           r.name,
                'description':    r.description,
                'address':        r.address,
                'phone':          r.phone,
                'cuisine_type':   r.cuisine_type,
                'logo_emoji':     r.logo_emoji,
                'logo_image_url': request.build_absolute_uri(r.logo_image.url) if r.logo_image else None,
                'status':         r.status,
                'delivery_fee':   float(r.delivery_fee),
                'min_order':      float(r.min_order),
            }})
        except Restaurant.DoesNotExist:
            return _json({'restaurant': None})

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return _json({'error': 'Invalid JSON'}, 400)
        if Restaurant.objects.filter(owner=request.user).exists():
            return _json({'error': 'Restaurant already registered'}, 400)
        if not data.get('name', '').strip():
            return _json({'error': 'Restaurant name is required'}, 400)
        r = Restaurant.objects.create(
            owner        = request.user,
            name         = data['name'].strip(),
            description  = data.get('description', ''),
            address      = data.get('address', ''),
            phone        = data.get('phone', ''),
            cuisine_type = data.get('cuisine_type', ''),
            logo_emoji   = data.get('logo_emoji', '🍽️'),
            delivery_fee = float(data.get('delivery_fee', 2.50)),
            min_order    = float(data.get('min_order', 0)),
        )
        return _json({'status': 'created', 'id': r.id, 'name': r.name}, 201)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return _json({'error': 'Invalid JSON'}, 400)
        try:
            r = Restaurant.objects.get(owner=request.user)
        except Restaurant.DoesNotExist:
            return _json({'error': 'Restaurant not found'}, 404)
        for field in ('name', 'description', 'address', 'phone', 'cuisine_type', 'logo_emoji'):
            if field in data:
                setattr(r, field, data[field])
        if 'delivery_fee' in data:
            r.delivery_fee = float(data['delivery_fee'])
        if 'min_order' in data:
            r.min_order = float(data['min_order'])
        r.save()
        return _json({'status': 'updated'})

    return _json({'error': 'Method not allowed'}, 405)


# ── Shop Owner — Menu items ─────────────────────────────────────────────────────

@csrf_exempt
def shop_menu(request):
    ok, err = _check_auth(request, ('shop_owner', 'superadmin'))
    if not ok:
        return err
    try:
        restaurant = Restaurant.objects.get(owner=request.user)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Register your restaurant first'}, 400)

    if request.method == 'GET':
        items = []
        for item in restaurant.menu_items.all().order_by('category', 'name'):
            items.append({
                'id':           item.id,
                'name':         item.name,
                'description':  item.description,
                'price':        float(item.price),
                'category':     item.category,
                'emoji':        item.emoji,
                'image_url':    item.image.url if item.image else None,
                'is_available': item.is_available,
            })
        return _json({'items': items, 'restaurant': restaurant.name})

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if not name:
            return _json({'error': 'Item name is required'}, 400)
        try:
            price = float(request.POST.get('price', 0))
        except (ValueError, TypeError):
            return _json({'error': 'Invalid price'}, 400)
        item = MenuItem(
            restaurant  = restaurant,
            name        = name,
            description = request.POST.get('description', ''),
            price       = price,
            category    = request.POST.get('category', ''),
            emoji       = request.POST.get('emoji', '🍽️'),
        )
        if 'image' in request.FILES:
            item.image = request.FILES['image']
        item.save()
        return _json({
            'status':    'created',
            'id':        item.id,
            'image_url': item.image.url if item.image else None,
        }, 201)

    return _json({'error': 'Method not allowed'}, 405)


@csrf_exempt
def shop_menu_item_image(request, item_id):
    """POST /api/shop/menu/<id>/image/ — upload menu item image (multipart)."""
    ok, err = _check_auth(request, ('shop_owner', 'superadmin'))
    if not ok:
        return err
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        item = MenuItem.objects.get(pk=item_id, restaurant__owner=request.user)
    except MenuItem.DoesNotExist:
        return _json({'error': 'Item not found'}, 404)
    if 'image' not in request.FILES:
        return _json({'error': 'No image file provided'}, 400)
    if item.image:
        item.image.delete(save=False)
    item.image = request.FILES['image']
    item.save()
    return _json({'status': 'updated', 'image_url': request.build_absolute_uri(item.image.url)})


@csrf_exempt
def shop_menu_item(request, item_id):
    ok, err = _check_auth(request, ('shop_owner', 'superadmin'))
    if not ok:
        return err
    try:
        item = MenuItem.objects.get(pk=item_id, restaurant__owner=request.user)
    except MenuItem.DoesNotExist:
        return _json({'error': 'Item not found'}, 404)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return _json({'error': 'Invalid JSON'}, 400)
        for field in ('name', 'description', 'category', 'emoji'):
            if field in data:
                setattr(item, field, data[field])
        if 'price' in data:
            item.price = float(data['price'])
        if 'is_available' in data:
            item.is_available = bool(data['is_available'])
        item.save()
        return _json({'status': 'updated'})

    if request.method == 'DELETE':
        item.delete()
        return _json({'status': 'deleted'})

    if request.method == 'PATCH':
        item.is_available = not item.is_available
        item.save()
        return _json({'status': 'toggled', 'is_available': item.is_available})

    return _json({'error': 'Method not allowed'}, 405)


# ── Order submission (called by frontend after placeOrder) ──────────────────────

@csrf_exempt
def submit_order(request):
    """Frontend calls this after placing an order — persists it to the database."""
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return _json({'error': 'Invalid JSON'}, 400)

    items_data = data.get('items', [])
    if not items_data:
        return _json({'error': 'No items in order'}, 400)

    # Use the client-supplied id if it looks like a valid ref (starts with ORD-)
    # so the customer can track the order via localStorage from order_comfirm.html.
    # Fall back to a server-generated ref when the client omits it.
    client_id = (data.get('id') or '').strip()
    if client_id.startswith('ORD-') and not Order.objects.filter(order_ref=client_id).exists():
        order_ref = client_id
    else:
        order_ref = f'ORD-{int(time.time() * 1000)}'

    # Customer — prefer the authenticated session over client-supplied strings
    if request.user.is_authenticated:
        customer_name  = request.user.get_full_name() or request.user.username
        customer_email = request.user.email
    else:
        customer_name  = (data.get('customerName') or data.get('customer_name') or '').strip()
        customer_email = (data.get('customerEmail') or data.get('customer_email') or '').strip()

    # Restaurant name — pull from items or top-level key
    restaurant_name = (
        data.get('restaurantName') or
        data.get('restaurant_name') or
        (items_data[0].get('restaurantName', '') if items_data else '')
    ).strip()

    # Delivery fee — look up from the approved Restaurant record for accuracy
    delivery_fee = float(data.get('deliveryFee') or data.get('delivery_fee') or 2.50)
    if restaurant_name:
        try:
            r = Restaurant.objects.get(name=restaurant_name, is_approved=True)
            delivery_fee = float(r.delivery_fee)
        except (Restaurant.DoesNotExist, Restaurant.MultipleObjectsReturned):
            pass  # keep the client-supplied value

    delivery_address = (data.get('deliveryAddress') or data.get('delivery_address') or '').strip()
    payment_method   = (data.get('paymentMethod')   or data.get('payment_method')   or 'khqr').strip()

    order = Order.objects.create(
        order_ref        = order_ref,
        customer_name    = customer_name,
        customer_email   = customer_email,
        restaurant_name  = restaurant_name,
        subtotal         = float(data.get('subtotal', 0)),
        delivery_fee     = delivery_fee,
        discount         = float(data.get('discount', 0)),
        total            = float(data.get('total', 0)),
        promo_code       = (data.get('promoCode') or data.get('promo_code') or ''),
        payment_method   = payment_method,
        status           = 'confirmed',
        delivery_address = delivery_address,
        # assigned_driver stays NULL — drivers pick this up via driver_orders endpoint
    )
    for it in items_data:
        OrderItem.objects.create(
            order           = order,
            name            = it.get('name', ''),
            price           = float(it.get('price', 0)),
            quantity        = int(it.get('quantity', 1)),
            emoji           = it.get('emoji', '🍽️'),
            restaurant_name = it.get('restaurantName', '') or restaurant_name,
        )
    return _json({'status': 'saved', 'db_id': order.id, 'order_ref': order.order_ref}, 201)


# ── Public: approved restaurant list (for home_screen.html) ────────────────────

def restaurants_public(request):
    """Returns all is_approved=True restaurants — no auth required."""
    rows = []
    for r in Restaurant.objects.filter(is_approved=True).order_by('-created_at'):
        rows.append({
            'id':             r.id,
            'name':           r.name,
            'cuisine_type':   r.cuisine_type,
            'logo_emoji':     r.logo_emoji,
            'logo_image_url': request.build_absolute_uri(r.logo_image.url) if r.logo_image else None,
            'rating':         float(r.rating),
            'delivery_fee':   float(r.delivery_fee),
            'description':    r.description,
            'address':        r.address,
        })
    return _json({'restaurants': rows})


# ── Public: single restaurant + menu ───────────────────────────────────────────

def restaurant_detail(request, restaurant_id):
    """GET /api/restaurants/<id>/ — single approved restaurant."""
    try:
        r = Restaurant.objects.get(pk=restaurant_id, is_approved=True)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Restaurant not found'}, 404)
    return _json({
        'id':             r.id,
        'name':           r.name,
        'description':    r.description,
        'cuisine_type':   r.cuisine_type,
        'logo_emoji':     r.logo_emoji,
        'logo_image_url': request.build_absolute_uri(r.logo_image.url) if r.logo_image else None,
        'rating':         float(r.rating),
        'delivery_fee':   float(r.delivery_fee),
        'min_order':      float(r.min_order),
        'address':        r.address,
        'phone':          r.phone,
    })


def restaurant_menu(request, restaurant_id):
    """GET /api/restaurants/<id>/menu/ — available menu items."""
    try:
        r = Restaurant.objects.get(pk=restaurant_id, is_approved=True)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Restaurant not found'}, 404)
    items = []
    for item in r.menu_items.filter(is_available=True).order_by('category', 'name'):
        items.append({
            'id':          item.id,
            'name':        item.name,
            'description': item.description,
            'price':       float(item.price),
            'category':    item.category,
            'emoji':       item.emoji,
            'image_url':   request.build_absolute_uri(item.image.url) if item.image else None,
        })
    return _json({'items': items, 'restaurant': r.name, 'count': len(items)})


@csrf_exempt
def restaurant_menu_add(request, restaurant_id):
    """POST /api/restaurants/<id>/menu/add/ — shop owner adds a menu item."""
    ok, err = _check_auth(request, ('shop_owner', 'superadmin', 'moderator'))
    if not ok:
        return err
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        r = Restaurant.objects.get(pk=restaurant_id, owner=request.user)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Restaurant not found or not yours'}, 404)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return _json({'error': 'Invalid JSON'}, 400)
    name = data.get('name', '').strip()
    if not name:
        return _json({'error': 'name is required'}, 400)
    item = MenuItem.objects.create(
        restaurant   = r,
        name         = name,
        description  = data.get('description', ''),
        price        = float(data.get('price', 0)),
        category     = data.get('category', ''),
        emoji        = data.get('emoji', '🍽️'),
        is_available = True,
    )
    return _json({'id': item.id, 'name': item.name, 'status': 'created'}, 201)


# ── Public: shop owner self-registration ───────────────────────────────────────

@csrf_exempt
def shop_register(request):
    """
    No auth required.  Creates User + UserProfile(shop_owner) + Restaurant
    in one step and returns the generated credentials.
    """
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return _json({'error': 'Invalid JSON'}, 400)

    name = data.get('name', '').strip()
    if not name:
        return _json({'error': 'Restaurant name is required'}, 400)

    # Generate a unique username from the restaurant name
    base = re.sub(r'[^a-z0-9_]', '', name.lower().replace(' ', '_')) or 'shop'
    username = base
    counter  = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1

    default_password = 'shop1234'
    user = User.objects.create_user(username=username, password=default_password)
    UserProfile.objects.create(user=user, role='shop_owner')

    restaurant = Restaurant.objects.create(
        owner        = user,
        name         = name,
        description  = data.get('description', ''),
        address      = data.get('address', ''),
        phone        = data.get('phone', ''),
        cuisine_type = data.get('cuisine_type', ''),
        logo_emoji   = data.get('logo_emoji', '🍽️'),
        delivery_fee = float(data.get('delivery_fee', 2.50)),
        min_order    = float(data.get('min_order', 0)),
        status       = 'pending',
        is_approved  = False,
    )

    return _json({
        'status':          'created',
        'restaurant_id':   restaurant.id,
        'restaurant_name': restaurant.name,
        'credentials': {
            'username': username,
            'password': default_password,
        },
        'message': 'Restaurant registered! Your account is pending admin approval.',
    }, 201)


# ── Admin: pending restaurants (is_approved=False) ─────────────────────────────

def restaurants_pending(request):
    """Admin only — returns restaurants not yet approved."""
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    rows = []
    for r in Restaurant.objects.filter(is_approved=False).select_related('owner').order_by('-created_at'):
        rows.append({
            'id':           r.id,
            'name':         r.name,
            'owner':        r.owner.username if r.owner else '—',
            'owner_email':  r.owner.email    if r.owner else '—',
            'cuisine_type': r.cuisine_type,
            'logo_emoji':   r.logo_emoji,
            'address':      r.address,
            'created':      r.created_at.strftime('%Y-%m-%d'),
        })
    return _json({'restaurants': rows, 'count': len(rows)})


@csrf_exempt
def shop_restaurant_logo(request):
    """POST /api/shop/restaurant/logo/ — upload restaurant logo image (multipart).
    Must be POST because Django only populates request.FILES for POST requests.
    """
    ok, err = _check_auth(request, ('shop_owner', 'superadmin'))
    if not ok:
        return err
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        r = Restaurant.objects.get(owner=request.user)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Restaurant not found'}, 404)
    if 'logo' not in request.FILES:
        return _json({'error': 'No logo file provided'}, 400)
    if r.logo_image:
        r.logo_image.delete(save=False)
    r.logo_image = request.FILES['logo']
    r.save()
    return _json({'status': 'updated', 'logo_image_url': request.build_absolute_uri(r.logo_image.url)})


@csrf_exempt
def restaurant_approve(request, restaurant_id):
    """PATCH /api/restaurants/<id>/approve/ — approve a pending restaurant."""
    ok, err = _check_auth(request, ('superadmin', 'moderator'))
    if not ok:
        return err
    if request.method != 'PATCH':
        return _json({'error': 'PATCH only'}, 405)
    try:
        r = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        return _json({'error': 'Not found'}, 404)
    r.is_approved = True
    r.status = 'active'
    r.save()
    return _json({'status': 'approved', 'restaurant': r.name, 'is_approved': True})


# ── Driver ─────────────────────────────────────────────────────────────────────

@csrf_exempt
def driver_signup_api(request):
    """POST /api/driver/signup/ — register a new driver account and log them in."""
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return _json({'error': 'Invalid JSON'}, 400)

    name     = data.get('name', '').strip()
    email    = data.get('email', '').strip().lower()
    password = data.get('password', '')
    phone    = data.get('phone', '').strip()

    if not name or not email or not password:
        return _json({'error': 'Name, email, and password are required'}, 400)
    if len(password) < 6:
        return _json({'error': 'Password must be at least 6 characters'}, 400)
    if User.objects.filter(email__iexact=email).exists():
        return _json({'error': 'An account with this email already exists'}, 400)

    base     = re.sub(r'[^a-z0-9_]', '', email.split('@')[0].lower()) or 'driver'
    username = base
    counter  = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1

    name_parts = name.split()
    user = User.objects.create_user(
        username   = username,
        email      = email,
        password   = password,
        first_name = name_parts[0],
        last_name  = ' '.join(name_parts[1:]),
    )
    UserProfile.objects.create(user=user, role='driver', phone=phone)

    login(request, user)
    return _json({
        'status':   'created',
        'username': username,
        'name':     name,
        'email':    email,
        'role':     'driver',
    }, 201)


def driver_orders(request):
    """GET /api/driver/orders/ — new unassigned orders + this driver's active/completed counts."""
    ok, err = _check_auth(request, ('driver', 'superadmin'))
    if not ok:
        return err
    if request.method != 'GET':
        return _json({'error': 'GET only'}, 405)

    from django.utils import timezone

    rejected_ids = request.session.get('driver_rejected_orders', [])
    today = timezone.now().date()

    def _fmt(o):
        return {
            'id':                o.id,
            'order_ref':         o.order_ref,
            'restaurant_name':   o.restaurant_name,
            'customer_name':     o.customer_name or 'Customer',
            'delivery_address':  o.delivery_address or '—',
            'delivery_fee':      float(o.delivery_fee),
            'payment_method':    o.payment_method,
            'status':            o.status,
            'distance_km':       round(((o.id % 7) + 1), 1),
            'estimated_minutes': (o.id % 12) + 8,
            'created_at':        o.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
        }

    # Only today's confirmed orders with no driver assigned
    new_orders = Order.objects.filter(
        status='confirmed',
        assigned_driver__isnull=True,
        created_at__date=today,
    ).exclude(id__in=rejected_ids).order_by('-created_at')[:30]

    # Orders this driver has accepted (preparing = picking up, on_the_way/delivering = en route)
    active_orders = Order.objects.filter(
        assigned_driver=request.user,
        status__in=['preparing', 'on_the_way', 'delivering'],
    ).order_by('-created_at')

    completed_count = Order.objects.filter(
        assigned_driver=request.user,
        status='delivered',
    ).count()

    return _json({
        'new_orders':      [_fmt(o) for o in new_orders],
        'active_orders':   [_fmt(o) for o in active_orders],
        'completed_count': completed_count,
    })


@csrf_exempt
def driver_order_action(request, order_id, action):
    """POST /api/driver/orders/<id>/accept|reject|complete/"""
    ok, err = _check_auth(request, ('driver', 'superadmin'))
    if not ok:
        return err
    if request.method != 'POST':
        return _json({'error': 'POST only'}, 405)
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return _json({'error': 'Order not found'}, 404)

    if action == 'accept':
        if order.assigned_driver is not None:
            return _json({'error': 'Order already taken'}, 409)
        order.assigned_driver = request.user
        order.status = 'preparing'
        order.save()
        return _json({
            'status':    'accepted',
            'order_ref': order.order_ref,
            'order': {
                'id':                order.id,
                'order_ref':         order.order_ref,
                'restaurant_name':   order.restaurant_name,
                'customer_name':     order.customer_name or 'Customer',
                'delivery_address':  order.delivery_address or '—',
                'delivery_fee':      float(order.delivery_fee),
                'payment_method':    order.payment_method,
                'status':            'preparing',
                'distance_km':       round(((order.id % 7) + 1), 1),
                'estimated_minutes': (order.id % 12) + 8,
                'created_at':        order.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            },
        })

    if action == 'pickup':
        if order.assigned_driver != request.user and not request.user.is_superuser:
            return _json({'error': 'Not your order'}, 403)
        order.status = 'on_the_way'
        order.save()
        return _json({'status': 'picked_up'})

    if action == 'reject':
        rejected = request.session.get('driver_rejected_orders', [])
        if order_id not in rejected:
            rejected.append(order_id)
            request.session['driver_rejected_orders'] = rejected
            request.session.modified = True
        return _json({'status': 'rejected'})

    if action in ('complete', 'delivered'):
        if order.assigned_driver != request.user and not request.user.is_superuser:
            return _json({'error': 'Not your order'}, 403)
        order.status = 'delivered'
        order.save()
        return _json({'status': 'completed', 'delivery_fee': float(order.delivery_fee)})

    return _json({'error': 'Unknown action'}, 400)


def driver_earnings(request):
    """GET /api/driver/earnings/ — earnings breakdown for this driver."""
    ok, err = _check_auth(request, ('driver', 'superadmin'))
    if not ok:
        return err
    if request.method != 'GET':
        return _json({'error': 'GET only'}, 405)

    from django.utils import timezone
    from datetime import timedelta

    now         = timezone.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start  = today_start - timedelta(days=now.weekday())
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    delivered = Order.objects.filter(assigned_driver=request.user, status='delivered')

    def _earn(qs):
        return float(qs.aggregate(s=Sum('delivery_fee'))['s'] or 0)

    today_qs = delivered.filter(created_at__gte=today_start)
    week_qs  = delivered.filter(created_at__gte=week_start)
    month_qs = delivered.filter(created_at__gte=month_start)

    recent = []
    for o in delivered.order_by('-created_at')[:50]:
        recent.append({
            'order_ref':        o.order_ref,
            'restaurant_name':  o.restaurant_name,
            'customer_name':    o.customer_name or 'Customer',
            'delivery_address': o.delivery_address or '—',
            'delivery_fee':     float(o.delivery_fee),
            'payment_method':   o.payment_method or '—',
            'completed_at':     o.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
        })

    return _json({
        'today':  {'earnings': _earn(today_qs),  'count': today_qs.count()},
        'week':   {'earnings': _earn(week_qs),   'count': week_qs.count()},
        'month':  {'earnings': _earn(month_qs),  'count': month_qs.count()},
        'recent': recent,
    })


# ── Customer: live order status (polled by order_comfirm.html) ─────────────────

def _order_status_json(order):
    """Shared helper — build the status payload for any Order instance."""
    driver_name = ''
    if order.assigned_driver:
        driver_name = order.assigned_driver.get_full_name() or order.assigned_driver.username
    status_map = {
        'confirmed':  'confirmed',
        'preparing':  'preparing',
        'on_the_way': 'on_the_way',
        'delivering': 'on_the_way',
        'delivered':  'delivered',
        'cancelled':  'cancelled',
    }
    return _json({
        'status':           status_map.get(order.status, order.status),
        'driver_name':      driver_name,
        'restaurant_name':  order.restaurant_name,
        'delivery_address': order.delivery_address or '',
        'order_ref':        order.order_ref,
    })


def order_status(request, order_ref):
    """GET /api/orders/<order_ref>/status/ — returns current status for polling."""
    try:
        order = Order.objects.get(order_ref=order_ref)
    except Order.DoesNotExist:
        return _json({'error': 'Order not found'}, 404)
    return _order_status_json(order)


def my_latest_order_status(request):
    """GET /api/orders/my-latest/status/ — returns the most recent order for
    the logged-in user. Used as a fallback when order_ref is missing or stale."""
    order = None
    if request.user.is_authenticated:
        order = (
            Order.objects
            .filter(customer_email=request.user.email)
            .order_by('-created_at')
            .first()
        )
    if order is None:
        # Also try by session-stored name/email supplied by the client
        order = Order.objects.order_by('-created_at').first()
    if order is None:
        return _json({'error': 'No orders found'}, 404)
    return _order_status_json(order)


# ── Chat ────────────────────────────────────────────────────────────────────────

@csrf_exempt
def chat_messages(request, order_ref):
    """GET /api/chat/<order_ref>/?since_id=N  — poll new messages
       POST /api/chat/<order_ref>/             — send a message"""
    if not request.user.is_authenticated:
        return _json({'error': 'Authentication required'}, 401)

    try:
        order = Order.objects.get(order_ref=order_ref)
    except Order.DoesNotExist:
        return _json({'error': 'Order not found'}, 404)

    driver_name = ''
    if order.assigned_driver:
        driver_name = order.assigned_driver.get_full_name() or order.assigned_driver.username

    def _fmt(m):
        is_driver = order.assigned_driver and m.sender_id == order.assigned_driver_id
        return {
            'id':          m.id,
            'sender_id':   m.sender_id,
            'sender_name': m.sender.get_full_name() or m.sender.username,
            'is_driver':   is_driver,
            'body':        m.body,
            'created_at':  m.created_at.strftime('%H:%M'),
        }

    if request.method == 'GET':
        since_id = int(request.GET.get('since_id', 0))
        qs = order.messages.select_related('sender')
        if since_id:
            qs = qs.filter(id__gt=since_id)
        return _json({
            'messages':      [_fmt(m) for m in qs],
            'driver_name':   driver_name,
            'customer_name': order.customer_name or '',
            'order_ref':     order.order_ref,
            'restaurant':    order.restaurant_name,
            'status':        order.status,
            'delivery_addr': order.delivery_address or '',
        })

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return _json({'error': 'Invalid JSON'}, 400)
        body = (data.get('body') or '').strip()
        if not body:
            return _json({'error': 'Empty message'}, 400)
        msg = ChatMessage.objects.create(order=order, sender=request.user, body=body)
        return _json(_fmt(msg), 201)

    return _json({'error': 'GET or POST only'}, 405)
