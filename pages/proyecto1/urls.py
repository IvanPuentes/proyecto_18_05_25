"""proyecto_vacaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path,include
from django.contrib import admin
from mipagina.views import HomePageView,RevistaPageView,MangaPageView,Descrip_libPageView,AutoresPageView,RegistrarView,ControlView,CVView,CVPrincipalView,CVEditView,CVDeleteView,TecView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mipagina/', include('mipagina.urls')),
    path('mipagina/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('Home',HomePageView.as_view(), name='home'),
    path('Manga',MangaPageView.as_view(), name='mangas'),
    path('Revista',RevistaPageView.as_view(), name='revistas'),
    path('descrip_lib',Descrip_libPageView.as_view(), name='descrip_lib'),
    path('Autor',AutoresPageView.as_view(), name='Autores'),
    path('registrar/', RegistrarView.as_view(),name='registrar'),
    path('Control',ControlView.as_view(), name='Control'),
    path('Tec',TecView.as_view(), name='tec'),
    path('CV/',CVView.as_view(),name='CV'),
    path('CV_principal/',CVPrincipalView.as_view(),name='CV_principal'),
    path('Nombre/<int:pk>/Update',CVEditView.as_view(),name='EditCV'),
    path('Nombre/<int:pk>/delete',CVDeleteView.as_view(),name='deleteCV'),
     
]