from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('customer',   'Customer'),
        ('shop_owner', 'Shop Owner'),
        ('moderator',  'Moderator'),
        ('superadmin', 'Super Admin'),
    ]
    user      = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role      = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone     = models.CharField(max_length=20, blank=True)
    avatar    = models.CharField(max_length=10, default='👤')
    is_banned = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} ({self.role})'


class Restaurant(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending Approval'),
        ('active',    'Active'),
        ('suspended', 'Suspended'),
    ]
    owner         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    name          = models.CharField(max_length=200)
    description   = models.TextField(blank=True)
    address       = models.CharField(max_length=300, blank=True)
    phone         = models.CharField(max_length=20, blank=True)
    cuisine_type  = models.CharField(max_length=100, blank=True)
    logo_emoji    = models.CharField(max_length=10, default='🍽️')
    logo_image    = models.FileField(upload_to='restaurant_logos/', blank=True, null=True)
    rating        = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_approved   = models.BooleanField(default=False)
    delivery_fee  = models.DecimalField(max_digits=5, decimal_places=2, default=2.50)
    min_order     = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.status})'


class MenuItem(models.Model):
    restaurant   = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name         = models.CharField(max_length=200)
    description  = models.TextField(blank=True)
    price        = models.DecimalField(max_digits=6, decimal_places=2)
    category     = models.CharField(max_length=100, blank=True)
    emoji        = models.CharField(max_length=10, default='🍽️')
    image        = models.FileField(upload_to='menu_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} — {self.restaurant.name}'


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',    'Pending'),
        ('confirmed',  'Confirmed'),
        ('preparing',  'Preparing'),
        ('delivering', 'Delivering'),
        ('delivered',  'Delivered'),
        ('cancelled',  'Cancelled'),
    ]
    order_ref        = models.CharField(max_length=60, unique=True)
    customer_name    = models.CharField(max_length=200, blank=True)
    customer_email   = models.EmailField(blank=True)
    restaurant_name  = models.CharField(max_length=200, blank=True)
    subtotal         = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    delivery_fee     = models.DecimalField(max_digits=5, decimal_places=2, default=2.50)
    discount         = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total            = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    promo_code       = models.CharField(max_length=50, blank=True)
    payment_method   = models.CharField(max_length=50, default='khqr')
    status           = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    delivery_address = models.CharField(max_length=300, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order_ref} — ${self.total}'


class OrderItem(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name            = models.CharField(max_length=200)
    price           = models.DecimalField(max_digits=6, decimal_places=2)
    quantity        = models.IntegerField(default=1)
    emoji           = models.CharField(max_length=10, default='🍽️')
    restaurant_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.quantity}x {self.name}'


# ── Kept from original schema ─────────────────────────────────

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    image_name  = models.CharField(max_length=100, help_text='e.g., asian_dishes.jpg')

    def __str__(self):
        return self.name
