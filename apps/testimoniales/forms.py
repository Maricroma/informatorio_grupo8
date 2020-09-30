from django import forms
from .models import Comentario

class AltaComentario(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ['nombre','email','mensaje']