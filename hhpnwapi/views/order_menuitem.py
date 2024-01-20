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
            order = Orders.objects.get(pk=pk)
            ordermenuitems = OrderMenuItem.objects.filter(orders=order)

            if ordermenuitems.exists():
                ordermenuitems_data = OrderMenuItemSerializer(
                    ordermenuitems, many=True).data

                # Fetch item details and order uid for each order menu item
                for ordermenuitem in ordermenuitems_data:
                    item_id = ordermenuitem['items']
                    item = Items.objects.get(pk=item_id)
                    item_data = ItemSerializer(item).data
                    ordermenuitem['item_details'] = item_data
                    ordermenuitem['order_uid'] = order.uid

                return Response(ordermenuitems_data)
            else:
                # Error 404 Not Found if order was found but no items
                # Fixed Error
                return Response([])

        except Orders.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

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

    def destroy(self, request, pk):
        """Handle DELETE requests for order menu item"""
        ordermenuitem = OrderMenuItem.objects.get(pk=pk)
        ordermenuitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for item"""
    class Meta:
        model = Items
        fields = ('id', 'name', 'img', 'type', 'price', 'description')


class OrderMenuItemSerializer(serializers.ModelSerializer):
    """JSON serializer for order menu item"""
    # Include the 'order_uid' field in the serializer
    order_uid = serializers.CharField(source='orders.uid', read_only=True)

    order_open = serializers.BooleanField(source='orders.open', read_only=True)

    price = serializers.IntegerField(source='items.price', read_only=True)

    class Meta:
        model = OrderMenuItem
        fields = ('id', 'orders', 'items', 'order_uid', 'price', 'order_open')
