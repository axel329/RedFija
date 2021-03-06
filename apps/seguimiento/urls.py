from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    path('crear_tipo/', login_required(CrearTipo.as_view()), name='crear_tipo'),
    path('listar_tipo/', login_required(ListadoTipo.as_view()), name='listar_tipo'),
    path('editar_tipo/<int:pk>/', login_required(ActualizarTipo.as_view()), name='editar_tipo'),
    path('eliminar_tipo/<int:pk>/', login_required(EliminarTipo.as_view()), name='eliminar_tipo'),
    path('listar_pqr/', login_required(ListadoPqr.as_view()),name = 'listar_pqr'),
    path('crear_pqr/', login_required(CrearPqr.as_view()),name = 'crear_pqr'),
    path('editar_pqr/<int:pk>/', login_required(ActualizarPqr.as_view()),name = 'editar_pqr'),
    path('eliminar_pqr/<int:pk>/', login_required(EliminarPqr.as_view()), name='eliminar_pqr'),
   
]
