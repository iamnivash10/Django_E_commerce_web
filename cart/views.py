from django.shortcuts import render,redirect 
from products.models import Products
from .models import Cart, CartItem
from django.http import HttpResponse

# Create your views here.
def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()

    
    return redirect('cart')
   
def reduce_item(request,product_id):
    product = Products.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id = _cart_id(request))
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 0:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart')
def remove_item(request,product_id):
    product = Products.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id = _cart_id(request))    
    cart_item = CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')
def cart(request,total = 0 ,quantity = 0 ,cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = 2 * total/100
        
        grand_total = total + tax
    except Exception as e:
        pass
    context = {"total":total,"quantity":quantity,"cart_items":cart_items, "tax": tax , "grand_total":grand_total}
    return render(request, 'store/cart.html', context)