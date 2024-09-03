from django.urls import path

from . import views

urlpatterns = [
    path('plcdisplay', views.displayPlc, name='plcdisplay'),
    path('plcregister', views.resgistePlc, name='plcregister'),
    path('plcdelete/<int:idR>', views.deletePlc, name='plcdelete'),
    path('plcupdate/<int:idR>', views.editPlc, name='plcupdate'),
    
    path('sensordisplay', views.displaySensor, name='sensordisplay'),
    path('sensorregister', views.resgisteSensor, name='sensorregister'),
    path('sensordelete/<int:idR>', views.deleteSensor, name='sensordelete'),
    path('sensorupdate/<int:idR>', views.updateSensor, name='sensorupdate'),
    
    path('equipmentdisplay', views.displayEquipment, name='equipmentdisplay'),
    path('equipmentregister', views.resgisteEquipment, name='equipmentregister'),
    path('equipmentdelete/<int:idR>', views.deleteEquipment, name='equipmentdelete'),
    path('equipmentupdate/<int:idR>', views.updateEquipment, name='equipmentupdate'),
]