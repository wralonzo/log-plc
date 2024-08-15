from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def display(request):
    data = User.objects.all()  # Obtener todos los usuarios
    return render(request, 'user/index.html', {'usuarios': data})

# Create your views here.
@login_required(login_url='login')
def resgisteGrupAlert(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deleteGroupAlert(request):
    pass