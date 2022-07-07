from lib2to3.pytree import Base
from pydoc import describe
from xml.parsers.expat import model
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
        return self.name
#Modelo Num.2
class CategoryProduct(BaseModel):
    
    descripcion = models.CharField('Descripcion', max_length = 50, blank=False ,null=False, unique= True)
    measure_unit = models.ForeignKey("MearsureUnit", verbose_name="Unidad de Medida", on_delete=models.CASCADE)
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
