"""kgWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('charts', views.index),
    # path('result/?input-str=sadfasfd', views.result)
    # url(r'^result/?', views.result),
    # url(r'^/?', views.index),
    # url(r'nodes', views.nodes),
    # url(r'ajax_info', views.ajax_info),
    path('', views.index),
    path('ajax_info', views.ajax_info),
    path("status_info", views.status_info),
]
