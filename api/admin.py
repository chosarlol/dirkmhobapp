from django.contrib import admin
from .models import UserProfile, Restaurant, MenuItem, Order, OrderItem, Category, Dish


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'role', 'is_banned', 'joined_at')
    list_filter   = ('role', 'is_banned')
    search_fields = ('user__username', 'user__email')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display  = ('name', 'owner', 'cuisine_type', 'status', 'rating', 'created_at')
    list_filter   = ('status',)
    search_fields = ('name', 'owner__username')
    actions       = ['approve_restaurants', 'suspend_restaurants']

    @admin.action(description='Approve selected restaurants')
    def approve_restaurants(self, request, queryset):
        queryset.update(status='active')

    @admin.action(description='Suspend selected restaurants')
    def suspend_restaurants(self, request, queryset):
        queryset.update(status='suspended')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display   = ('name', 'restaurant', 'price', 'category', 'is_available')
    list_filter    = ('is_available', 'category')
    list_editable  = ('is_available',)
    search_fields  = ('name', 'restaurant__name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ('order_ref', 'customer_name', 'restaurant_name', 'total', 'status', 'created_at')
    list_filter   = ('status', 'payment_method')
    search_fields = ('order_ref', 'customer_name', 'customer_email')
    readonly_fields = ('created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'quantity', 'price', 'restaurant_name')


admin.site.register(Category)
admin.site.register(Dish)
