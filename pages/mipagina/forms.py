from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPers

#cracion del usuario personalizado
class UsuarioPersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPers
        fields = UserCreationForm.Meta.fields + ('edad','telefono','email','genero',)

#cambio de usuarios personalizado
class UsuarioPersChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioPers 
        fields = UserChangeForm.Meta.fields