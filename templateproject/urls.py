
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include('euphoria.urls')),

    path('api/' ,include('api.v1.tasks.urls')),

]
