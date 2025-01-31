from rest_framework import serializers
from euphoria.models import product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


