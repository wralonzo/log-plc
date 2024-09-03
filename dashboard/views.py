import django
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.db.models.functions import TruncMonth, TruncDay
from django.utils import timezone
from datetime import datetime, timedelta
from equipment.models import Device, Equipment, Sensor
from logger.models import Logger


def enviar_correo(asunto, mensaje, destinatarios):
    send_mail(
        asunto,
        mensaje,
        'tu_email@example.com',
        destinatarios,
        fail_silently=False,
    )

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    dataLog = Logger.objects.select_related('failureTypeId').select_related('failureTypeId__name').values('failureTypeId').values('failureTypeId__name').annotate(total=Count('failureTypeId')).order_by('failureTypeId')
    dataSensor = Sensor.objects.select_related('deviceId').select_related('deviceId__name').values('deviceId').values('deviceId__name').annotate(total=Count('deviceId')).order_by('deviceId')
    dataEquipment = Equipment.objects.select_related('sensorId').select_related('sensorId__name').values('sensorId').values('sensorId__name').annotate(total=Count('sensorId')).order_by('sensorId')
    context = {
        'labelsFalla': [item['failureTypeId__name'] for item in dataLog],
        'dataFalla': [item['total'] for item in dataLog],
        'labelsSensor': [item['deviceId__name'] for item in dataSensor],
        'dataSensor': [item['total'] for item in dataSensor],
        'labelsE': [item['sensorId__name'] for item in dataEquipment],
        'dataE': [item['total'] for item in dataEquipment],
    }
    print(list(dataEquipment));
    
    return render(request, 'dashboard/home.html', context)






def getLogs(request):
    asunto = 'Alerta de correo'
    mensaje = 'Se ha realizo una accion en PLC tal'
    destinatarios = ['test@gmail.com', 'test@gmail.com', 'test@gmail.com']
    # enviar_correo(asunto, mensaje, destinatarios)
    # Pass data to the template
    data = Logger.objects.select_related('failureTypeId').select_related('failureTypeId__name').values('failureTypeId').values('failureTypeId__name').annotate(total=Count('failureTypeId')).order_by('failureTypeId')
    print(list(data));
    # Prepare data for the template
    context = {
        'labelsFalla': [item['failureTypeId__name'] for item in data],
        'dataFalla': [item['total'] for item in data],'labelsFalla': [item['failureTypeId__name'] for item in data],
        'labelSensor': [item['name'] for item in data],
        'dataSensor': [item['total'] for item in data],'labelSensor': [item['deviceId'] for item in data],
    }
    
    return render(request, 'dashboard/logger.html', context)