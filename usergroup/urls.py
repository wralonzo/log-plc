from django.urls import path

from . import views

urlpatterns = [
    path('failuredisplay', views.displayFailure, name='failuredisplay'),
    path('failureregister', views.resgisteFailure, name='failureregister'),
    path('failuredelete/<int:idR>', views.deleteFailure, name='failuredelete'),
    path('failureupdate/<int:idR>', views.updateFailure, name='failureupdate'),
    
    path('groupdisplay', views.displayGroup, name='groupdisplay'),
    path('groupregister', views.resgisteGrup, name='groupregister'),
    path('groupdelete/<int:idR>', views.deleteGroup, name='groupdelete'),
    path('groupupdate/<int:idR>', views.updateGroup, name='groupupdate'),
    
    path('groupalertdisplay', views.displayGroupAlert, name='groupalertdisplay'),
    path('groupalertregister', views.resgisteGrupAlert, name='groupalertregister'),
    path('groupalertdelete/<int:idR>', views.deleteGroupAlert, name='groupalertdelete'),
    path('groupalertupdate/<int:idR>', views.updateGroupAlert, name='groupalertupdate'),
]


    # path('user/update/<int:idR>', views.update, name='userupdate'),
    # path('user/delete/<int:idR>', views.delete, name='userdelete'),