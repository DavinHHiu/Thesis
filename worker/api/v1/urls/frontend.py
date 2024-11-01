from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1 import views

router = SimpleRouter()

router.register(r"products", views.ProductDisplayViewset, basename="product")
router.register(r"carts", views.CartViewSet, basename="cart")
router.register(r"cart-items", views.CartItemViewSet, basename="cart-item")

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("token/", views.BaseObtainJSONWebTokenView.as_view(), name="eu-token"),
    path(
        "token/refresh/",
        views.EURefreshJSONWebTokenView.as_view(),
        name="eu-token-refresh",
    ),
]

urlpatterns.append(path("", include(router.urls)))
