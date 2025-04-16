from rest_framework import serializers

from store.models import Category, Product

# Serilaizer 객체의 주요 기능
# 1) serialization
# 2) deserialiaztion
# 3) validation
# 4) request / response 데이터 핸들링 ( to_internal_value() / to_representation() )
# 5) nested serialization


# # dev_29
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     price = serializers.ImageField()
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     description = serializers.CharField(
#         max_length=250, required=False, allow_blank=True, allow_null=True
#     )
#     image = serializers.ImageField()
#     # created_at = serializers.DateField()
#     # updated_at = serializers.DateField()
#     is_sale = serializers.BooleanField()
#     sale_price = serializers.IntegerField()


# 객체를 딕셔너리로 만드는 게 목적
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "name", "category"]
