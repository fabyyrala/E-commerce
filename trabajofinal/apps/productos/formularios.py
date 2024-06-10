from django import forms
from .models import Producto


from apps.usuarios.models import AbstractUser

class NuevoProducto(forms.ModelForm):
   
    class Meta:
        model = Producto
        fields = ["nombre", "desc", "precio"]


    #Otra forma a traves del constructor
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    desc = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    precio = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


    
