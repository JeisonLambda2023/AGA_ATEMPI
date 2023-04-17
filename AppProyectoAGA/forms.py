from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import *

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label = "Nombre de Usuario",
        widget = forms.TextInput(attrs={'autofocus': True,"class":"form-control inpr","id":"inputUsuario","placeholder":"Nombre de usuario"})
    )

    password  = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Contraseña", "required":"True"})
        )
    

class PuntoAccesoForm(forms.ModelForm):
    class Meta:
        model = PuntoAcceso
        fields = ["nombre", "latitud", "longitud", "estado"]
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "latitud": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "longitud": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
        
    
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["nit", "razon_social", "area_servicio", "fecha_inicio_actividad", "fecha_fin_actividad", "estado"]
        
        widgets = {
            "nit": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "razon_social": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "area_servicio": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "fecha_inicio_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "fecha_fin_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
        

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["documento", "nombre", "rol", "estado", "password"]
        
        widgets = {
            "documento": forms.NumberInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "nombre": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "rol": forms.Select(attrs={"class":"form-select", "autocomplete":"off",}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off",'id':"password",'requerid':'requerid','name':'password'}),
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
        
        
class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ["documento", "nombre_completo", "empresa", "portal_autorizado", "observaciones", "foto", "tipo_persona", "fecha_inicio_actividad", "fecha_fin_actividad", "estado"]
        
        widgets = {
            "documento": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "nombre_completo": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "empresa": forms.Select(attrs={"class":"form-select"}),
            "portal_autorizado": forms.Select(attrs={"class":"form-select"}),
            "observaciones": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "tipo_persona": forms.Select(attrs={"class":"form-select"}),
            "fecha_inicio_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "fecha_fin_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
        
        
class VehiculosForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["placa", "marca", "modelo", "color","empresa", "observaciones", "foto", "tipo_vehiculo", "fecha_inicio_actividad", "fecha_fin_actividad", "estado"]
        
        widgets = {
            "placa": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "marca": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}),
            "modelo": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "color": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "empresa": forms.Select(attrs={"class":"form-select"}),
            "observaciones": forms.TextInput(attrs={"class":"form-control", "autocomplete":"off",}), 
            "tipo_vehiculo": forms.Select(attrs={"class":"form-select"}),
            "fecha_inicio_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "fecha_fin_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }