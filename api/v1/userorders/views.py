from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from euphoria.models import Order
from .serializers import OrderSerializer

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can place orders

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id  # Assign the logged-in user
        serializer = OrderSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order placed successfully!", "order": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminOrderListView(APIView):
    permission_classes = [IsAdminUser]  # Only admins can view all orders

    def get(self, request):
        orders = Order.objects.all().order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
