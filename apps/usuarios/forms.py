from django.db import models
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm): 
    pass
