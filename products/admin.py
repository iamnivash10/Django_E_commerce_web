from django.contrib import admin
from .models import Products,variant

# Register your models here.

class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ("product_name","price","stock","is_available","category")
    

class variantadmin(admin.ModelAdmin):
    list_display = ("product","variant_categery","variant_value","is_active")
    list_editable = ("is_active",)
    list_filter = ("product","variant_categery","variant_value")

admin.site.register(Products,productAdmin)
admin.site.register(variant,variantadmin)