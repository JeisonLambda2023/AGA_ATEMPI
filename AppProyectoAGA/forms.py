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
        
    def clean_nit(self):
        self.nit=self.cleaned_data["nit"]
        if len(str(self.nit)) < 7:
            raise forms.ValidationError('Se debe ingresar un mínimo de 7 caracteres.')
        if not self.instance.nit:
            print("registrar")
            emp = Empresa.objects.filter(nit=self.nit).filter(borrado=False)
            if emp:
                raise forms.ValidationError(f"Ya existe una empresa registrada con este Nit: {self.nit}")
        else:
            print("modificar")
            emp = Empresa.objects.filter(nit=self.nit).filter(borrado=False)
            objetoActual = Empresa.objects.get(pk=self.instance.pk)
            bandera=False
            for i in emp:
                if i.nit == objetoActual.nit:
                    bandera=True
            print(bandera)
            if emp and bandera==False:
                raise forms.ValidationError(f"Ya existe una empresa registrada con este Nit: {self.nit}")
        return self.nit
        
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
        
    def clean_documento(self):
        self.documento=self.cleaned_data["documento"]
        if len(str(self.documento)) < 7:
            raise forms.ValidationError('Se debe ingresar un mínimo de 7 caracteres.')
        if not self.instance.documento:
            print("registrar")
            user = Usuario.objects.filter(documento=self.documento).filter(borrado=False)
            if user:
                raise forms.ValidationError(f"Ya existe un usuario registrado con este documento: {self.documento}")
        else:
            print("modificar")
            user = Usuario.objects.filter(documento=self.documento).filter(borrado=False)
            objetoActual = Usuario.objects.get(pk=self.instance.pk)
            bandera=False
            for i in user:
                if i.documento == objetoActual.documento:
                    bandera=True
            print(bandera)
            if user and bandera==False:
                raise forms.ValidationError(f"Ya existe un usuario registrado con este documento: {self.documento}")
        return self.documento
    
        
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
            "observaciones": forms.Textarea(attrs={"class":"form-control", "autocomplete":"off",}), 
            "tipo_persona": forms.Select(attrs={"class":"form-select"}),
            "fecha_inicio_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "fecha_fin_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
        
    def clean_documento(self):
        self.documento=self.cleaned_data["documento"]
        if len(str(self.documento)) < 7:
            raise forms.ValidationError('Se debe ingresar un mínimo de 7 caracteres.')
        if not self.instance.documento:
            print("registrar")
            per = Personal.objects.filter(documento=self.documento).filter(borrado=False)
            if per:
                raise forms.ValidationError(f"Ya existe un personal registrado con este documento: {self.documento}")
        else:
            print("modificar")
            per = Personal.objects.filter(documento=self.documento).filter(borrado=False)
            objetoActual = Personal.objects.get(pk=self.instance.pk)
            bandera=False
            for i in per:
                if i.documento == objetoActual.documento:
                    bandera=True
            print(bandera)
            if per and bandera==False:
                raise forms.ValidationError(f"Ya existe un personal registrado con este documento: {self.documento}")
        return self.documento
        
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
            "observaciones": forms.Textarea(attrs={"class":"form-control", "autocomplete":"off",}), 
            "tipo_vehiculo": forms.Select(attrs={"class":"form-select"}),
            "fecha_inicio_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "fecha_fin_actividad": forms.DateInput(attrs={"type":"date","class":"form-control", "autocomplete":"off",},format=('%Y-%m-%d')), 
            "estado": forms.Select(attrs={"class":"form-select", "autocomplete":"off",})
        }
     
    def clean_placa(self):
        self.placa=self.cleaned_data["placa"]
        if len(str(self.placa)) < 4:
            raise forms.ValidationError('Se debe ingresar un mínimo de 4 caracteres.')
        if not self.instance.placa:
            print("registrar")
            veh = Vehiculo.objects.filter(placa=self.placa).filter(borrado=False)
            if veh:
                raise forms.ValidationError(f"Ya existe un vehiculo registrado con esta placa: {self.placa}")
        else:
            print("modificar")
            veh = Vehiculo.objects.filter(placa=self.placa).filter(borrado=False)
            objetoActual = Vehiculo.objects.get(pk=self.instance.pk)
            bandera=False
            for i in veh:
                if i.placa == objetoActual.placa:
                    bandera=True
            print(bandera)
            if veh and bandera==False:
                raise forms.ValidationError(f"Ya existe un vehiculo registrado con esta placa: {self.placa}")
        return self.placa 
        
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
    def __init__(self, *args, **kwargs):
        super(PermisosForm, self).__init__(*args, **kwargs)
        self.fields["personal"].queryset = Personal.objects.filter(borrado=False).filter(estado="1")
        self.fields["portal_autorizado"].queryset = PuntoAcceso.objects.filter(borrado=False).filter(estado="1")
    
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
        
    def clean_codigo(self):
        self.codigo=self.cleaned_data["codigo"]
        if not self.instance.codigo:
            print("registrar")
            per = Permiso.objects.filter(codigo=self.codigo).filter(borrado=False)
            if per:
                raise forms.ValidationError(f"Ya existe un Permiso asignado al personal en el punto de acceso de: {self.portal_autorizado}")
        else:
            print("modificar")
            per = Permiso.objects.filter(codigo=self.codigo).filter(borrado=False)
            objetoActual = Permiso.objects.get(pk=self.instance.pk)
            bandera=False
            for i in per:
                if i.codigo == objetoActual.codigo:
                    bandera=True
            print(bandera)
            if per and bandera==False:
                raise forms.ValidationError(f"Ya existe un Permiso asignado al personal en el punto de acceso de: {self.portal_autorizado}")
        return self.codigo     
        
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
        
    