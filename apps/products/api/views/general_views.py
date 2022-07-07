
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.serializers_general import MeasureUnitSerializer,IndicatorSerializer,CategoryProductSerializer
#MeasureUnit
class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer
    
#Indicator
class IndicatorUnitListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer

#CategoryProduct
class CategoryProductUnitListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer

