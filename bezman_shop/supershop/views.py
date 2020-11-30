from django.shortcuts import render
from .models import *
# Create your views here.

def product_list(request):
    product = Product.objects.all()
    return render((request,'supershop/products.html'))