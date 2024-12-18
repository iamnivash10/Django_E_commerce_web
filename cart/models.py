from django.db import models
from products.models import Products,variant

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variation = models.ManyToManyField(variant,blank= True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product
    def get_sub_price(self):
        return self.product.price * self.quantity

    
    
