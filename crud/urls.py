"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from employee.views.register import Regis
from employee.views.showdata import Show
from employee.views.delete import delete
from employee.views.update import Edit ,update
from employee.views.login import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Regis.as_view(),name="Register"),
    path('show/',Show.as_view(),name="showdata"),
    path('delete/<int:id>',delete,name="Delete"),
    path('edit/<int:id>',Edit,name="Edit"),
    path('update/<int:id>',update,name="update"),
    path('login/',Login.as_view(),name="Login")
]
