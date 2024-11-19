from django.shortcuts import render,redirect 
from products.models import Products,variant
from .models import Cart, CartItem 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    variant_list = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            
            try :
                variation = variant.objects.get(product=product,variant_categery__iexact=key,variant_value__iexact=value,is_active=True)
                variant_list.append(variation)
            except variant.DoesNotExist:
                pass
    

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    
    is_object_in_cart_exist = CartItem.objects.filter(product=product,cart=cart).exists()

    if is_object_in_cart_exist:
        cart_items =  CartItem.objects.filter(product=product,cart=cart)
        exist_variation=[]
        id_all = []
        for item in cart_items:
            variations = item.variation.all()
            exist_variation.append(list(variations))
            id_all.append(item.id)

        
        if variant_list in exist_variation:
            index = exist_variation.index(variant_list)
            id = id_all[index]
            item = CartItem.objects.get(product=product,cart=cart,id = id)
            item.quantity+=1
            item.save()
        else:
            item = CartItem.objects.create(product=product,cart=cart,quantity=1)
            if len(variant_list)>0:
                item.variation.add(*variant_list)
            item.save

    else:
        item = CartItem.objects.create(product=product,cart=cart,quantity=1)
        if len(variant_list)>0:
            item.variation.add(*variant_list)
        item.save()
        
    
    return redirect('cart')
   
def reduce_item(request,product_id,cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Products,id = product_id)
    try:
        cart_item = CartItem.objects.get(product=product,cart=cart,id =cart_item_id)
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
        cart_item.save()
    except:
        pass
    return redirect('cart')
def remove_item(request,product_id,cart_item_id):
    product = get_object_or_404(Products,id = product_id)
    cart = Cart.objects.get(cart_id = _cart_id(request))  
    try:  
         cart_item = CartItem.objects.get(product=product,cart=cart,id = cart_item_id)
         cart_item.delete()
    except:
        pass
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