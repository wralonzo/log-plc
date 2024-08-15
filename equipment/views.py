from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
# PLC
@login_required(login_url='login')
def displayPlc(request):
    data = models.Device.objects.all()  # Obtener todos los usuarios
    return render(request, 'catalog/device/index.html', {'data': data})
    

# Create your views here.
@login_required(login_url='login')
def resgistePlc(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deletePlc(request):
    pass

# Create your views here.
# Sensor
@login_required(login_url='login')
def displaySensor(request):
    data = models.Sensor.objects.all()
    return render(request, 'catalog/sensor/index.html', {'data': data})  

# Create your views here.
@login_required(login_url='login')
def resgisteSensor(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deleteSensor(request):
    pass

# Create your views here.
# Equipo
@login_required(login_url='login')
def displayEquipment(request):
    data = models.Equipment.objects.all()
    return render(request, 'catalog/equipment/index.html', {'data': data})  

# Create your views here.
@login_required(login_url='login')
def resgisteEquipment(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deleteEquipment(request):
    pass



