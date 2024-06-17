from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', "img"]



    nombre = forms.CharField(
         widget=forms.TextInput(attrs={'class': 'form-control'})
    )

        
    img = forms.ImageField(
            widget=forms.FileInput(attrs={'class': 'form-control'})
        )
