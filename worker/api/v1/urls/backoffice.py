from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1 import views

router = SimpleRouter()
router.register(r"carts", views.CartViewSet, basename="cart")
router.register(r"cart-items", views.CartItemViewSet, basename="cart-items")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"sub-categories", views.SubCategoryViewSet, basename="sub-categories")
router.register(r"orders", views.OrderDetailViewSet, basename="order-detail")
router.register(r"order-items", views.OrderDetailViewSet, basename="order-items")
router.register(r"payment", views.PaymentViewSet, basename="payment")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(
    r"product-attributes", views.ProductAttributeViewSet, basename="product-attribute"
)
router.register(r"shipments", views.ShipmentViewSet, basename="shipment")
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"wishlists", views.WishListViewSet, basename="wishlist")

urlpatterns = []

urlpatterns.append(path("", include(router.urls)))
