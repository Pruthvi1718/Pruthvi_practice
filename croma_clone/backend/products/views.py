from django.db.models import Q
from rest_framework import permissions, viewsets

from users.permissions import IsOwnerOrAdmin
from .models import Brand, Category, Inventory, Product, ProductImage, ProductSpec, Review
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    InventorySerializer,
    ProductImageSerializer,
    ProductSerializer,
    ProductSpecSerializer,
    ReviewSerializer,
)


class ReadOnlyOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyOrAdmin]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [ReadOnlyOrAdmin]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "brand").all()
    serializer_class = ProductSerializer
    permission_classes = [ReadOnlyOrAdmin]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.select_related("product").all()
    serializer_class = ProductImageSerializer
    permission_classes = [ReadOnlyOrAdmin]


class ProductSpecViewSet(viewsets.ModelViewSet):
    queryset = ProductSpec.objects.select_related("product").all()
    serializer_class = ProductSpecSerializer
    permission_classes = [ReadOnlyOrAdmin]


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.select_related("product").all()
    serializer_class = InventorySerializer
    permission_classes = [ReadOnlyOrAdmin]


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Review.objects.select_related("product", "user").all()
        if self.request.user.is_authenticated:
            return Review.objects.filter(Q(is_approved=True) | Q(user=self.request.user))
        return Review.objects.filter(is_approved=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
