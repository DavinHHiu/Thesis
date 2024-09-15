from datetime import datetime

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from api.authentications import JSONWebTokenAuthentication
from api.models import Address, User
from api.v1.serializers import (
    AddressSerializer,
    BaseJSONWebTokenSerializer,
    BaseRefreshAuthTokenSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [AllowAny]

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


class RegisterApiView(APIView):
    """
    API endpoint for registering a new user.
    """

    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JSONWebTokenViewMixin(APIView):
    """Base clase authentication by token"""

    authentication_class = None

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            "request": self.request,
            "view": self,
        }

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get("user") or request.user
            token = serializer.validated_data.get("token")
            issued_at = serializer.validated_data.get("issued_at")
            response_data = {
                "token": token,
                "user": UserSerializer(user).data,
                "issued_at": issued_at,
            }
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
                response.set_cookie(
                    api_settings.JWT_AUTH_COOKIE,
                    token,
                    expires=expiration,
                    httponly=True,
                )

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseObtainJSONWebTokenView(JSONWebTokenViewMixin):
    """ObtainJSONWebTokenView"""

    permission_classes = [AllowAny]
    serializer_class = BaseJSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BaseRefreshJSONWebTokenView(JSONWebTokenViewMixin):
    """認証トークンの更新"""

    def post(self, request, *args, **kwargs) -> Response:
        """認証トークンを更新する"""
        response = super().post(request, *args, **kwargs)

        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return response

        return response


class BORefreshJSONWebTokenView(BaseRefreshJSONWebTokenView):
    """BORefresh"""

    permission_classes = [AllowAny]
    authentication_class = JSONWebTokenAuthentication
    serializer_class = BaseRefreshAuthTokenSerializer


class EURefreshJSONWebTokenView(BaseRefreshJSONWebTokenView):
    """EU 認証トークンの更新"""

    permission_classes = [AllowAny]
    authentication_class = JSONWebTokenAuthentication
    serializer_class = BaseRefreshAuthTokenSerializer
