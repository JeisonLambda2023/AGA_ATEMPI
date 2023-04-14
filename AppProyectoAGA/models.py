from django.db import models
from  django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group
import datetime
import os


DEFAULT_IMG_USER = "user.png"

ESTADOS=(
    ("1", "Activo"),
    ("0", "Inactivo")
)

ROLES=(
    ("1", "Administrador"),
    ("0", "Operador")
)

TIPOS_PERSONA=(
    ("1", "Empleado"),
    ("2", "Proveedor"),
    ("3", "Visitante"),
    ("4", "Contratista")
)

class PuntoAcceso(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    estado = models.CharField(max_length=5, choices=ESTADOS, default=1)
    borrado = models.BooleanField(null=True, blank=True, default=False)
    
    
    def __str__(self):
        return self.nombre.upper()

class UsuarioManager(BaseUserManager):
    def create_user(self,documento,nombre,rol,estado,borrado,password=None):
        usuario = self.model(
            documento =documento,
            nombre = nombre,
            rol = rol,
            estado = estado,
            borrado = borrado,
            )
        usuario.set_password(password)
        usuario.save()
        return usuario

      
    def create_superuser(self,documento,nombre,rol,estado,borrado,password=None):    
        usuario = self.model(
            documento =documento,
            nombre = nombre,
            rol = rol,
            estado = estado,
            borrado = borrado,
            )
        usuario.set_password(password)
        usuario.administrador = True
        usuario.save()
        return usuario
    
    


class Usuario(AbstractBaseUser):
    documento = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=50, unique=True)
    # rol = models.ForeignKey(Group, on_delete=models.PROTECT,blank=True, null=True)
    rol = models.CharField(max_length=5, choices=ROLES, default=1)
    estado = models.CharField(max_length=5, choices=ESTADOS, default=1)
    borrado = models.BooleanField(null=True, blank=True, default=False)
    administrador = models.BooleanField(default=False)  
    objects = UsuarioManager()


    USERNAME_FIELD='nombre' 
    REQUIRED_FIELDS=["documento", "rol", "estado", "borrado","password"]

    class Meta:
        db_table = "usuarios"

    def __str__(self):
        return self.nombre.capitalize()
    

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.administrador
    

class Empresa(models.Model):
    nit = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=200)
    area_servicio = models.CharField(max_length=200)
    fecha_inicio_actividad = models.DateField(default=datetime.date.today)
    fecha_fin_actividad = models.DateField(default=datetime.date.today)
    estado = models.CharField(max_length=5, choices=ESTADOS, default=1)
    borrado = models.BooleanField(null=True, blank=True, default=False)
    
    def __str__(self):
        return self.razon_social.upper()
    
    
def extension(file):
        name, extension = os.path.splitext(file)
        return extension
    
def guardar_imagen(instance, filename):
    return  f"Fotos_personal/{instance.nombre_completo}_{instance.documento}/imagen{extension(filename)}"

class Personal(models.Model):
    documento = models.CharField(max_length=100)
    nombre_completo = models.CharField(max_length=200)
    portal_autorizado = models.ForeignKey(PuntoAcceso, on_delete=models.SET_NULL, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    fecha_inicio_actividad = models.DateField(default=datetime.date.today)
    fecha_fin_actividad = models.DateField(default=datetime.date.today)
    observaciones = models.TextField(max_length=300, null=True, blank=True)
    tipo_persona = models.CharField(max_length=5,choices=TIPOS_PERSONA, null=False, blank=False)
    foto = models.ImageField("Imagen del personal", upload_to=guardar_imagen,blank=True, null=True, default=DEFAULT_IMG_USER)
    estado = models.CharField(max_length=5, choices=ESTADOS, default=1)
    borrado = models.BooleanField(null=True, blank=True, default=False)
 
    def __str__(self):
        return self.nombre_completo.upper()