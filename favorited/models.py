from django.db import models

# Create your models here.
from centre.models import ShoppingCentre
from user.models import MyUser


class Favorite(models.Model):
    favorited = models.ForeignKey(ShoppingCentre, on_delete=models.CASCADE, related_name="favorited")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['favorited']]
