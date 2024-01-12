"""View module for handling requests about Revenue"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpnwapi.models import Revenue, Orders


class RevenueView(ViewSet):
    """HHPNW revenue view"""

    def retrieve(self, request, pk):
        """Handle GET requests for Revenue"""
        try:
            revenue = Revenue.objects.get(pk=pk)
            serializer = RevenueSerializer(revenue)
            return Response(serializer.data)
        except Revenue.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all revenue"""
        revenue = Revenue.objects.all()
        serializer = RevenueSerializer(revenue, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST revenue"""
        orderid = Orders.objects.get(pk=request.data["orderid"])
        revenue = Revenue.objects.create(
            orderid=orderid,
            date=request.data["date"],
            tipAmount=request.data["tipAmount"],
            paymentType=request.data["paymentType"]
        )
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for revenue"""
        orderid = Orders.objects.get(pk=request.data["orderid"])

        revenue = Revenue.objects.get(pk=pk)
        revenue.tipAmount = request.data["tipAmount"]
        revenue.paymentType = request.data["paymentType"]
        revenue.date = request.data["date"]
        orderid = orderid
        revenue.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for Revenue"""
        revenue = Revenue.objects.get(pk=pk)
        revenue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""
    class Meta:
        model = Orders
        fields = ('id', 'orderName', 'customerEmail', 'open')


class RevenueSerializer(serializers.ModelSerializer):
    """JSON serializer for revenue"""
    order = OrderSerializer(
        source='orderid', read_only=True)

    class Meta:
        model = Revenue
        fields = ('id', 'order', 'tipAmount', 'paymentType', 'date', 'orderid')
