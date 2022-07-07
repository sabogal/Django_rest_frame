
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.serializers_product import ProductSerializer

class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer