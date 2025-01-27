from django.urls import path
from api.v1.tasks import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [


    path('', views.api , name = 'api'),

    path('post/', views.create_api , name = 'postrequest'),
    path('post/<int:pk>/', views.detail_api , name = 'detailrequest'),

    path('token/' ,jwt_views.TokenObtainPairView.as_view(),name ='token_refresh'),
    path('refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),

    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
]