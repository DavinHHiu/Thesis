from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from api.v1 import views

urlpatterns = [
    path("bo/", include("api.v1.urls.backoffice"), name="backoffice"),
    path("eu/", include("api.v1.urls.frontend"), name="frontend"),
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
