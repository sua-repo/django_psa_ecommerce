from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProductSerializer
from store.models import Product


@api_view(["GET"])
def products_api(request):

    if request.method == "GET":
        products = Product.objects.all()

        # many=True : 여러 개의 인스턴스 (QuertSet, 리스트 등)
        # many=False (기본값) : 단일 인스턴스
        serializer = ProductSerializer(products, many=True)

        print(serializer.data)
        return Response(serializer.data)
