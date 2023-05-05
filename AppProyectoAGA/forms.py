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
        
    def clean_fecha_inicio_actividad(self):
        self.fecha_inicio_actividad=self.cleaned_data["fecha_inicio_actividad"]
        return self.fecha_inicio_actividad
        
    def clean_fecha_fin_actividad(self):
        fin = self.cleaned_data["fecha_fin_actividad"]
        if(fin < self.fecha_inicio_actividad):
            raise forms.ValidationError("La fecha de fin de actividad debe ser mayor o igual a la fecha de inicio de actividad")
        else:
            return fin
        

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
    
    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields["empresa"].queryset = Empresa.objects.filter(borrado=False).filter(estado="1")
        self.fields["portal_autorizado"].queryset = PuntoAcceso.objects.filter(borrado=False).filter(estado="1")
    
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
        
    def clean_fecha_inicio_actividad(self):
        self.fecha_inicio_actividad=self.cleaned_data["fecha_inicio_actividad"]
        return self.fecha_inicio_actividad
        
    def clean_fecha_fin_actividad(self):
        fin = self.cleaned_data["fecha_fin_actividad"]
        if(fin < self.fecha_inicio_actividad):
            raise forms.ValidationError("La fecha de fin de actividad debe ser mayor o igual a la fecha de inicio de actividad")
        else:
            return fin
            
        
        
class VehiculosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehiculosForm, self).__init__(*args, **kwargs)
        self.fields["empresa"].queryset = Empresa.objects.filter(borrado=False).filter(estado="1")
    
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
        
    def clean_fecha_inicio_actividad(self):
        self.fecha_inicio_actividad=self.cleaned_data["fecha_inicio_actividad"]
        return self.fecha_inicio_actividad
        
    def clean_fecha_fin_actividad(self):
        fin = self.cleaned_data["fecha_fin_actividad"]
        if(fin < self.fecha_inicio_actividad):
            raise forms.ValidationError("La fecha de fin de actividad debe ser mayor o igual a la fecha de inicio de actividad")
        else:
            return fin
        
        
class PermisosForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ["portal_autorizado", "personal", "fecha_inicio_actividad", "fecha_fin_actividad", "estado"]
        
        widgets = {
            "portal_autorizado": forms.Select(attrs={"class":"form-select"}),
            "personal": forms.Select(attrs={"class":"form-select"}),
            "fecha_inicio_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "fecha_fin_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
        
    def clean_fecha_inicio_actividad(self):
        self.fecha_inicio_actividad=self.cleaned_data["fecha_inicio_actividad"]
        return self.fecha_inicio_actividad
        
    def clean_fecha_fin_actividad(self):
        fin = self.cleaned_data["fecha_fin_actividad"]
        if(fin < self.fecha_inicio_actividad):
            raise forms.ValidationError("La fecha de fin de actividad debe ser mayor o igual a la fecha de inicio de actividad")
        else:
            return fin
        

class AccesosForm(forms.ModelForm):
    class Meta:
        model = Acceso
        fields = ["ingreso"]
        
        widgets = {
            "ingreso": forms.Select(attrs={"class":"form-select"})
        }
        
    