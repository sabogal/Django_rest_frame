from pydoc import describe
from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.

class MeasureUnit(BaseModel):
    
    descripcion = models.CharField('Descripcion', max_length = 50, blank=False ,null=False )
    historical = HistoricalRecords()

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
