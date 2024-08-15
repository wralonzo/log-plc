from django.urls import path

from . import views

urlpatterns = [
    path('failuredisplay', views.displayFailure, name='failuredisplay'),
    path('failureregister', views.resgisteFailure, name='failureregister'),
    path('failuredelete', views.deleteFailure, name='failuredelete'),
    
    path('groupdisplay', views.displayGroup, name='groupdisplay'),
    path('groupregister', views.resgisteGrup, name='groupregister'),
    path('groupdelete', views.deleteGroup, name='groupdelete'),
    
    path('groupalertdisplay', views.displayGroupAlert, name='groupalertdisplay'),
    path('groupalertregister', views.resgisteGrupAlert, name='groupalertregister'),
    path('groupalertdelete', views.deleteGroupAlert, name='groupalertdelete'),
]