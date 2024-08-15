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
    
    path('failuredisplay', views.displayPlc, name='failuredisplay'),
    path('failureregister', views.resgistePlc, name='failureregister'),
    path('failuredelete', views.deletePlc, name='failuredelete'),
    
    path('groupdisplay', views.displayPlc, name='groupdisplay'),
    path('groupregister', views.resgistePlc, name='groupregister'),
    path('groupdelete', views.deletePlc, name='groupdelete'),
    
    path('groupalertdisplay', views.displayPlc, name='groupalertdisplay'),
    path('groupalertregister', views.resgistePlc, name='groupalertregister'),
    path('groupalertdelete', views.deletePlc, name='groupalertdelete'),
]