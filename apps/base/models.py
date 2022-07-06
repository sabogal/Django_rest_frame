from datetime import datetime
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    
    id = models.AutoField(primary_key= True)
    state = models.BooleanField('Estado', default = True)
    create_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modify_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)
    class Meta:
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
        
    def __str__(self):
        pass
    