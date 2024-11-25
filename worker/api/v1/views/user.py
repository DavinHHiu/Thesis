from datetime import datetime

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from api.authentications import JSONWebTokenAuthentication
from api.models import Address, User
from api.v1.serializers import (
    AddressSerializer,
    BaseJSONWebTokenSerializer,
    BaseRefreshAuthTokenSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
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

    def update(self, request, pk=None, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing user addresses.
    """

    permission_classes = [AllowAny]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        address = self.get_object()
        serializer = self.get_serializer(address, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="by-user")
    def listByUser(self, request, *args, **kwargs):
        addresses = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterApiView(APIView):
    """
    API endpoint for registering a new user.
    """

    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


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
                "user": UserSerializer(user, context={"request": request}).data,
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

    serializer = BaseRefreshAuthTokenSerializer

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


class ChangePasswordApiView(APIView):
    """API endpoint for changing user passwords"""

    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer

    def get_serializer_context(self):
        return {
            "request": self.request,
            "view": self,
        }

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def post(self, request: Request) -> Response:
        """Change password"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
