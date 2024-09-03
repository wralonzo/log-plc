from django.db import models
from equipment.models import Equipment
from usergroup.models import FailureType, GroupEmail
from django.core.mail import send_mail

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
    
    def save(self, *args, **kwargs):
        # Call the parent save method
        super(Logger, self).save(*args, **kwargs)
        typeFalla = FailureType.objects.get(name=self.failureTypeId)
        equipo = Equipment.objects.get(name=self.equipmentId);
        emailType = GroupEmail.objects.filter(failuteId = typeFalla.id)
        destinatarios = [email.userId.email for email in emailType]
        self.enviar_correo(typeFalla.name, 'Se reporto un log de: '+typeFalla.name +', En el equipo'+ equipo.name, destinatarios)
    
    def enviar_correo(self, asunto, mensaje, destinatarios):
        send_mail(
            asunto,
            mensaje,
            'tu_email@example.com',
            destinatarios,
            fail_silently=False,
        )
    class Meta:
        ordering = ['-equipmentId']
        verbose_name = 'Lecturas'
        verbose_name_plural = 'Lecturas'