from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.v1 import views


router = SimpleRouter()
router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
]

urlpatterns.append(path("", include(router.urls)))