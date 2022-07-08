
from apps.products.models import MeasureUnit, Product
from rest_framework import serializers
from apps.products.api.serializers.serializers_general import MeasureUnitSerializer,CategoryProductSerializer
class ProductSerializer(serializers.ModelSerializer):

### primera opcion para mostrar los valores de las llaves foraneas
    #measure_unit = MeasureUnitSerializer()
    #category_product = CategoryProductSerializer()
########
### segunda opcion para mostrar los valores de las llaves foraneas
## Se le llama los campos de el metodo Meta en el campo __str__
    #measure_unit = serializers.StringRelatedField()
    #category_product= serializers.StringRelatedField()
########
    class Meta:
        model = Product
        exclude = ('state','create_date','modify_date','delete_date')

### primera opcion para mostrar los valores de las llaves foraneas

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.descripcion if instance.measure_unit is not None else '',
            'category_product': instance.category_product.descripcion if instance.category_product is not None else '',
        }