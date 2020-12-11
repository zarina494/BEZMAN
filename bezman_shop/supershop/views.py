import string

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter
from .decorators import allowed_roles



# Create your views here.

def product_list(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    context = {'products':products,'filter':filter}
    return render(request,'supershop/products.html',context)

@allowed_roles(allowed=['bezman'])
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
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('page Status=404')
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context= {'form':form}
    return render(request,'supershop/order-create.html', context)

def task1(request):
    string = 'wjmzbmr'
    a = set(string)
    if len(a)%2 ==0:
        return HttpResponse('CHAT WITH HER')
    else:
        return HttpResponse('IGNORE')

def task2(request):
    import random
    n,h= 3,7
    list1 = []
    list2 =[4,5,14]
    # for i in range(n):
    #     list1.append(random.randint(1,2*h))
    for hei in list2:
        if hei > h:
            list1.append(2)
        elif hei <= h:
            list1.append(1)
    return HttpResponse(sum(list1))

def orderDelete(request,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('page Status=404')
    #form = OrderForm(instance=order)
    if request.method == 'POST':
        if order.status == 'Not Delivered':
            order.delete()
            return HttpResponse('Order Delete!')
        else:
            return HttpResponse('Not Delivered!')

    context = {'order':order}
    return render(request,'supershop/order-delete.html',context)


