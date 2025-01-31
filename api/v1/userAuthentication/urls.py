from django.urls import path
from .views import userRegistrationView 
from .views import (LogoutView ,CustomTokenObtainPairView)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('registration/', userRegistrationView.as_view(), name='user-register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='user_obtain'),
    path('tokenrefresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]