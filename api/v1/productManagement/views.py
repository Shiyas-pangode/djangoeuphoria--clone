from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from euphoria.models import product
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly



class create_product(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]

class ProductRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]




    