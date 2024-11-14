
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.store,name="store"),
    path("load_more_products/",views.load_more_products,name="load_more_products"),
    path("<slug:category_slug>/",views.store,name="products_by_category"),
    path("<slug:category_slug>/<slug:product_slug>/",views.product_page,name="products_by_name"),
    
]
