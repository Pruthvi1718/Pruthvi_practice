from django.contrib import admin
from .models import Brand, Category, Inventory, Product, ProductImage, ProductSpec, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "parent", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "slug"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductSpecInline(admin.TabularInline):
    model = ProductSpec
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "category", "brand", "price", "mrp", "is_active"]
    list_filter = ["is_active", "category", "brand"]
    search_fields = ["name", "sku"]
    inlines = [ProductImageInline, ProductSpecInline]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["product", "stock", "reserved", "updated_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "rating", "is_approved", "created_at"]
    list_filter = ["rating", "is_approved"]
