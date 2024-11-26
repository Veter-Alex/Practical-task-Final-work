from django.contrib import admin

from .models import Category, Good, Seller

# Register your models here.


admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Seller)
