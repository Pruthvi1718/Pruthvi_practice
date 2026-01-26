from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    Address,
    Cart,
    CartItem,
    Coupon,
    Order,
    OrderItem,
    Payment,
    ServiceRequest,
    User,
    WishlistItem,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    list_display = ["email", "first_name", "last_name", "phone", "is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "phone", "title", "gender", "date_of_birth", "anniversary_date")},
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2", "is_staff", "is_superuser"),
            },
        ),
    )
    search_fields = ["email", "first_name", "last_name", "phone"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "city", "state", "country", "is_default"]
    list_filter = ["city", "state", "country", "is_default"]
    search_fields = ["full_name", "city", "state", "country", "postal_code"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "updated_at"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity", "price_at_add", "created_at"]


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "created_at"]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "discount_type", "amount", "is_active", "starts_at", "ends_at"]
    list_filter = ["discount_type", "is_active"]
    search_fields = ["code"]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "status", "total_amount", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["id", "user__email"]
    inlines = [OrderItemInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["order", "method", "status", "amount", "created_at"]
    list_filter = ["method", "status"]
    search_fields = ["order__id", "transaction_id"]


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ["user", "subject", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["subject", "user__email"]
