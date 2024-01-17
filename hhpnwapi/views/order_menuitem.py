"""View module for handling requests about Order Menu Items"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpnwapi.models import Items, Orders, OrderMenuItem


class OrderMenuItemView(ViewSet):
    """HHPNW order item menu"""

    def retrieve(self, request, pk):
        """Handle GET requests for item orders"""
        try:
            ordermenuitem = OrderMenuItem.objects.get(pk=pk)
            serializer = OrderMenuItemSerializer(ordermenuitem)
            return Response(serializer.data)
        except OrderMenuItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all items in orders"""
        ordermenuitems = OrderMenuItem.objects.all()
        serializer = OrderMenuItemSerializer(ordermenuitems, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST order menu item"""
        orders = Orders.objects.get(pk=request.data["orders"])
        items = Items.objects.get(pk=request.data["items"])
        ordermenuitem = OrderMenuItem.objects.create(
            orders=orders,
            items=items
        )
        serializer = OrderMenuItemSerializer(ordermenuitem)
        return Response(serializer.data)


class OrderMenuItemSerializer(serializers.ModelSerializer):
    """JSON serializer for order menu item"""
    class Meta:
        model = OrderMenuItem
        fields = ('id', 'orders', 'items')
