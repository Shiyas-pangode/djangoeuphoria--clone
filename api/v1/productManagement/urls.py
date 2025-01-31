from django.urls import path
from . import views


urlpatterns = [
    path('product/' ,views.create_product.as_view() ),

    path('product/<int:pk>/' , views.ProductRetrieve.as_view()),
   

]