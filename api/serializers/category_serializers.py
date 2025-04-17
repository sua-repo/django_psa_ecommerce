from rest_framework import serializers
from api.serializers.product_serializers import ProductSimpleSerializer
from store.models import Category, Product


# dev_34 : 순환 구조 피하기 위해
class CategorySimpleSerializer(serializers.ModelSerializer):
    # dev_32 : 역방향 참조
    # products = ProductSerializer(many=True, read_only=True)  # related_name=products

    class Meta:
        model = Category
        fields = ["id", "name"]  # "__all__"


# dev_32
class CategorySerializer(serializers.ModelSerializer):

    products = ProductSimpleSerializer(many=True)  # related_name=products

    class Meta:
        model = Category
        fields = "__all__"
