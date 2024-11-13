from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from  .models import Products
from category.models import Category


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
        context = {"products":products,
        "count":count}

    return render(request,'store/store.html',context)

def product_page(request, category_slug, product_slug):
    try:
        single_product_detail = Products.objects.get(category__slug = category_slug,slug = product_slug)
    except Exception as e:
        raise e
    context = {"single_product_detail":single_product_detail}
    return render(request,'store/single_product.html',context)