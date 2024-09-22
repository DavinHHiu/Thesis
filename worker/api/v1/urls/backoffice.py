from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1 import views

router = SimpleRouter()
router.register(r"addresses", views.AddressViewSet, basename="address")
router.register(r"carts", views.CartViewSet, basename="cart")
router.register(r"cart-items", views.CartItemViewSet, basename="cart-item")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"sub-categories", views.SubCategoryViewSet, basename="sub-category")
router.register(r"orders", views.OrderDetailViewSet, basename="order-detail")
router.register(r"order-items", views.OrderDetailViewSet, basename="order-item")
router.register(r"payment", views.PaymentViewSet, basename="payment")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"product-skus", views.ProductSkuViewSet, basename="product-sku")
router.register(r"product-images", views.ProductImageViewSet, basename="product-images")
router.register(
    r"products-display", views.ProductDisplayViewset, basename="product-display"
)
router.register(
    r"product-attributes", views.ProductAttributeViewSet, basename="product-attribute"
)
router.register(r"shipments", views.ShipmentViewSet, basename="shipment")
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"wishlists", views.WishListViewSet, basename="wishlist")

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("token/", views.BaseObtainJSONWebTokenView.as_view(), name="token"),
    path(
        "token/refresh/",
        views.BORefreshJSONWebTokenView.as_view(),
        name="token-refresh",
    ),
]

urlpatterns.append(path("", include(router.urls)))
