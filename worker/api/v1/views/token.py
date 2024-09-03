from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
