from django.shortcuts import render  
from django.contrib.auth.models import User  
from rest_framework import generics, status  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework.permissions import AllowAny  
from rest_framework_simplejwt.tokens import RefreshToken  

from .serializers import userRegistrationSerializer  
from euphoria.models import Product  



class userRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userRegistrationSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            # token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

