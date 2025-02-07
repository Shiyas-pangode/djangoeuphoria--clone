from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 



class userRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)


    class Meta :
        model = User
        fields = ['username' , 'password']

        def create (self, validated_data):
            user = User.objects.create_user( 
                username = validated_data["username"],
                password =  validated_data["password"]
            ) 
            user.is_active = True  
            user.save()

            return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token