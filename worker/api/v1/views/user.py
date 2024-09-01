from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Address, User
from api.v1.serializers import AddressSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing user addresses.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
