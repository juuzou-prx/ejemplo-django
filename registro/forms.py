#heredar el formulario de registro de Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        #validar que ambas contraseñas coincidan - contraseña cifrada
        fields = ['username', 'password', 'password2']