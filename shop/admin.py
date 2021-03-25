from django.contrib import admin
from .models import Dish, Beverage


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dish_type', 'description']

@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'beverages_type', 'description']
