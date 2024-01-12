"""View module for handling requests about Users"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hhpnwapi.models import User


class UserView(ViewSet):
    """HHPNW user view"""

    def retrieve(self, request, pk):
        """Handle GET requests for Users"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST users"""
        user = User.objects.create(
            uid=request.data["uid"],
            joinDate=request.data["joinDate"],
            hasAccess=request.data["hasAccess"]
        )


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user"""
    class Meta:
        model = User
        fields = ('uid', 'joinDate', 'hasAccess')
