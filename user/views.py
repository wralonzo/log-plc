from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user.forms import EditForm, UserForm

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


@login_required(login_url='login')
def update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Optionally, add a success message
            return redirect('display-user')  # Redirect to the user's detail page
    else:
        form = EditForm(instance=user)
    
    return render(request, 'user/update.html', {'form': form})

@login_required(login_url='login')
def delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if user.delete():
            # Optionally, add a success message
        return redirect('display-user')  # Redirect to the user's detail page
    else:
        return redirect('display-user')