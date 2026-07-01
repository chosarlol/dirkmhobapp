from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views

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

    # ── Orders (submitted by frontend) ────────────────
    path('api/orders/', views.submit_order, name='submit_order'),

    # ── Public ────────────────────────────────────────
    path('api/restaurants/',                                  views.restaurants_public,   name='restaurants_public'),
    path('api/restaurants/register/',                         views.shop_register,        name='restaurants_register'),
    path('api/restaurants/pending/',                          views.restaurants_pending,  name='restaurants_pending'),
    path('api/restaurants/<int:restaurant_id>/approve/',      views.restaurant_approve,   name='restaurant_approve'),
    path('api/restaurants/<int:restaurant_id>/menu/add/',     views.restaurant_menu_add,  name='restaurant_menu_add'),
    path('api/restaurants/<int:restaurant_id>/menu/',         views.restaurant_menu,      name='restaurant_menu'),
    path('api/restaurants/<int:restaurant_id>/',              views.restaurant_detail,    name='restaurant_detail'),
    path('api/shop/register/',                                views.shop_register,        name='shop_register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
