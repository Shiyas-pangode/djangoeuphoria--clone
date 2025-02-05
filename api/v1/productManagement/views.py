from django.shortcuts import render  
from django.http import JsonResponse  

from rest_framework import generics, status  
from rest_framework.response import Response  
from rest_framework.decorators import api_view  
from rest_framework.permissions import IsAuthenticated  

from euphoria.models import Product  
from .serializers import CartSerializer  
from .permissions import IsAdminOrReadOnly  



class create_product(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]

    def list(self ,request , *args ,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)

        return Response({"status": "success",
        "messege" : "Products retrived successfully",
        "data": serializer.data},
        status=status.HTTP_200_OK)

        def create(self , request , *args , **kwargs) :
            self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status" : "messege",
                    "messege" : "product created succesfully",
                    "data" : serializer.data
                }, status=status.HTTP_201_CREATED)

                return Response({"status" : "error",
                "messege" : "product creation failed",
                "errors" : serializer.error},
                status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]




    