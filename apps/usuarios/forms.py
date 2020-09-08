from django.db import models
from .models import Perfil

class CustomUserForm(forms.ModelForm): 
    
    class Meta:
		model = Perfil
		fields = '__all__'