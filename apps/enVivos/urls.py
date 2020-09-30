from django.urls import path
from .views import lista_de_videos_en_vivo



urlpatterns=[
	path('en-vivos/<int:id>', lista_de_videos_en_vivo, name="en_vivos"),

]