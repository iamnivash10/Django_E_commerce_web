from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from  .models import Products
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import Paginator
from zetraweb import settings

def store(request,category_slug = None):
    product = None
    categery = None
    if category_slug != None:
        categery_name = get_object_or_404(Category,slug = category_slug)
        products = Products.objects.filter(category=categery_name,is_available = True)
        count = products.count()
        context = {"products":products,
                   "count":count}
    else:

        products = Products.objects.all().filter(is_available = True)
        count = products.count()
        aginator = Paginator(products,settings.PAGE_SIZE)
        product_page = aginator.page(1)
        context = {"products":product_page ,
        "count":count}

    return render(request,'store/store.html',context)

def product_page(request, category_slug, product_slug):
    try:
        single_product_detail = Products.objects.get(category__slug = category_slug,slug = product_slug)
        is_cart = CartItem.objects.filter(product = single_product_detail,cart__cart_id = _cart_id(request))
    except Exception as e:
        raise e
    context = {"single_product_detail":single_product_detail,"is_cart":is_cart}
    return render(request,'store/single_product.html',context)

def load_more_products(request):
    page = request.GET.get('page',1)
    products = Products.objects.all().filter(is_available = True)
    count = products.count()
    paginator = Paginator(products,settings.PAGE_SIZE)
    context = {"products":paginator.page(page) ,
        "count":count}

    return render(request,'store/store.html#product_list',context)