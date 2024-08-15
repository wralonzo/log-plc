from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    context = {'name': 'World'}  # Pass data to the template
    return render(request, 'login/index.html', context)

# Create your views here.
def authLogin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
    return redirect('/') 
