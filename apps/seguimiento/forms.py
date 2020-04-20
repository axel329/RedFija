from django import forms
from .models import Tipo_seguimiento, Seguimiento

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo_seguimiento
        fields = ['tipo']
        labels = {

            'tipo': 'Tipo de Seguimiento',
        }
        widgets = {
            'tipo': forms.TextInput(
                attrs = {

                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo'
            
                }
                
                )
        }


class PqrForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ('numero_seguimiento', 'cedula', 'nombre', 'telefono',
                 'direccion', 'departamento', 'ciudad', 'descripcion',
                  'fecha_apertura', 'estado_siebel', 'grupo', 'tipo_seguimiento'
                )
        labels = {

                    'numero_seguimiento': 'No. Incidente',
                    'cedula': 'Cedula',
                    'nombre': 'Nombre',
                    'telefono': 'Telefono ',
                    'direccion': 'Dirección ',
                    'departamento': 'Dpto',
                    'ciudad': 'Ciudad ',
                    'descripcion': 'Descripción',
                    'fecha_apertura': 'Fecha de apertura',
                    'estado_siebel': 'Estado en siebel',
                    'grupo': 'Grupo',
                    'tipo_seguimiento': 'Tipos de Seguimiento',
                }
        widgets = {

            'numero_seguimiento' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Numero de seguimiento '
                }
            ),


            'cedula' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese cedula '
                }
            ),

             'nombre' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre '
                }
            ),

             'telefono' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Telefono '
                }
            ),

             'direccion' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Dirección '
                }
            ),
             'departamento' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese deparatamento '
                }
            ),

             'ciudad' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Ciudad '
                }
            ),

             'descripcion' : forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Descripción '
                }
            ),

            'tipo_seguimiento': forms.SelectMultiple(

                attrs={

                    'class': 'form-control'
                }
            ),

            'fecha_apertura' : forms.SelectDateWidget(
                attrs={

                    'class': 'form-control'
                }
            )

        }

        