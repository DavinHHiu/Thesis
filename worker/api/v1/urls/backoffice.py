from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.v1 import views

app_name = 'api'

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]