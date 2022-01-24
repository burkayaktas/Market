from django.db import models

from user.models import MyUser

class ShoppingCentre(models.Model):
    product = models.CharField(max_length=1024, blank=True)
    price = models.CharField(max_length=1024, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    photo = models.FileField(upload_to="", blank=True) 