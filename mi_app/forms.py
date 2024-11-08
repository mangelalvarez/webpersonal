from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Correo Electrónico")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")