from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

    nombre = forms.CharField(
         widget=forms.TextInput(attrs={'class': 'form-control'})
    )