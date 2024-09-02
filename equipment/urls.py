from django.urls import path

from . import views

urlpatterns = [
    path('plcdisplay', views.displayPlc, name='plcdisplay'),
    path('plcregister', views.resgistePlc, name='plcregister'),
    path('plcdelete', views.deletePlc, name='plcdelete'),
    
    
    path('sensordisplay', views.displaySensor, name='sensordisplay'),
    path('sensorregister', views.resgisteSensor, name='sensorregister'),
    path('sensordelete', views.deleteSensor, name='sensordelete'),
    
    path('equipmentdisplay', views.displayEquipment, name='equipmentdisplay'),
    path('equipmentregister', views.resgisteEquipment, name='equipmentregister'),
    path('equipmentdelete', views.deletePlc, name='equipmentdelete'),
]