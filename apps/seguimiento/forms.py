from django import forms
from .models import Tipo_seguimiento

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
        