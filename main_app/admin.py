from django.contrib import admin
from .models import DishCategory, Dish, About

# Register your models here.
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(About)