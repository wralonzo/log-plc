from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PermissionForm, UserForm

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

@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User created successfully!')
            return redirect('display-user')  # Redirect to a user list view
    else:
        form = UserForm()
    return render(request, 'user/register.html', {'form': form})