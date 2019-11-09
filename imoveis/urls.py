"""imoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import casa_create, casa_view, casa_edit, casa_delete, apartamento_create, apartamento_view, apartamento_edit, apartamento_delete,

urlpatterns = [
    path('admin/', admin.site.urls),
    #Casa
    path('casa/create', casa_create, name='casa_create'),
    path('casa/view', casa_view, name='casa_view'),
    path('casa/edit/<int:casa_id>', casa_edit, name='casa_edit'),
    path('casa/delete/<int:casa_id>', casa_delete, name='casa_delete'),
    #Apartamento
    path('apartamento/create', apartamento_create, name='apartamento_create'),
    path('apartamento/view', apartamento_view, name='apartamento_view'),
    path('apartamento/edit/<int:apartamento_id>', apartamento_edit, name='apartamento_edit'),
    path('apartamento/delete/<int:apartamento_id>', apartamento_delete, name='apartamento_delete'),
]
