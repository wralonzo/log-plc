from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
username_validator = UnicodeUsernameValidator()

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True,
                                label="Nombres *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True,label="Apellidos *",
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(max_length=50, label='Correo electronico *',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=('Contraseña *'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=('Confirmar contraseña *'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=('Repita su contraseña'))
    
    username = forms.CharField(
        label=('Usuario *'),
        max_length=150,
        validators=[username_validator],
        error_messages={'unique': ("Ya existe el usuario.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'user_permissions')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_permissions'].label_from_instance = self.label_permission_instance

    def label_permission_instance(self, obj):
        permission_name = obj.name
        permissions_translated =[w.replace('Can', 'Puede').replace('add', 'agregar').replace('change', 'modificar').replace('delete', 'eliminar').replace('view', 'ver') for w in permission_name.split()]
        return ' '.join(permissions_translated)
    
class PermissionForm(forms.Form):
    name= forms.CharField(max_length=12, min_length=4, required=True,label="Nombre del permiso *",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rol'}))
    class Meta:
        model = Permission
        fields = ('name')
    