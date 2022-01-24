from rest_framework import serializers

from centre.models import ShoppingCentre


class ShoppingCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCentre
        fields = "__all__"