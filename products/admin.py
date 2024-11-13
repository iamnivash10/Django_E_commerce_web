from django.contrib import admin
from .models import Products

# Register your models here.

class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ("product_name","price","stock","is_available","category")
admin.site.register(Products,productAdmin)