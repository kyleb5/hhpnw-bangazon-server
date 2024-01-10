"""View module for handling requests about Orders"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpnwapi.models import Orders


class OrderView(ViewSet):
    """HHPNW event view"""

    def retrieve(self, request, pk):
        """Handle GET requests for Orders"""
        orders = Orders.objects.get(pk=pk)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get ALL orders"""
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        orders = Orders.objects.create(
            customerEmail=request.data["customerEmail"],
            customerPhone=request.data["customerPhone"],
            date=request.data["data"],
            open=request.data["open"],
            orderName=request.data["orderName"],
            orderType=request.data["orderType"],
            uid=request.data["uid"]
        )
        serializer = OrderSerializer(orders)
        return Response(serializer.data)


class OrderSerializer(serializers.ModelSerializer):
    """JSON serilaizer for order"""
    class Meta:
        model = Orders
        fields = ('id', 'customerEmail', 'customerPhone', 'date',
                  'open', 'orderName', 'orderType', 'uid')
