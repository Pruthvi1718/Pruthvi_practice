from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BrandViewSet,
    CategoryViewSet,
    InventoryViewSet,
    ProductImageViewSet,
    ProductSpecViewSet,
    ProductViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"product-images", ProductImageViewSet, basename="product-image")
router.register(r"product-specs", ProductSpecViewSet, basename="product-spec")
router.register(r"inventories", InventoryViewSet, basename="inventory")
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("", include(router.urls)),
]
