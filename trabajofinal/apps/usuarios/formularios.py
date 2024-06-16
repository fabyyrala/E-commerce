from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistroUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


    #Otra forma a traves del constructor
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
        
    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

class ActualizarPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


    #Otra forma a traves del constructor
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
        
    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control'}))