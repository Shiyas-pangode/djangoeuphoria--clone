from rest_framework import generics, status  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework.permissions import IsAuthenticated  
from rest_framework.exceptions import NotFound  

from django.shortcuts import get_object_or_404  

from euphoria.models import Cart, product  
from .serializers import CartViewSerializer  



class Cart_View(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        # Fetch the cart items for the authenticated user
        cart_items = Cart.objects.filter(user=request.user)
        serializers = CartViewSerializer(cart_items, many=True)
        return Response(serializers.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        
        # Ensure the product exists
        try:
            Product = product.objects.get(id=product_id)
        except product.DoesNotExist:
            raise NotFound("Product not found.")

        # Add product to the user's cart, or increment the quantity if already present
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=Product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return Response({"message": "Product added to cart"}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        product_id = request.data.get('product_id')
        
        # Ensure the product is in the user's cart before deleting
        cart_item = Cart.objects.filter(user=request.user, product_id=product_id)
        if not cart_item.exists():
            return Response({"detail": "Product not in cart"}, status=status.HTTP_404_NOT_FOUND)
        
        # Remove the product from the user's cart
        cart_item.delete()
        return Response({"message": "Product removed from cart"}, status=status.HTTP_204_NO_CONTENT)
