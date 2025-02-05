from rest_framework import serializers
from euphoria.models import Cart

class CartViewSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', read_only=True,
                                             max_digits=10, decimal_places=2)  # Fixed typo
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity', 'product_name', 'product_price', 'user_username']  # Added 'user_username'
        read_only_fields = ['product_name', 'product_price', 'user_username']


