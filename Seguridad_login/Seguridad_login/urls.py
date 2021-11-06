"""Seguridad_login URL Configuration

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
from django.contrib import admin
from django.urls import path
from login.views import(
    login,
    cuenta,
	)
from proveedor.views import(
    add_proveedor, list_proveedor, show_proveedor)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name="login"),
    path('cuenta/', cuenta, name="cuenta"),
    path('add_proveedor', add_proveedor, name='add_proveedor'),
    path('list_proveedor', list_proveedor, name='list_proveedor'),
    path('show_proveedor/<IDProveedor>', show_proveedor, name='show_proveedor'),

]
