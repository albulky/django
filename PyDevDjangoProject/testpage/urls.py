"""PyDevDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from . import views, contactform

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:n>/<str:s>/', views.index, name='index_with_params'),
    path('html/', views.show_html, name='html_page'),
    path('html/<str:title>/<str:msg>/', views.show_html, name='html_page'),
    path('contact/', contactform.contact, name='contact'),
    path('<path:p>/', views.index, name='index_with_path'),
]
