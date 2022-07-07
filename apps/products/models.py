from itertools import product
from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
#Modelo Num.1-
class MeasureUnit(BaseModel):
    
    descripcion = models.CharField('Descripcion', max_length = 50, blank=False ,null=False, unique= True )
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Unidad de Medida")
        verbose_name_plural =("Unidades de Medidas")

    def __str__(self):
        return self.descripcion
#Modelo Num.2
class CategoryProduct(BaseModel):
    
    descripcion = models.CharField('Descripcion', max_length = 50, blank=False ,null=False, unique= True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categoria de productos"
    
    def __str__(self):
        return self.descripcion
#Modelo Num.3
class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product =models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name= 'Indicador de Oferta')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'Oferta de la Categoria{self.category_product} : {self.descount_value}%'
    
#Modelo Principal

class Product(BaseModel):
    
    name = models.CharField('Nombre de Product', max_length=30, unique = True, blank= False, null= False )
    description = models.TextField('Descripcion de Producto', blank=False, null= False)
    image =models.ImageField('Imagen del Producto', upload_to='products/', blank = True, null = True)
    measure_unit = models.ForeignKey(MeasureUnit, verbose_name='Unidad de Medida', on_delete=models.CASCADE, null= True)
    category_product = models.ForeignKey(CategoryProduct, verbose_name='Indicador de Oferta', on_delete=models.CASCADE, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name
    

