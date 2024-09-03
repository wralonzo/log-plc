from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from equipment.forms import DeviceCreateForm, EquipmentCreateForm, SensorCreateForm
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
    if request.method == 'POST':
        form = DeviceCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plcdisplay')
    else:
        form = DeviceCreateForm()
    return render(request, 'catalog/device/register.html', {'form': form})

@login_required(login_url='login')
def editPlc(request, idR):
    data = models.Device.objects.get(id=idR)
    if request.method == 'POST':
        form = DeviceCreateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('plcdisplay')
    else:
        form = DeviceCreateForm(instance=data)
    return render(request, 'catalog/device/update.html', {'form': form})
    
@login_required(login_url='login')
def deletePlc(request, idR):
    data = models.Device.objects.get(id=idR)
    if data.delete():
        return redirect('plcdisplay')
    else:
        return redirect('plcdisplay')
    
# Sensor
@login_required(login_url='login')
def displaySensor(request):
    data = models.Sensor.objects.all()
    return render(request, 'catalog/sensor/index.html', {'data': data})  

# Create your views here.
@login_required(login_url='login')
def resgisteSensor(request):
    if request.method == 'POST':
        form = SensorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensordisplay')
    else:
        form = SensorCreateForm()
    return render(request, 'catalog/sensor/register.html', {'form': form})

@login_required(login_url='login')
def updateSensor(request, idR):
    data = models.Sensor.objects.get(id=idR)
    if request.method == 'POST':
        form = SensorCreateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('sensordisplay')
    else:
        form = SensorCreateForm(instance=data)
    return render(request, 'catalog/sensor/update.html', {'form': form})

@login_required(login_url='login')
def deleteSensor(request, idR):
    data = models.Sensor.objects.get(id=idR)
    if data.delete():
        return redirect('sensordisplay')
    else:
        return redirect('sensordisplay')

# Create your views here.
# Equipo
@login_required(login_url='login')
def displayEquipment(request):
    data = models.Equipment.objects.all()
    return render(request, 'catalog/equipment/index.html', {'data': data})  

# Create your views here.
@login_required(login_url='login')
def resgisteEquipment(request):
    if request.method == 'POST':
        form = EquipmentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipmentdisplay')
    else:
        form = EquipmentCreateForm()
    return render(request, 'catalog/equipment/register.html', {'form': form})

# Create your views here.
@login_required(login_url='login')
def updateEquipment(request, idR):
    data = models.Equipment.objects.get(id=idR)
    if request.method == 'POST':
        form = EquipmentCreateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('equipmentdisplay')
    else:
        form = EquipmentCreateForm(instance=data)
    return render(request, 'catalog/equipment/update.html', {'form': form})


@login_required(login_url='login')
def deleteEquipment(request, idR):
    data = models.Equipment.objects.get(id=idR)
    if data.delete():
        return redirect('equipmentdisplay')
    else:
        return redirect('equipmentdisplay')



