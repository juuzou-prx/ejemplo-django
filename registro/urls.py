from django.urls import path, include
from . import views

urlpatterns = [
    path('iniciar_sesion/', views.inciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('registro/', views.registrar_usuario, name='registro'),
]
