from rest_framework import viewsets

from api.models import User
from api.v1.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    """
    API endpoint for managing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    