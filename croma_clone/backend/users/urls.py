from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewSet,
    CartItemViewSet,
    CartView,
    CouponViewSet,
    OrderViewSet,
    PaymentViewSet,
    ServiceRequestViewSet,
    WishlistItemViewSet,
)

router = DefaultRouter()
router.register(r"addresses", AddressViewSet, basename="address")
router.register(r"cart-items", CartItemViewSet, basename="cart-item")
router.register(r"wishlist", WishlistItemViewSet, basename="wishlist")
router.register(r"coupons", CouponViewSet, basename="coupon")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"payments", PaymentViewSet, basename="payment")
router.register(r"service-requests", ServiceRequestViewSet, basename="service-request")

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("", include(router.urls)),
]
