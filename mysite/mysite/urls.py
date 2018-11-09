"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include,path,re_path
#from django.conf.urls.defaults import *
from Myapp.views import *
urlpatterns = [
    #path('hello/<name>',say_hello),
    re_path(r'hello/(\w+)',say_hello), # for reg ex as path that takes any param after hello/
    path('date/',date_time),
    re_path(r'addtime/(.*)',addhours),
    path('template/<content>',getTemplate),
    path("viewsearch/",getForm),
    re_path(r"search/",searchtext),
    path("update/",update),
    path("myform/",getMyform),
    path("getcookie/",getcookie),
    path("setcookie/",setcookie),
    path("login/",login),
    path('login_validate/',validate_login),
    path('logout/',logout),
    path('admin/', admin.site.urls),
]

