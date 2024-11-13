from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products

def home(request):
    products = Products.objects.all().filter(is_available = True)
    context = {"products":products}
    return render(request,'index.html',context)