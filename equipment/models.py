from django.db import models

# Create your models here.
class Device(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Nombre del PLC", max_length=100)
    location = models.CharField(verbose_name="Ubicación", max_length=100)
    encargado = models.CharField(verbose_name="Nombre del encargado", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = 'PLC'
        verbose_name_plural = 'PLC'
        
# Create your models here.
class Sensor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Nombre del sensor", max_length=100)
    deviceId = models.ForeignKey(Device,on_delete=models.CASCADE, verbose_name="PLC asociado", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensores'
        
# Create your models here.
class Equipment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Nombre del equipo", max_length=100)
    sensorId = models.ForeignKey(Device,on_delete=models.CASCADE, verbose_name="Sensor asociado", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'