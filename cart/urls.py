from django.urls import path
from . import views

urlpatterns = [
   
    path("",views.cart,name="cart"),
    path("add/<int:product_id>/",views.add_cart,name="add_cart"),
    path("reduce_item/<int:product_id>/<int:cart_item_id>/",views.reduce_item, name ="reduce_item"),
    path("remove_item/<int:product_id>/<int:cart_item_id>/",views.remove_item, name ="remove_item"),
   
   
]