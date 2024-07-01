from django import forms
from .models import Artista, Genero, Pintura
from django.forms import ModelForm

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia']

        class PinturaForm(forms.ModelForm):
    
            class Meta:
                   model = Pintura
                   fields = ['titulo', 'artista', 'imagen', 'genero']

            def __init__(self, *args, **kwargs):
                  super().__init__(*args, **kwargs)
                  self.fields['genero'].queryset = Genero.objects.all()  # Define las opciones del campo 'genero' 
            class GeneroForm(forms.ModelForm):
                class Meta:
                    model = Genero
                    fields = ['genero']  # Solo incluir los campos válidos para el modelo Genero