from django.contrib import admin
from .models import Cart,CartItem

# Register your models here.
class Cartadmin(admin.ModelAdmin):
    list_display =("cart_id","date_added")

class CartItemadmin(admin.ModelAdmin):
    list_display =("product","cart","quantity")

admin.site.register(Cart,Cartadmin)
admin.site.register(CartItem,CartItemadmin)
