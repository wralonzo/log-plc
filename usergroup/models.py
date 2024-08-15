from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Group(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Nombre del grupo", max_length=100)
    key = models.CharField(verbose_name="Id del grupo", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = 'Grupos de notificaciones'
        verbose_name_plural = 'Grupos de notificaciones'
        
# Create your models here.
class FailureType(models.Model):
    name = models.CharField(verbose_name="Nombre de fallta", max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name   
     
    class Meta:
        ordering = ['-name']
        verbose_name = 'Tipo de anomalía'
        verbose_name_plural = 'Tipo de anomalía'
    
# Create your models here.
class GroupEmail(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Usuario")
    groupId = models.ForeignKey(Group,on_delete=models.CASCADE, verbose_name="Grupo")
    key = models.CharField(verbose_name="Identificador de la anomalía", max_length=100)
    failuteId = models.ForeignKey(FailureType,on_delete=models.CASCADE, verbose_name="Tipo de anomalía")
    
    def __str__(self):
        return self.userId
    
    class Meta:
        ordering = ['-groupId']
        verbose_name = 'Grupos de usuarios'
        verbose_name_plural = 'Grupos de usuarios'
    

