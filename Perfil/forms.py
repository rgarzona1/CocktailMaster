# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'foto_perfil',
            'password1',
            'password2'
        ]



class CustomLoginForm(forms.Form):
    username = forms.CharField(label="Usuario o Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Permitir email o username
        try:
            user = User.objects.get(email=username_or_email)
            username = user.username
        except User.DoesNotExist:
            username = username_or_email

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("Usuario o contraseña incorrectos.")

        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user
