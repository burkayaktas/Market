from rest_framework import serializers

from favorited.models import Favorite
from user.models import MyUser


class FavoriteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

