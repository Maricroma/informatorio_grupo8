from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm): 
    
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] 
