from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from logger.forms import LoggerCreateForm
from logger.models import Logger

# Create your views here.
# Create your views here.
@login_required(login_url='login')
def display(request):
    data = Logger.objects.all() 
    return render(request, 'logger/index.html', {'data': data})

# Create your views here.
@login_required(login_url='login')
def resgister(request):
    if request.method == 'POST':
        form = LoggerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logdisplay')  # Redirect to a user list view
    else:
        form = LoggerCreateForm()
    return render(request, 'logger/register.html', {'form': form})


# Create your views here.
@login_required(login_url='login')
def delete(request):
    pass