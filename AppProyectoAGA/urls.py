from django.urls import path
from AppProyectoAGA import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.conf import  settings

urlpatterns = [
    path('', views.Login.as_view(), name='Login'),
    path('Inicio/', login_required(views.inicio), name='Inicio'),
    path('Accesos/', login_required(views.accesos), name='Accesos'),
    path('Usuarios/', login_required(views.usuarios), name='Usuarios'),
    path('CrearUsuarios/', login_required(views.crearUsuarios.as_view()), name='crearUsuarios'),
    path('ModificarUsuarios/<int:pk>', login_required(views.modificarUsuarios.as_view()), name='modificarUsuarios'),
    path('EliminarUsuario/<int:pk>', login_required(views.eliminarUsuario.as_view()), name='eliminarUsuario'),
    path('Personal/', login_required(views.personal.as_view()), name='Personal'),
    path('CrearPersonal/', login_required(views.crearPersonal.as_view()), name='crearPersonal'),
    path('ModificarPersonal/<int:pk>', login_required(views.modificarPersonal.as_view()), name='modificarPersonal'),
    path('EliminarPersonal/<int:pk>', login_required(views.eliminarPersonal.as_view()), name='eliminarPersonal'),
    path('Portales/', login_required(views.portales.as_view()), name='Portales'),
    path('CrearPortales/', login_required(views.crearPortales.as_view()), name='crearPortales'),
    path('ModificarPortales/<int:pk>', login_required(views.modificarPortales.as_view()), name='modificarPortales'),
    path('EliminarPotal/<int:pk>', login_required(views.eliminarPortal.as_view()), name='eliminarPortal'),
    path('Empresas/', login_required(views.empresas), name='Empresas'),
    path('CrearEmpresas/', login_required(views.crearEmpresas.as_view()), name='crearEmpresas'),
    path('ModificarEmpresas/<int:pk>', login_required(views.modificarEmpresas.as_view()), name='modificarEmpresas'),
    path('EliminarEmpresa/<int:pk>', login_required(views.eliminarEmpresa.as_view()), name='eliminarEmpresa'),
    path('Permisos/', login_required(views.permisos), name='Permisos'),
    path('Vehiculos/', login_required(views.vehiculos.as_view()), name='Vehiculos'),
    path('CrearVehiculo/', login_required(views.crearVehiculo.as_view()), name='crearVehiculo'),
    path('ModificarVehiculo/<int:pk>', login_required(views.modificarVehiculo.as_view()), name='modificarVehiculo'),
    path('EliminarVehiculo/<int:pk>', login_required(views.eliminarVehiculo.as_view()), name='eliminarVehiculo'),
    path("Logout/", LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name="Logout"),
]