from django.urls import path
from .views import Cart_View


urlpatterns = [
    path('cartview/',Cart_View.as_view() ,name = 'CartManagement'),
]