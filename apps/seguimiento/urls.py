from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('crear_tipo/', CrearTipo.as_view(), name='crear_tipo'),
    path('listar_tipo/', ListadoTipo.as_view(), name='listar_tipo'),
    path('editar_tipo/<int:pk>', ActualizarTipo.as_view(), name='editar_tipo'),
    path('eliminar_tipo/<int:pk>', EliminarTipo.as_view(), name='eliminar_tipo')
]
