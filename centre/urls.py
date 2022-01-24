from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.shopping_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.shopping_detail, name="detail"),
]
