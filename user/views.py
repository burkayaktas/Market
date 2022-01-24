from django.shortcuts import render,redirect
from user.models import MyUser
from rest_framework import viewsets
from user.serializers import MyUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class Users(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = []

    tags = ["users"]
    
 
def home(request):
    return render(request,"users/home.html")
    
        
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"             
                