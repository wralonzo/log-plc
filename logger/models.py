from django.db import models
from equipment.models import Equipment
from usergroup.models import FailureType

# Create your models here.
# Create your models here.
class Logger(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    equipmentId = models.ForeignKey(Equipment,on_delete=models.CASCADE, verbose_name="Equipo")
    failureTypeId = models.ForeignKey(FailureType,on_delete=models.CASCADE, verbose_name="Tipo de anomalía")
    description = models.CharField(verbose_name="Descripión de la accion realizada", max_length=100)
    operador = models.CharField(verbose_name="Nombre del operado", max_length=100)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-equipmentId']
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'