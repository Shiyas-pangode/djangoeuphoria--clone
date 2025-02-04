
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', include('euphoria.urls')),

    path('api/' ,include('api.v1.tasks.urls')),

    path('api/product/' ,include('api.v1.productManagement.urls')),

    path( 'api/auth/' ,include('api.v1.userAuthentication.urls')),
    
    path( 'api/Cart/' ,include('api.v1.CartManagement.urls')),
    
    path( 'api/order/' , include('api.v1.userorders.urls')),

]
