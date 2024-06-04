from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class FormularioRegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    #Otra forma a traves del constructor
    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"
        
    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
