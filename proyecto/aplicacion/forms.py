from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings



class empresaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    nit = forms.IntegerField(required=True)

class GarantiaForm(forms.Form):
    banco = forms.CharField(label="Razón Social", max_length=50, required=True)
    contrato = forms.CharField(label="Contrato", max_length=100, required=True)
    valor = forms.DecimalField(max_digits=100, decimal_places=2, required=True)
    fecha_inicial = forms.DateField(label="Fecha Inicial (DD/MM/YYYY)",  required=True,input_formats=settings.DATE_INPUT_FORMATS)
    fecha_final = forms.DateField(label="Fecha Final", required=True,input_formats=settings.DATE_INPUT_FORMATS)

class GarantiaSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Escriba aquí'})
                  )

class ClienteSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Escriba aquí'})
                  )
class EmpresaSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Escriba aquí'})
                  )

class SucursalSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Escriba aquí'})
                  )
    
class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)