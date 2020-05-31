from django import forms
from .models import *

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'name',
            'plaza',
            'fijo',
            'celular',
            'uo',
            'cargo',
        ]
        labels = {
            'name': 'Nombre',
            'plaza':'Plaza',
            'fijo': 'Teléfono fijo',
            'celular': 'Teléfono celular',
            'uo': 'Unidad Organizativa',
            'cargo':'Cargo',
        }
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'plaza':forms.TextInput(attrs={'class':'form-control'}),
            'fijo':forms.TextInput(attrs={'class':'form-control'}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'uo':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
        }

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'persona',
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'persona': 'Persona',
            'numero_mascotas':'Número de Mascotas',
            'razones': 'Razones',
        }
        widgets = {
            
            'persona':forms.TextInput(attrs={'class':'form-control'}),
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.TextInput(attrs={'class':'form-control'}),        
        }        