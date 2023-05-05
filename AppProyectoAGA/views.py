from django.shortcuts import render
from django.http import JsonResponse
from AppProyectoAGA.models import *
from django.contrib.auth.views import LoginView
from .forms import  *
from django.shortcuts import  redirect
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
import pandas as pd
import xlsxwriter
from django.db.models import Count 
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay
from io import BytesIO
from django.contrib.sessions.backends.db import SessionStore


#Inicio de sesión
class Login(LoginView):
    template_name = "AppProyectoAGA/Login.html"
    form_class = LoginForm
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.rol == "1":
                return redirect("Inicio")
            else:
                return redirect("Accesos")
        return render(request, self.template_name, {"form": self.form_class,"puntosAcceso":PuntoAcceso.objects.filter(estado='1').filter(borrado=False)})
    
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
                        request.session['puntoAcesso_usuario'] = request.POST.get("access")
                        if 'next' in request.GET:
                            return redirect(request.GET.get('next'))
                        else:
                            if request.user.rol == "1":
                                return redirect("Inicio")
                            else:
                                return redirect("Accesos")
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


#Página principal del aplicativo
class inicio(View):
    def get(self, request, *args, **kwargs):
        fechaActual = datetime.now()
        ingAÑO = Acceso.objects.annotate(anio=ExtractYear('fecha_ingreso')).filter(anio=int(fechaActual.year)).count()
        ingMES = Acceso.objects.annotate(mes=ExtractMonth('fecha_ingreso')).filter(mes=int(fechaActual.month)).count()
        ingDIA = Acceso.objects.annotate(dia=ExtractDay('fecha_ingreso')).filter(dia=int(fechaActual.day)).count()
        ingVAÑO = Acceso.objects.annotate(anio2=ExtractYear('fecha_ingreso')).filter(anio2=int(fechaActual.year), ingreso="2").count()
        agrupados = Acceso.objects.filter(fecha_ingreso__year=datetime.now().year).values('personal__tipo_persona').annotate(total=Count('id'))
        agrupados = list(agrupados); total1="";total2="";total3="";total4="";
        try:
            if agrupados[0]['personal__tipo_persona'] != None:
                total1=agrupados[0]['total']
        except:
            total1=0
        try:
            if agrupados[1]['personal__tipo_persona'] != None:
                total2=agrupados[1]['total']
        except:
            total2=0
        try:
            if agrupados[4]['personal__tipo_persona'] != None:
                total3=agrupados[4]['total']
        except:
            total3=0
        try:
            if agrupados[3]['personal__tipo_persona'] != None:
                total4=agrupados[3]['total']
        except:
            total4=0
        contexto={'ingAÑO': ingAÑO, "ingMES":ingMES, "ingDIA":ingDIA, "ingVAÑO":ingVAÑO, "agrupados": agrupados, "total1":total1, "total2":total2, "total3":total3, "total4":total4}
        return render(request, "AppProyectoAGA/Inicio.html", contexto)


#Módulo de accesos
class accesos(View):
    def get(self, request, *args, **kwargs):
        if request.user.rol == "1":
            accesos = Acceso.objects.filter(estado="1")
            personal = Personal.objects.filter(borrado=False, estado="1")
            vehiculos = Vehiculo.objects.filter(borrado=False, estado="1")
            contexto={'accesos': accesos, "form":AccesosForm(), "personal": personal, "vehiculos": vehiculos}
            return render(request, "AppProyectoAGA/Accesos.html", contexto)
        else:
            accesos = Acceso.objects.filter(estado="1").filter(portal=request.session['puntoAcesso_usuario'])
            personal = Personal.objects.filter(borrado=False, estado="1")
            vehiculos = Vehiculo.objects.filter(borrado=False, estado="1")
            contexto={'accesos': accesos, "form":AccesosForm(), "personal": personal, "vehiculos": vehiculos}
            return render(request, "AppProyectoAGA/Accesos.html", contexto)
    def post(self, request, *args, **kwargs):
        ingreso = request.POST.get("ingreso")
        doc = request.POST.get("doc")
        if not ingreso:
            return JsonResponse({"errores":"No se especifico quien ingresa"}, status=400)
        if not doc:
            return JsonResponse({"errores":"No se especifico el documento"}, status=400)
        
        if ingreso == "1":
            try:
                personal = Personal.objects.get(documento=doc)
                if personal.estado == "1":
                    url = reverse_lazy("verInfoAccesoPersonal", kwargs={"pk":personal.pk})
                    return JsonResponse({"response":url}, status=200)
                else:
                    return JsonResponse({"errores":"El personal no está activo"}, status=400)
            except:
                return JsonResponse({"errores":"No se encontró el personal"}, status=400)
        else:
            try:
                vehiculo = Vehiculo.objects.get(placa=doc)
                if vehiculo.estado == "1":
                    url = reverse_lazy("verInfoAccesoVehiculo", kwargs={"pk":vehiculo.pk})
                    return JsonResponse({"response":url}, status=200)
                else:
                    return JsonResponse({"errores":"El vehiculo no está activo"}, status=400)
            except:
                return JsonResponse({"errores":"No se encontró el vehiculo"}, status=400)

class InfoAccesoPersonal(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AppProyectoAGA/Accesos/validacion.html", {"personal":Personal.objects.get(pk=kwargs["pk"])})
    
class InfoAccesoVehiculo(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AppProyectoAGA/Accesos/validacion2.html", {"vehiculo":Vehiculo.objects.get(pk=kwargs["pk"])})
        
class registrarAcceso(View):
    model = Acceso
    form_class = AccesosForm
    template_name = "AppProyectoAGA/Accesos.html"
    success_url = reverse_lazy("Accesos")
    
    def post(self, request, *args, **kwargs):
        ingreso = request.POST.get("ingreso")
        portal = PuntoAcceso.objects.get(pk=request.POST.get("portal"))
        if(ingreso == "1"):
            personal = Personal.objects.get(pk=request.POST.get("personal"))
            ultimoPersonal = Acceso.objects.filter(personal=personal)
            if(not ultimoPersonal):
                Acceso.objects.create(ingreso=ingreso, personal=personal, portal=portal)
            else:
                ultimoPersonalReg=ultimoPersonal.last()
                if(ultimoPersonalReg.tipo == "2"):
                    Acceso.objects.create(ingreso=ingreso, personal=personal, portal=portal)
                else:
                    ultimoPersonalReg.fecha_salida = datetime.now()
                    ultimoPersonalReg.tipo = "2"
                    ultimoPersonalReg.save()
        else:
            vehiculo = Vehiculo.objects.get(pk=request.POST.get("vehiculo"))
            ultimoVehiculo = Acceso.objects.filter(vehiculo=vehiculo)
            if(not ultimoVehiculo):
                Acceso.objects.create(ingreso=ingreso, vehiculo=vehiculo, portal=portal)
            else:
                ultimoVehiculoReg=ultimoVehiculo.last()
                if(ultimoVehiculoReg.tipo == "2"):
                    Acceso.objects.create(ingreso=ingreso, vehiculo=vehiculo, portal=portal)
                else:
                    ultimoVehiculoReg.fecha_salida = datetime.now()
                    ultimoVehiculoReg.tipo = "2"
                    ultimoVehiculoReg.save()
        return JsonResponse({"status":"OK"}, status=200)
 
    

#Módulo de usuarios
class usuarios(View):
    def get(self, request, *args, **kwargs):
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


#Módulo de personal
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


#Módulo de portales
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
        

#Módulo de empresas
class empresas(View):
    def get(self, request, *args, **kwargs):
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
    
    def form_valid(self, form):
        self.object = form.save()
        estado = self.object.estado
        Personal.objects.filter(empresa=self.object.pk).update(estado=estado)
        Vehiculo.objects.filter(empresa=self.object.pk).update(estado=estado)
        
        return super().form_valid(form)
    
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
            Personal.objects.filter(empresa=empresa.pk).update(borrado=empresa.borrado)
            Vehiculo.objects.filter(empresa=empresa.pk).update(borrado=empresa.borrado)
            return JsonResponse({"estado":True}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)


#Módulo de permisos
class permisos(View):
    def get(self, request, *args, **kwargs):
        personal = Personal.objects.filter(borrado=False, estado="1")
        permisos = Permiso.objects.filter(borrado=False, estado="1")
        contexto={'permisos': permisos, "form":PermisosForm(), "personal": personal}
        return render(request, "AppProyectoAGA/Permisos.html", contexto)
    def post(self, request, *args, **kwargs):
        ingreso = request.POST.get("ingreso")
        doc = request.POST.get("doc")
        if not ingreso:
            return JsonResponse({"errores":"No se especifico quien ingresa"}, status=400)
        if not doc:
            return JsonResponse({"errores":"No se especifico el documento"}, status=400)
        
        if ingreso == "1":
            try:
                personal = Personal.objects.get(documento=doc)
                if personal.estado == "1":
                    url = reverse_lazy("verInfoAccesoPersonal", kwargs={"pk":personal.pk})
                    return JsonResponse({"response":url}, status=200)
                else:
                    return JsonResponse({"errores":"El personal no está activo"}, status=400)
            except:
                return JsonResponse({"errores":"No se encontró el personal"}, status=400)
        else:
            try:
                vehiculo = Vehiculo.objects.get(placa=doc)
                if vehiculo.estado == "1":
                    url = reverse_lazy("verInfoAccesoVehiculo", kwargs={"pk":vehiculo.pk})
                    return JsonResponse({"response":url}, status=200)
                else:
                    return JsonResponse({"errores":"El vehiculo no está activo"}, status=400)
            except:
                return JsonResponse({"errores":"No se encontró el vehiculo"}, status=400)   
    
    
class infoPermisoPersonal(View):
    def get(self, request, *args, **kwargs):
        contexto = {"form": PermisosForm(), "personal":Personal.objects.get(pk=kwargs["pk"])}
        return render(request, "AppProyectoAGA/Permisos/registro.html", contexto)


class crearPermiso(CreateView):
    model = Permiso
    form_class = PermisosForm
    template_name = "AppProyectoAGA/Permisos.html"
    success_url = reverse_lazy("Permisos")
    
    def form_valid(self, form):
        try:
            form.save()
            return JsonResponse({"status":"OK"}, status=200)
        except:
            errores = {"portal_autorizado":"El personal ya posee un permiso en este Punto de acceso"}
            return JsonResponse({"status":"ERROR", "errores":errores}, status=400)
    
    def form_invalid(self, form):
        print(form.errors)
        return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
    def post(self, request, *args, **kwargs):
        print(request.FILES)
        return super().post(request, *args, **kwargs)


class verInfoPermisoPersonal(View):
    def get(self, request, *args, **kwargs):
        contexto = {"form": PermisosForm(), "personal":Personal.objects.get(pk=kwargs["pk"]),
                    "permisos": Permiso.objects.filter(personal=kwargs["pk"], borrado=False)}
        return render(request, "AppProyectoAGA/Permisos/ver.html", contexto)

class modificarPermiso(UpdateView):
    model = Permiso
    form_class = PermisosForm
    template_name = "AppProyectoAGA/Permisos/modificar.html"
    success_url = reverse_lazy("Permisos")
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object(), data=request.POST)
        if form.is_valid():
            form.save()
            val = list(self.get_object().personal.permiso_set.all())
            valores=list()
            MESES = {"01": "Enero","02": "Febrero","03": "Marzo","04": "Abril","05": "Mayo","06": "Junio","07": "Julio","08": "Agosto","09": "Septiembre",10: "Octubre",11: "Noviembre",12: "Diciembre"}
            for i in val:
                if i.borrado == False:
                    fecha_inicio = datetime.strptime(str(i.fecha_inicio_actividad), "%Y-%m-%d")
                    mes1 = fecha_inicio.strftime("%m")
                    fecha_inicio = fecha_inicio.strftime("%d de " + MESES[mes1] + " de %Y")
                    fecha_fin = datetime.strptime(str(i.fecha_fin_actividad), "%Y-%m-%d")
                    mes2 = fecha_fin.strftime("%m")
                    fecha_fin = fecha_fin.strftime("%d de " + MESES[mes2] + " de %Y")
                    if(i.estado == "1"):
                        estado="Activo"
                    else:
                        estado="Inactivo"
                    valores.append({
                        "portal": i.portal_autorizado.__str__(),
                        "personal": i.personal.__str__(),
                        "fecha_inicio": fecha_inicio,
                        "fecha_fin": fecha_fin,
                        "estado": estado,
                        "botones": f"""
                            <span class="icon" style="margin: 2px;"><a onclick="modificarPermiso('{reverse("modificarPermisoPersonal", kwargs={"pk":i.pk})}')" class="btn btn-warning btn-sm"><i class="fa-solid fa-pen-to-square"></i></a><a onclick="eliminarPermiso('{reverse("eliminarPermiso", kwargs={"pk":i.pk})}')" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a></span>
                        """
                    })
            return JsonResponse({"status":"ERROR", "info":valores}, status=200)
        else:
            return JsonResponse({"status":"ERROR", "errores":form.errors}, status=400)
    
    
  
    
    
class modificarPermisoPersonal(View):
    def get(self, request, *args, **kwargs):
        permiso = Permiso.objects.get(pk=kwargs["pk"])
        contexto = {"form": PermisosForm(instance=permiso),"permiso": permiso}
        return render(request, "AppProyectoAGA/Permisos/modificar.html", contexto)    
    
class eliminarPermiso(View):
    model = Permiso
    
    def post(self, request, *args, **kwargs):
        try:
            permiso = self.model.objects.get(pk=kwargs["pk"])
            permiso.borrado = True
            permiso.save()
            val = list(permiso.personal.permiso_set.all())
            valores=list()
            MESES = {"01": "Enero","02": "Febrero","03": "Marzo","04": "Abril","05": "Mayo","06": "Junio","07": "Julio","08": "Agosto","09": "Septiembre",10: "Octubre",11: "Noviembre",12: "Diciembre"}
            for i in val:
                if i.borrado == False:
                    fecha_inicio = datetime.strptime(str(i.fecha_inicio_actividad), "%Y-%m-%d")
                    mes1 = fecha_inicio.strftime("%m")
                    fecha_inicio = fecha_inicio.strftime("%d de " + MESES[mes1] + " de %Y")
                    fecha_fin = datetime.strptime(str(i.fecha_fin_actividad), "%Y-%m-%d")
                    mes2 = fecha_fin.strftime("%m")
                    fecha_fin = fecha_fin.strftime("%d de " + MESES[mes2] + " de %Y")
                    if(i.estado == "1"):
                        estado="Activo"
                    else:
                        estado="Inactivo"
                    valores.append({
                        "portal": i.portal_autorizado.__str__(),
                        "personal": i.personal.__str__(),
                        "fecha_inicio": fecha_inicio,
                        "fecha_fin": fecha_fin,
                        "estado": estado,
                        "botones": f"""
                            <span class="icon" style="margin: 2px;"><a onclick="modificarPermiso('{reverse("modificarPermisoPersonal", kwargs={"pk":i.pk})}')" class="btn btn-warning btn-sm"><i class="fa-solid fa-pen-to-square"></i></a><a onclick="eliminarPermiso('{reverse("eliminarPermiso", kwargs={"pk":i.pk})}')" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></a></span>
                        """
                    })
            return JsonResponse({"estado":True,"info":valores}, status=200)
        except Exception as e:
            return JsonResponse({"estado":True, "error":str(e)}, status=400)


#Módulo de vehiculos
class vehiculos(View):
    def get(self, request, *args, **kwargs):
        empresas = Empresa.objects.filter(borrado=False, estado="1")
        vehiculos = Vehiculo.objects.filter(borrado=False)
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
