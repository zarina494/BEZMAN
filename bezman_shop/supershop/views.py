from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    context = {'products':products,'filter':filter}
    return render(request,'supershop/products.html',context)

def orderlist(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count
    orders_in_process = Order.objects.filter(status='In Process').count
    orders_not_delivered = Order.objects.filter(status='Not Delivered').count
    context = {'orders':orders,'orders_count':orders_count,'orders_delivered':orders_delivered,
               'orders_in_process':orders_in_process,'orders_not_delivered':orders_not_delivered}
    return render(request, 'supershop/order-list.html', context)

def orderCreate(request, product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user
    form = OrderForm(initial={'product':product,'customer':customer})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'form':form}
    return render(request,'supershop/order-create.html',context)


def orderUpdate(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context= {'form':form}
    return render(request,'supershop/order-create.html', context)



