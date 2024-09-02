from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from usergroup.forms import FailureTypeCreateForm, GroupCreateForm, GroupEmailCreateForm
from . import models

# Create your views here.
# Falla
@login_required(login_url='login')
def displayFailure(request):
    data = models.FailureType.objects.all()  # Obtener todos los usuarios
    return render(request, 'groups/failure/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgisteFailure(request):
    if request.method == 'POST':
        form = FailureTypeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('failuredisplay')  # Redirect to a user list view
    else:
        form = FailureTypeCreateForm()
    return render(request, 'groups/failure/register.html', {'form': form})


# Create your views here.
@login_required(login_url='login')
def deleteFailure(request):
    pass
# Create your views here.
# Falla
@login_required(login_url='login')
def displayGroup(request):
    data = models.Group.objects.all()  # Obtener todos los usuarios
    return render(request, 'groups/group/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgisteGrup(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupdisplay')  # Redirect to a user list view
    else:
        form = GroupCreateForm()
    return render(request, 'groups/group/register.html', {'form': form})

# Create your views here.
@login_required(login_url='login')
def deleteGroup(request):
    pass

# Create your views here.
# Falla
@login_required(login_url='login')
def displayGroupAlert(request):
    data = models.GroupEmail.objects.all()  # Obtener todos los usuarios
    return render(request, 'groups/groupemail/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgisteGrupAlert(request):
    if request.method == 'POST':
        form = GroupEmailCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupalertdisplay')  # Redirect to a user list view
    else:
        form = GroupEmailCreateForm()
    return render(request, 'groups/groupemail/register.html', {'form': form})

# Create your views here.
@login_required(login_url='login')
def deleteGroupAlert(request):
    pass