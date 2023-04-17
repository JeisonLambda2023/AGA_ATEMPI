from django.shortcuts import render
from django.http import JsonResponse
from AppProyectoAGA.models import *
from django.contrib.auth.views import LoginView
from .forms import  *
from django.shortcuts import  redirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.views.generic import View, ListView, CreateView, UpdateView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = "AppProyectoAGA/Login.html"
    form_class = LoginForm
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("Inicio")
        return render(request, self.template_name, {"form": self.form_class,"puntosAcceso":PuntoAcceso.objects.filter(estado='1')})
    
    def post(self, request, *args, **kwargs):
        context={"puntosAcceso":PuntoAcceso.objects.filter(estado='1')}
        
        form = LoginForm(request,data=request.POST) #con esto se le pasan los datos al formulario, inserción
        context["form"]=form
        
        if request.POST.get("access") == "None":
            context['error']="Seleccione un punto de acceso valido"
            context['puntosAcceso']:PuntoAcceso.objects.filter(estado=1)
            
            return render(request, self.template_name, context)
        else:
            context['puntosAcceso']:PuntoAcceso.objects.filter(estado=1)
            if form.is_valid():
                nombre = form.cleaned_data.get("username")
                contrasena = form.cleaned_data.get("password")
                usuario = authenticate(username=nombre, password = contrasena)
                if usuario is not None:
                    if usuario.estado == '1':
                        login(request, usuario)
                        usuario.last_login = datetime.now()
                        if 'next' in request.GET:
                            return redirect(request.GET.get('next'))
                            
                        else:
                            return redirect("Inicio")
                    else: 
                        context['error']="Este usuario se encuentra inhabilitado"
            else:
                try:
                    Usuario.objects.get(nombre=form.cleaned_data.get('username'))
                    context['error']="La contraseña es incorrecta"
        
                except:
                    context['error']="El usuario ingresado no existe"
        context['puntosAcceso']:PuntoAcceso.objects.filter(estado=1)
        return render(request, self.template_name, context)



def inicio(request):
    return render(request, "AppProyectoAGA/Inicio.html")

def accesos(request):
    return render(request, "AppProyectoAGA/Accesos.html")

def usuarios(request):
    usuarios = Usuario.objects.filter(borrado=False)
    contexto={'usuarios': usuarios, "form":UsuarioForm()}
    return render(request, "AppProyectoAGA/Usuarios.html", contexto)

class crearUsuarios(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "AppProyectoAGA/Usuarios.html"
    success_url = reverse_lazy("Usuarios")
    
    def form_valid(self, form):
        usuario = form.save()
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()
        return JsonResponse({"status":"OK"}, status=200)
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)

class modificarUsuarios(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "AppProyectoAGA/Usuarios/modificar.html"
    success_url = reverse_lazy("Usuarios")
    
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
class eliminarUsuario(View):
    model = Usuario
    
    def post(self, request, *args, **kwargs):
        try:
            usuario = self.model.objects.get(pk=kwargs["pk"])
            usuario.borrado = 1
            usuario.save()
            return JsonResponse({"estado":True}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)


class personal(View):
    def get(self, request, *args, **kwargs):
        personal = Personal.objects.filter(borrado=False)
        empresas = Empresa.objects.filter(borrado=False, estado="1")
        portales = PuntoAcceso.objects.filter(borrado=False, estado="1")
        contexto={'personal': personal, "form":PersonalForm(),'empresas': empresas,'portales': portales}
        return render(request, "AppProyectoAGA/Personal.html", contexto)
    

class crearPersonal(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = "AppProyectoAGA/Personal.html"
    success_url = reverse_lazy("Personal")
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":"OK"}, status=200)
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        return super().post(request, *args, **kwargs)

class modificarPersonal(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = "AppProyectoAGA/Personal/modificar.html"
    success_url = reverse_lazy("Personal")
    
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        return super().post(request, *args, **kwargs)
    
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
class eliminarPersonal(View):
    model = Personal
    
    def post(self, request, *args, **kwargs):
        try:
            personal = self.model.objects.get(pk=kwargs["pk"])
            personal.borrado = True
            personal.save()
            return JsonResponse({"estado":True}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)




class portales(View):
    def get(self, request, *args, **kwargs):
        puntosAcceso = PuntoAcceso.objects.filter(borrado=False)
        contexto={'puntosAcceso': puntosAcceso, "form":PuntoAccesoForm()}
        return render(request, "AppProyectoAGA/Portales.html", contexto)
    

class crearPortales(CreateView):
    model = PuntoAcceso
    form_class = PuntoAccesoForm
    template_name = "AppProyectoAGA/Portales.html"
    success_url = reverse_lazy("Portales")
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":"OK"}, status=200)
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)

class modificarPortales(UpdateView):
    model = PuntoAcceso
    form_class = PuntoAccesoForm
    template_name = "AppProyectoAGA/Portales/modificar.html"
    success_url = reverse_lazy("Portales")
    
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
class eliminarPortal(View):
    model = PuntoAcceso
    
    def post(self, request, *args, **kwargs):
        try:
            portal = self.model.objects.get(pk=kwargs["pk"])
            portal.borrado = True
            portal.save()
            return JsonResponse({"estado":True}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)

def empresas(request):
    empresas = Empresa.objects.filter(borrado=False)
    contexto={'empresas': empresas, "form":EmpresaForm()}
    return render(request, "AppProyectoAGA/Empresas.html", contexto)

class crearEmpresas(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = "AppProyectoAGA/Empresas.html"
    success_url = reverse_lazy("Empresas")
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":"OK"}, status=200)
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)

class modificarEmpresas(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = "AppProyectoAGA/Empresas/modificar.html"
    success_url = reverse_lazy("Empresas")
    
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
class eliminarEmpresa(View):
    model = Empresa
    
    def post(self, request, *args, **kwargs):
        try:
            empresa = self.model.objects.get(pk=kwargs["pk"])
            empresa.borrado = True
            empresa.save()
            return JsonResponse({"estado":True}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)

def permisos(request):
    return render(request, "AppProyectoAGA/Permisos.html")

class vehiculos(View):
    def get(self, request, *args, **kwargs):
        empresas = Empresa.objects.filter(borrado=False, estado="1")
        vehiculos = Vehiculo.objects.filter(borrado=False, estado="1")
        contexto={'vehiculos': vehiculos, "form":VehiculosForm(),'empresas': empresas}
        return render(request, "AppProyectoAGA/Vehiculos.html", contexto)
    

class crearVehiculo(CreateView):
    model = Vehiculo
    form_class = VehiculosForm
    template_name = "AppProyectoAGA/Vehiculos.html"
    success_url = reverse_lazy("Vehiculos")
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({"status":"OK"}, status=200)
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        return super().post(request, *args, **kwargs)

class modificarVehiculo(UpdateView):
    model = Vehiculo
    form_class = VehiculosForm
    template_name = "AppProyectoAGA/Vehiculos/modificar.html"
    success_url = reverse_lazy("Vehiculos")
    
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        return super().post(request, *args, **kwargs)
    
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
class eliminarVehiculo(View):
    model = Vehiculo
    
    def post(self, request, *args, **kwargs):
        try:
            personal = self.model.objects.get(pk=kwargs["pk"])
            personal.borrado = True
            personal.save()
            return JsonResponse({"estado":True}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)