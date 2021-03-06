"""BienalDigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import view
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.inicio, name='inicio'),
    path('Login/',auth.LoginView.as_view(template_name="usuarios/login.html"),name="login"),
    path('Logout/',auth.LogoutView.as_view(),name="logout"),
    path('Ciudad/', view.historia, name='historia'),
    #url de aplicaciones
    path('', include('apps.usuarios.urls')),
    path('', include('apps.votos.urls')),
    path('', include('apps.perfiles.urls')),
    path('', include('apps.contacto.urls')),
    path('', include('apps.testimoniales.urls')),
    path('', include('apps.enVivos.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Bienal Digital - Administración'
admin.site.index_title = 'Módulos de Administración'
admin.site.site_title = 'Bienal Digital'
