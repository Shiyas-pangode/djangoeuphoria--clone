from rest_framework import serializers
from euphoria.models import Cart


class CartViewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cart
        fields = ' __all__'

