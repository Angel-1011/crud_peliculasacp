from .models import peliculas 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = peliculas  
        fields = ['nombre', 'categoria', 'año', 'foto']  

        foto = forms.ImageField(required=False)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]