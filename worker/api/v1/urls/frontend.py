from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1 import views

router = SimpleRouter()

router.register(r"addresses", views.AddressViewSet, basename="address")
router.register(r"provinces", views.ProvinceViewSet, basename="province")
router.register(r"districts", views.DistrictViewSet, basename="district")
router.register(r"wards", views.WardViewSet, basename="ward")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"subcategories", views.SubCategoryViewSet, basename="subcategory")
router.register(r"carts", views.CartViewSet, basename="cart")
router.register(r"cart-items", views.CartItemViewSet, basename="cart-item")
router.register(r"orders", views.OrderDetailViewSet, basename="order")
router.register(r"order-items", views.OrderItemViewSet, basename="order-item")
router.register(
    r"payment-methods", views.PaymentMethodViewSet, basename="payment-method"
)
router.register(r"products", views.ProductDisplayViewset, basename="product")
router.register(
    r"shipment-methods", views.ShipmentMethodViewSet, basename="shipment-method"
)
router.register(r"users", views.UserViewSet, basename="users")

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
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    path("search/by-image/", views.SearchByImageApiView.as_view(), name="search"),
]

urlpatterns.append(path("", include(router.urls)))
