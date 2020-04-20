from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,  TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import TipoForm, PqrForm
from .models import Tipo_seguimiento, Seguimiento


'''
    1. - dispatch(): valida la petición y elige que metodo HTTP se utilizo para la solicitud
    2. - http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    3. - options()
'''

# Create your views here.


class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoTipo(ListView):
    template_name = 'seguimiento/tipos/listar_tipo.html'
    context_object_name = 'tipos'
    queryset = Tipo_seguimiento.objects.filter(estado = True)

class ActualizarTipo(UpdateView):
    model = Tipo_seguimiento
    template_name = 'seguimiento/tipos/crear_tipo.html'
    form_class = TipoForm
    success_url = reverse_lazy('seguimiento:listar_tipo')

class CrearTipo(CreateView):
    model = Tipo_seguimiento
    form_class = TipoForm
    template_name = 'seguimiento/tipos/crear_tipo.html'
    success_url = reverse_lazy('seguimiento:listar_tipo')


class EliminarTipo(DeleteView):
    model = Tipo_seguimiento # para eliminación directa solo se usa esta linea y la documentada abajo
    #success_url = reverse_lazy('seguimiento:listar_tipo')
    # eliminar de forma Logica cambiando el estado se omite la linea anterior

    def post(self, request,pk, *args, **kwargs):

        object = Tipo_seguimiento.objects.get(id = pk)
        object.estado = False
        object.save()

        return redirect('seguimiento:listar_tipo')

class ListadoPqr(View):
    model = Seguimiento
    form_class = PqrForm
    context_object_name = 'seguimientos'
    template_name = 'seguimiento/proyectos/pqr/listar_pqr.html' 

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self):
        contexto = {}
        contexto['seguimientos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
       
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seguimiento:listar_pqr')


class ActualizarPqr(UpdateView):
    model = Seguimiento
    template_name = 'seguimiento/proyectos/pqr/listar_pqr.html'
    form_class = PqrForm
    success_url = reverse_lazy('seguimiento:listar_pqr')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seguimientos'] = Seguimiento.objects.filter(estado=True)
        return context

class EliminarPqr(DeleteView):
    model = Seguimiento
    def post(self, request,pk, *args, **kwargs):

        object = Seguimiento.objects.get(id = pk)
        object.estado = False
        object.save()

        return redirect('seguimiento:listar_pqr')

    
