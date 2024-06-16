from django import forms
from .models import Producto, Categoria


class NuevoProducto(forms.ModelForm):
    
    
    class Meta:
        model = Producto
        fields = ["nombre", "desc", "precio","categoria", "img"]

    img = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )


    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    desc = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    precio = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
  