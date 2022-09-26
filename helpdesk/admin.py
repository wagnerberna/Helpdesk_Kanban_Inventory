from unicodedata import category

from django.contrib import admin

from .models import Category, Demand, Status, Support

# Register your models here.
admin.site.register(Category)
admin.site.register(Demand)
admin.site.register(Support)
admin.site.register(Status)
