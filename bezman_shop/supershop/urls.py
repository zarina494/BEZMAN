"""bezman_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/',product_list,name='products'),
    path('orders/',orderlist,name='orders'),
    path ('order-create/<int:product_id>/',orderCreate,name='order-create'),
    path ('order-update/<int:order_id>/',orderUpdate,name='order-update'),
    path('order-delete/<int:order_id>/',orderDelete,name='order-delete'),
    path('order-list/<int:order_id>/',orderDelete,name='order-list'),
]

