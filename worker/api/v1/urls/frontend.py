from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1 import views

router = SimpleRouter()

router.register(r"products", views.ProductDisplayViewset, basename="product")
router.register(r"carts", views.CartViewSet, basename="cart")
router.register(r"cart-items", views.CartItemViewSet, basename="cart-item")
router.register(r"order", views.OrderDetailViewSet, basename="order")
router.register(r"order-items", views.OrderItemViewSet, basename="order-item")
router.register(r"addresses", views.AddressViewSet, basename="address")
router.register(
    r"shipment-methods", views.ShipmentMethodViewSet, basename="shipment-method"
)
router.register(
    r"payment-methods", views.PaymentMethodViewSet, basename="payment-method"
)

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("token/", views.BaseObtainJSONWebTokenView.as_view(), name="eu-token"),
    path(
        "token/refresh/",
        views.EURefreshJSONWebTokenView.as_view(),
        name="eu-token-refresh",
    ),
    path("create-payment/", views.CreatePaymentView.as_view(), name="create-payment"),
    path(
        "execute-payment/", views.ExecutePaymentView.as_view(), name="execute-payment"
    ),
]

urlpatterns.append(path("", include(router.urls)))
