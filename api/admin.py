from django.contrib import admin
from .models import Category, Dish  # Real model names imported here

admin.site.register(Category)
admin.site.register(Dish)
