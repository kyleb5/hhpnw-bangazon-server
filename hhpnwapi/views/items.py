"""View module for handling requests about Items"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpnwapi.models import Items


class ItemView(ViewSet):
    """HHPNW item view"""

    def retrieve(self, request, pk):
        """Handle GET requests for Items"""
        try:
            items = Items.objects.get(pk=pk)
            serializer = ItemSerializer(items)
            return Response(serializer.data)
        except Items.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL items"""
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle CREATE requests for items"""
        items = Items.objects.create(
            name=request.data["name"],
            img=request.data["img"],
            price=request.data["price"],
            type=request.data["type"],
            description=request.data["description"]
        )
        serializer = ItemSerializer(items)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """Handle PUT requests for updating items"""
        items = Items.objects.get(pk=pk)
        items.name = request.data.get["name"]
        items.img = request.data.get["img"]
        items.price = request.data.get["price"]
        items.type = request.data.get["type"]
        items.description = request.data["description"]
        items.save()

        serializer = ItemSerializer(items)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """Handle DELETE requests for ITEMS"""
        items = Items.objects.get(pk=pk)
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serlazier for ITEMS"""

    class Meta:
        model = Items
        fields = ('id', 'name', 'img', 'price', 'type', 'description')
        depth = 1
