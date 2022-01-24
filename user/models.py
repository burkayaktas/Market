from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)