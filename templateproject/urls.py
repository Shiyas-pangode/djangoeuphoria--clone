
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include('euphoria.urls')),

    path('api/' ,include('api.v1.tasks.urls')),

    path('cart/' ,include('api.v1.cart.urls')),

]
