from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def inicio(request):
    return render(request, 'mi_app/cv.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Enviar correo
            asunto = f"Nuevo mensaje de {nombre}"
            mensaje_correo = f"Nombre: {nombre}\nCorreo: {email}\nMensaje: {mensaje}"
            destinatario = ['mangelalvarezv@hotmail.com']  # Correo de destino (puedes poner varios)

            send_mail(asunto, mensaje_correo, settings.DEFAULT_FROM_EMAIL, destinatario)

            return render(request, 'mi_app/contacto_gracias.html')
    else:
        form = ContactForm()

    return render(request, 'mi_app/contacto.html', {'form': form})

def cv(request):
    return render(request, 'mi_app/cv.html')
