from rest_framework import serializers
from .models import Brand, Category, Inventory, Product, ProductImage, ProductSpec, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent", "is_active"]
        read_only_fields = ["id"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "slug"]
        read_only_fields = ["id"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "alt_text", "is_primary"]
        read_only_fields = ["id"]


class ProductSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpec
        fields = ["id", "name", "value"]
        read_only_fields = ["id"]


class InventorySerializer(serializers.ModelSerializer):
    available_stock = serializers.IntegerField(read_only=True)

    class Meta:
        model = Inventory
        fields = ["id", "stock", "reserved", "available_stock", "updated_at"]
        read_only_fields = ["id", "available_stock", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    specs = ProductSpecSerializer(many=True, required=False)
    inventory = InventorySerializer(required=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "sku",
            "category",
            "brand",
            "price",
            "mrp",
            "color",
            "size",
            "is_active",
            "images",
            "specs",
            "inventory",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        images = validated_data.pop("images", [])
        specs = validated_data.pop("specs", [])
        inventory = validated_data.pop("inventory", None)
        product = Product.objects.create(**validated_data)
        for image in images:
            ProductImage.objects.create(product=product, **image)
        for spec in specs:
            ProductSpec.objects.create(product=product, **spec)
        if inventory:
            Inventory.objects.create(product=product, **inventory)
        return product

    def update(self, instance, validated_data):
        images = validated_data.pop("images", None)
        specs = validated_data.pop("specs", None)
        inventory = validated_data.pop("inventory", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if images is not None:
            instance.images.all().delete()
            for image in images:
                ProductImage.objects.create(product=instance, **image)
        if specs is not None:
            instance.specs.all().delete()
            for spec in specs:
                ProductSpec.objects.create(product=instance, **spec)
        if inventory is not None:
            Inventory.objects.update_or_create(product=instance, defaults=inventory)
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "product", "user", "rating", "title", "comment", "is_approved", "created_at"]
        read_only_fields = ["id", "user", "is_approved", "created_at"]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
