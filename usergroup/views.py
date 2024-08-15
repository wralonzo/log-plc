from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
# Falla
@login_required(login_url='login')
def displayFailure(request):
    data = models.FailureType.objects.all()  # Obtener todos los usuarios
    return render(request, 'usergroup/failure/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgisteFailure(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deleteFailure(request):
    pass


# Create your views here.
# Falla
@login_required(login_url='login')
def displayGroup(request):
    data = models.Group.objects.all()  # Obtener todos los usuarios
    return render(request, 'usergroup/group/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgisteGrup(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deleteGroup(request):
    pass

# Create your views here.
# Falla
@login_required(login_url='login')
def displayGroupAlert(request):
    data = models.GroupEmail.objects.all()  # Obtener todos los usuarios
    return render(request, 'usergroup/groupemail/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgisteGrupAlert(request):
    pass

# Create your views here.
@login_required(login_url='login')
def deleteGroupAlert(request):
    pass