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
from django.urls import path, include
from .views import *
from django.contrib.auth.views import *


urlpatterns = [
    path('reset-password/',PasswordResetView.as_view(),name='reset-password'),
    path('reset-password-done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset-password-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('customers/',customerList,name='customer'),
    path('customers/<int:customer_id>/',get_customer,name='customers'),
    path('registration/',registration,name='registration'),
    path('login/',auth,name='login'),
    path('logout/',logout_page,name='logout'),
    path('customer_list/<int:customer_id>/',get_customer,name='customer_list'),
]