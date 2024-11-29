# app_base/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para la vista 'inicio'
]
