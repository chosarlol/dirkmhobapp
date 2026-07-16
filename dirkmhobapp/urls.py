import mimetypes
import os
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.http import FileResponse, Http404
from api import views


def serve_frontend(request, path=''):
    """Serve any file from the frontend/ directory; default to home_screen.html."""
    if not path:
        path = 'home_screen.html'
    filepath = os.path.join(settings.BASE_DIR, 'frontend', os.path.normpath(path))
    frontend_root = os.path.join(settings.BASE_DIR, 'frontend')
    if not filepath.startswith(frontend_root):
        raise Http404
    if os.path.isfile(filepath):
        content_type, _ = mimetypes.guess_type(filepath)
        return FileResponse(open(filepath, 'rb'), content_type=content_type or 'application/octet-stream')
    raise Http404


def serve_media(request, path=''):
    """Serve uploaded media files — works regardless of DEBUG setting."""
    filepath = os.path.join(settings.MEDIA_ROOT, os.path.normpath(path))
    media_root = str(settings.MEDIA_ROOT)
    if not filepath.startswith(media_root):
        raise Http404
    if os.path.isfile(filepath):
        content_type, _ = mimetypes.guess_type(filepath)
        return FileResponse(open(filepath, 'rb'), content_type=content_type or 'application/octet-stream')
    raise Http404

urlpatterns = [
    path('admin/', admin.site.urls),

    # ── Auth ──────────────────────────────────────────
    path('api/signup/', views.signup_api,      name='signup'),
    path('api/login/',  views.admin_login_api, name='login'),
    path('api/logout/', views.logout_api,      name='logout'),
    path('api/me/',     views.me_api,          name='me'),

    # ── Super Admin ───────────────────────────────────
    path('api/admin/stats/',                                    views.admin_stats,             name='admin_stats'),
    path('api/admin/users/',                                    views.admin_users,             name='admin_users'),
    path('api/admin/users/<int:user_id>/<str:action>/',         views.admin_user_action,       name='admin_user_action'),
    path('api/admin/restaurants/',                              views.admin_restaurants,       name='admin_restaurants'),
    path('api/admin/restaurants/<int:restaurant_id>/<str:action>/', views.admin_restaurant_action, name='admin_restaurant_action'),
    path('api/admin/orders/',                                   views.admin_orders,            name='admin_orders'),

    # ── Shop Owner ────────────────────────────────────
    path('api/shop/restaurant/logo/',        views.shop_restaurant_logo, name='shop_restaurant_logo'),
    path('api/shop/restaurant/',            views.shop_restaurant,      name='shop_restaurant'),
    path('api/shop/menu/',                          views.shop_menu,            name='shop_menu'),
    path('api/shop/menu/<int:item_id>/image/',    views.shop_menu_item_image, name='shop_menu_item_image'),
    path('api/shop/menu/<int:item_id>/',          views.shop_menu_item,       name='shop_menu_item'),

    # ── Driver ───────────────────────────────────────────
    path('api/driver/signup/',                              views.driver_signup_api,   name='driver_signup'),
    path('api/driver/orders/',                              views.driver_orders,       name='driver_orders'),
    path('api/driver/orders/<int:order_id>/<str:action>/', views.driver_order_action, name='driver_order_action'),
    path('api/driver/earnings/',                            views.driver_earnings,     name='driver_earnings'),

    # ── Orders (submitted by frontend) ────────────────
    path('api/orders/', views.submit_order, name='submit_order'),
    path('api/orders/my-latest/status/', views.my_latest_order_status, name='my_latest_order_status'),
    path('api/orders/<str:order_ref>/status/', views.order_status,   name='order_status'),
    path('api/chat/<str:order_ref>/',          views.chat_messages,  name='chat_messages'),

    # ── Public ────────────────────────────────────────
    path('api/restaurants/',                                  views.restaurants_public,   name='restaurants_public'),
    path('api/restaurants/register/',                         views.shop_register,        name='restaurants_register'),
    path('api/restaurants/pending/',                          views.restaurants_pending,  name='restaurants_pending'),
    path('api/restaurants/<int:restaurant_id>/approve/',      views.restaurant_approve,   name='restaurant_approve'),
    path('api/restaurants/<int:restaurant_id>/menu/add/',     views.restaurant_menu_add,  name='restaurant_menu_add'),
    path('api/restaurants/<int:restaurant_id>/menu/',         views.restaurant_menu,      name='restaurant_menu'),
    path('api/restaurants/<int:restaurant_id>/',              views.restaurant_detail,    name='restaurant_detail'),
    path('api/shop/register/',                                views.shop_register,        name='shop_register'),

    path('media/<path:path>', serve_media),
    # Serve the frontend HTML/PNG/etc. files — must come LAST
    path('', serve_frontend),
    path('<path:path>', serve_frontend),
]
