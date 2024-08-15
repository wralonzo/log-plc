from django.urls import path

from . import views

urlpatterns = [
    path('logdisplay', views.display, name='logdisplay'),
    path('flogregister', views.resgister, name='flogregister'),
    path('logdelete', views.delete, name='logdelete'),
]