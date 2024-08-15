from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('auth', views.authLogin, name='auth'),
     path('logout', views.logout_view, name='logout'),
]