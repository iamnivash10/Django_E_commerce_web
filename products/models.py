from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Products (models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='photos/products/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name

    def get_urls(self):
        return reverse("products_by_name",args=[self.category.slug,self.slug])
