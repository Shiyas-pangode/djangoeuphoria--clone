from django.urls import path
from .views import PlaceOrderView, AdminOrderListView

urlpatterns = [
    path('orderplace/', PlaceOrderView.as_view(), name='place-order'),
    path('orderadmin/', AdminOrderListView.as_view(), name='admin-orders'),
]

