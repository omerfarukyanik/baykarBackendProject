"""
URL configuration for baykarBackendProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from baykarApp import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='landing_page'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('home/', views.home_page, name='home_page'),
    path('profile/', views.home_page, name='profile'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('list/', views.list_products, name='list'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/purchase/', views.purchase_cart, name='purchase_cart'),
    path('rentallogs/', views.get_rental_logs, name='rental_logs'),
    path('rentallogs/delete/<int:log_id>', views.delete_rental_log, name='delete_rental_log'),
    path('rentallogs/edit/<int:log_id>', views.edit_rental_log, name='edit_rental_log'),
]
