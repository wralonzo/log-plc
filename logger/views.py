from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
# Create your views here.
@login_required(login_url='login')
def display(request):
    data = models.Logger.objects.all()  # Obtener todos los usuarios
    return render(request, 'logger/index.html', {'usuarios': data})

# Create your views here.
@login_required(login_url='login')
def resgister(request):
    pass

# Create your views here.
@login_required(login_url='login')
def delete(request):
    pass