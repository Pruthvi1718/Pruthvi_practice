from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from products.models import Product
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "first_name",
            "last_name",
            "title",
            "gender",
            "date_of_birth",
            "anniversary_date",
        ]
        read_only_fields = ["id", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "phone",
            "first_name",
            "last_name",
            "title",
            "gender",
            "date_of_birth",
            "anniversary_date",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Cart.objects.create(user=user)
        return user


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "full_name",
            "phone",
            "line1",
            "line2",
            "city",
            "state",
            "country",
            "postal_code",
            "address_type",
            "is_default",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = [
            "id",
            "product",
            "product_id",
            "quantity",
            "price_at_add",
            "created_at",
        ]
        read_only_fields = ["id", "price_at_add", "created_at", "product"]

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "updated_at", "items"]
        read_only_fields = ["id", "updated_at", "items"]


class WishlistItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WishlistItem
        fields = ["id", "product", "product_id", "created_at"]
        read_only_fields = ["id", "product", "created_at"]


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "id",
            "code",
            "description",
            "discount_type",
            "amount",
            "min_order_amount",
            "max_discount_amount",
            "is_active",
            "starts_at",
            "ends_at",
        ]
        read_only_fields = ["id"]


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "unit_price", "total_price"]
        read_only_fields = ["id", "product", "unit_price", "total_price"]


class OrderCreateItemSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source="product")
    quantity = serializers.IntegerField(min_value=1)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    items_payload = OrderCreateItemSerializer(many=True, write_only=True)
    coupon_code = serializers.CharField(write_only=True, required=False, allow_blank=True)
    shipping_address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), source="shipping_address", write_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "subtotal_amount",
            "discount_amount",
            "total_amount",
            "coupon",
            "shipping_address",
            "shipping_address_id",
            "items",
            "items_payload",
            "coupon_code",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "subtotal_amount",
            "discount_amount",
            "total_amount",
            "coupon",
            "shipping_address",
            "items",
            "created_at",
            "updated_at",
        ]

    def validate_shipping_address(self, value):
        request = self.context.get("request")
        if request and value.user != request.user:
            raise serializers.ValidationError("Shipping address must belong to the current user.")
        return value

    def _apply_coupon(self, coupon, subtotal):
        if coupon.discount_type == "percent":
            discount = (subtotal * coupon.amount) / Decimal("100")
        else:
            discount = coupon.amount
        if coupon.max_discount_amount is not None:
            discount = min(discount, coupon.max_discount_amount)
        return max(discount, Decimal("0"))

    def create(self, validated_data):
        items_payload = validated_data.pop("items_payload", [])
        coupon_code = validated_data.pop("coupon_code", "").strip()
        user = self.context["request"].user

        if not items_payload:
            raise serializers.ValidationError({"items_payload": "At least one item is required."})

        subtotal = Decimal("0")
        for item in items_payload:
            product = item["product"]
            quantity = item["quantity"]
            subtotal += product.price * quantity

        coupon = None
        discount = Decimal("0")
        if coupon_code:
            now = timezone.now()
            coupon = Coupon.objects.filter(code__iexact=coupon_code, is_active=True).first()
            if not coupon:
                raise serializers.ValidationError({"coupon_code": "Invalid coupon code."})
            if coupon.starts_at and coupon.starts_at > now:
                raise serializers.ValidationError({"coupon_code": "Coupon not active yet."})
            if coupon.ends_at and coupon.ends_at < now:
                raise serializers.ValidationError({"coupon_code": "Coupon expired."})
            if subtotal < coupon.min_order_amount:
                raise serializers.ValidationError({"coupon_code": "Order amount below minimum for coupon."})
            discount = self._apply_coupon(coupon, subtotal)

        total = max(subtotal - discount, Decimal("0"))

        with transaction.atomic():
            order = Order.objects.create(
                user=user,
                subtotal_amount=subtotal,
                discount_amount=discount,
                total_amount=total,
                coupon=coupon,
                shipping_address=validated_data["shipping_address"],
            )
            for item in items_payload:
                product = item["product"]
                quantity = item["quantity"]
                unit_price = product.price
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    total_price=unit_price * quantity,
                )
            return order


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "order", "method", "status", "transaction_id", "amount", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_order(self, value):
        request = self.context.get("request")
        if request and not request.user.is_staff and value.user != request.user:
            raise serializers.ValidationError("Order must belong to the current user.")
        return value


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ["id", "subject", "message", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "status", "created_at", "updated_at"]
