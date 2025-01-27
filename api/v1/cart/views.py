from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from euphoria.models import product
from .serializers import CartSerializer

@api_view(['POST'])

def create_product(request):
    if request.method == "POST":
        # Add logic to create a product
        return JsonResponse({"message": "Product created successfully"})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
# @api_view(['GET' , 'POST' ,'DELETE'])

# def create_product(request):
#     if request.method == 'GET':
#         posts = CreatePost.objects.all()
#         serializers = CartSerializer(posts, many=True, context= {'request': request})
#         data = serializers.data 
#         for product in data:
#             product['image'] = request.build_absolute_uri(post['image'])
#             return Response(serializers.data,status=status.HTTP_200_OK)