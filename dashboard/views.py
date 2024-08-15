from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def enviar_correo(asunto, mensaje, destinatarios):
    send_mail(
        asunto,
        mensaje,
        'tu_email@example.com',
        destinatarios,
        fail_silently=False,
    )

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    context = {'name': 'World'} 
    asunto = 'Alerta de correo'
    mensaje = 'Se ha realizo una accion en PLC tal'
    destinatarios = ['test@gmail.com', 'test@gmail.com', 'test@gmail.com']
    # enviar_correo(asunto, mensaje, destinatarios)
    # Pass data to the template
    return render(request, 'dashboard/home.html', context)