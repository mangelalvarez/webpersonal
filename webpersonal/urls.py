from django.contrib import admin
from django.urls import path, include
from mi_app import views  # Importa views desde mi_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # Vista de inicio desde mi_app.views
    path('mi_app/', include('mi_app.urls')),  # Incluye las URLs de mi_app
]