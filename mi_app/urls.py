# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('cv/', views.cv, name='cv'),      # Asegúrate de que views.inicio exista
]