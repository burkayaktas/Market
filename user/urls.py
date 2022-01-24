from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()
router.register('', views.Users)

urlpatterns = [
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),

]

