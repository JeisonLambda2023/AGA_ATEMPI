from django.urls import path
from AppProyectoAGA import views, reportes, cargas_masivas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.conf import  settings
from .reportes import *

urlpatterns = [
    
    #Inicio de sesión
    path('', views.Login.as_view(), name='Login'),
    path("Logout/", LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name="Logout"),
    
    #Página principal del aplicativo
    path('Inicio/', login_required(views.inicio.as_view()), name='Inicio'),
    
    #Módulo de accesos
    path('Accesos/', login_required(views.accesos.as_view()), name='Accesos'),
    path('RegistrarAcceso/', login_required(views.registrarAcceso.as_view()), name='registrarAcceso'),
    path('VerInfoAccesoPersonal/<int:pk>', login_required(views.InfoAccesoPersonal.as_view()), name='verInfoAccesoPersonal'),
    path('VerInfoAccesoVehiculo/<int:pk>', login_required(views.InfoAccesoVehiculo.as_view()), name='verInfoAccesoVehiculo'),
    
    #Módulo de usuarios
    path('Usuarios/', login_required(views.usuarios.as_view()), name='Usuarios'),
    path('CrearUsuarios/', login_required(views.crearUsuarios.as_view()), name='crearUsuarios'),
    path('ModificarUsuarios/<int:pk>', login_required(views.modificarUsuarios.as_view()), name='modificarUsuarios'),
    path('EliminarUsuario/<int:pk>', login_required(views.eliminarUsuario.as_view()), name='eliminarUsuario'),
    
    #Módulo de personal
    path('Personal/', login_required(views.personal.as_view()), name='Personal'),
    path('CrearPersonal/', login_required(views.crearPersonal.as_view()), name='crearPersonal'),
    path('ModificarPersonal/<int:pk>', login_required(views.modificarPersonal.as_view()), name='modificarPersonal'),
    path('EliminarPersonal/<int:pk>', login_required(views.eliminarPersonal.as_view()), name='eliminarPersonal'),
    path('ExportarPersonal/', login_required(exportarPersonal), name="exportarPersonal"),
    
    #Módulo de portales
    path('Portales/', login_required(views.portales.as_view()), name='Portales'),
    path('CrearPortales/', login_required(views.crearPortales.as_view()), name='crearPortales'),
    path('ModificarPortales/<int:pk>', login_required(views.modificarPortales.as_view()), name='modificarPortales'),
    path('EliminarPotal/<int:pk>', login_required(views.eliminarPortal.as_view()), name='eliminarPortal'),
    path('ImportarPortales/', login_required(cargas_masivas.importarPortales), name='importarPortales'),
    path('ExportarPortales/', login_required(exportarPortales), name="exportarPortales"),
    path('FormatoPortales/', login_required(cargas_masivas.formatoPortales), name='formatoPortales'),
    
    #Módulo de empresas
    path('Empresas/', login_required(views.empresas.as_view()), name='Empresas'),
    path('CrearEmpresas/', login_required(views.crearEmpresas.as_view()), name='crearEmpresas'),
    path('ModificarEmpresas/<int:pk>', login_required(views.modificarEmpresas.as_view()), name='modificarEmpresas'),
    path('EliminarEmpresa/<int:pk>', login_required(views.eliminarEmpresa.as_view()), name='eliminarEmpresa'),
    path('ExportarEmpresas/', login_required(exportarEmpresas), name="exportarEmpresas"),
    path('FormatoEmpresas/', login_required(cargas_masivas.formatoEmpresas), name='formatoEmpresas'),
    path('ImportarEmpresas/', login_required(cargas_masivas.importarEmpresas), name='importarEmpresas'),
    
    #Módulo de permisos
    path('Permisos/', login_required(views.permisos.as_view()), name='Permisos'),
    path('CrearPermiso/', login_required(views.crearPermiso.as_view()), name='crearPermiso'),
    path('VerInfoPermisoPersonal/<int:pk>', login_required(views.infoPermisoPersonal.as_view()), name='verInfoPermisoPersonal'),
    path('ModificarPermiso/<int:pk>', login_required(views.modificarPermiso.as_view()), name='modificarPermiso'),
    path('VerPermisoPersonal/<int:pk>', login_required(views.verInfoPermisoPersonal.as_view()), name='verPermisosPersonal'),
    path('ModificarPermisosPersonal/<int:pk>', login_required(views.modificarPermisoPersonal.as_view()), name='modificarPermisoPersonal'),
    path('EliminarPermiso/<int:pk>', login_required(views.eliminarPermiso.as_view()), name='eliminarPermiso'),
    path('ExportarPermisos/<int:pk>', login_required(exportarPermisos), name="exportarPermisos"),
    
    #Módulo de vehiculos
    path('Vehiculos/', login_required(views.vehiculos.as_view()), name='Vehiculos'),
    path('CrearVehiculo/', login_required(views.crearVehiculo.as_view()), name='crearVehiculo'),
    path('ModificarVehiculo/<int:pk>', login_required(views.modificarVehiculo.as_view()), name='modificarVehiculo'),
    path('EliminarVehiculo/<int:pk>', login_required(views.eliminarVehiculo.as_view()), name='eliminarVehiculo'),
    path('ExportarVehiculos/', login_required(exportarVehiculos), name="exportarVehiculos"),
    
]