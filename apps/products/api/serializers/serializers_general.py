from apps.products.models import MeasureUnit,CategoryProduct,Indicator
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state','create_date','modify_date','delete_date')

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state','create_date','modify_date','delete_date')
        
class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        
        exclude = ('state','create_date','modify_date','delete_date')
        
