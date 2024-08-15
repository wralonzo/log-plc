from django.shortcuts import render

# Create your views here.
def dashboard(request):
    context = {'name': 'World'}  # Pass data to the template
    return render(request, 'dashboard/home.html', context)