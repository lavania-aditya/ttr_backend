from rest_framework import serializers

from apps.categories.models import Category
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "category",
            "image_url",
            "stock",
            "created_at",
            "updated_at",
        ]

    def get_category(self, obj):
        return {
            "id": obj.category_id,
            "name": obj.category.name,
            "slug": obj.category.slug,
        }


class ProductWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category")

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "description", "price", "category_id", "image_url", "stock", "created_at", "updated_at"]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]
