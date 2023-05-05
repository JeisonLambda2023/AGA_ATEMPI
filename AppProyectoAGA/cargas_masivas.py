import pandas as pd
import os
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import sys
import pandas as pd
from django.db import transaction
import xlsxwriter
from io import BytesIO
from django.shortcuts import render

BASE_DIR = settings.BASE_DIR

#Puntos de acceso
def validar_portal(item): 
    if  item["nombre"] == "nan" or item["nombre"] == None or item["nombre"]=="": 
        raise Exception({"nombre":"La columna 'nombre' esta vacia"})
    if  item["latitud"] == "nan" or item["latitud"] == None or item["latitud"]=="": 
        raise Exception({"latitud":"La columna 'latitud' esta vacia"}) 
    if  item["longitud"] == "nan" or item["longitud"] == None or item["longitud"]=="": 
        raise Exception({"longitud":"La columna 'longitud' esta vacia"}) 
    return True

def formatoPortales(request):
        excel = pd.DataFrame()
        excel['Nombre'] = ""
        excel['Latitud'] = ""
        excel['Longitud'] = ""
        excel['Estado'] = ""
        
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            excel.to_excel(writer, sheet_name='Puntos de Acceso a importar', index=False)
            writer.save()
            filename = "Importar_PuntosDeAcceso_AGA"
            content_type = 'application/vnd.ms-excel'
            response = HttpResponse(b.getvalue(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
            return response
        
def importarPortales(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo_excel']
        datos_excel = pd.read_excel(archivo)
        with transaction.atomic():
            for index, row in datos_excel.iterrows():
                try: 
                    data = { 
                            "nombre":row["Nombre"], 
                            "latitud":row["Latitud"], 
                            "longitud":row["Longitud"],
                            "estado":row["Estado"]
                            }
                except Exception as e: 
                    raise Exception("El formato del Excel es incorrecto, por favor verifique la columna: ", str(e)) 
                try:
                    validacion = validar_portal(data) 
                
                    if validacion == True: 
                        formPortal = PuntoAcceso.objects.create(
                            nombre=data["nombre"], 
                            latitud=data["latitud"], 
                            longitud=data["longitud"],
                            estado=data["estado"]
                            ) 
                    else: 
                        print("validaciones desde el excel: ",validacion)
                except Exception as e:
                    return JsonResponse({"error": str(e)}, status=400)
        return JsonResponse({"error": "Importación exitosa"}, status=200)
    

#Empresas
def validar_empresas(item): 
    if  item["nit"] == "nan" or item["nit"] == None or item["nit"]=="": 
        raise Exception({"nit":"La columna 'Nit' esta vacia"})
    if  item["razon_social"] == "nan" or item["razon_social"] == None or item["razon_social"]=="": 
        raise Exception({"razon_social":"La columna 'Razón social' esta vacia"}) 
    if  item["area_servicio"] == "nan" or item["area_servicio"] == None or item["area_servicio"]=="": 
        raise Exception({"area_servicio":"La columna 'Área de servicios' esta vacia"}) 
    if  item["fecha_inicio_actividad"] == "nan" or item["fecha_inicio_actividad"] == None or item["fecha_inicio_actividad"]=="": 
        raise Exception({"fecha_inicio_actividad":"La columna 'Fecha inicio de actividades' esta vacia"}) 
    if  item["fecha_fin_actividad"] == "nan" or item["fecha_fin_actividad"] == None or item["fecha_fin_actividad"]=="": 
        raise Exception({"fecha_fin_actividad":"La columna 'Fecha fin de actividades' esta vacia"}) 
    return True

def formatoEmpresas(request):
        excel = pd.DataFrame()
        excel['Nit'] = ""
        excel['Razón social'] = ""
        excel['Área de servicios'] = ""
        excel['Fecha inicio de actividades'] = ""
        excel['Fecha fin de actividades'] = ""
        excel['Estado'] = ""
        
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            excel.to_excel(writer, sheet_name='Empresas a importar', index=False)
            writer.save()
            filename = "Importar_Empresas_AGA"
            content_type = 'application/vnd.ms-excel'
            response = HttpResponse(b.getvalue(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
            return response
        
def importarEmpresas(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo_excel']
        datos_excel = pd.read_excel(archivo)
        with transaction.atomic():
            for index, row in datos_excel.iterrows():
                try: 
                    data = { 
                            "nit":row["Nit"], 
                            "razon_social":row["Razón social"], 
                            "area_servicio":row["Área de servicios"],
                            "fecha_inicio_actividad":row["Fecha inicio de actividades"],
                            "fecha_fin_actividad":row["Fecha fin de actividades"],
                            "estado":row["Estado"]
                            }
                except Exception as e: 
                    raise Exception("El formato del Excel es incorrecto, por favor verifique la columna: ", str(e)) 
                try:
                    validacion = validar_empresas(data) 
                
                    if validacion == True: 
                        formEmpresa = Empresa.objects.create(
                            nit=data["nit"], 
                            razon_social=data["razon_social"], 
                            area_servicio=data["area_servicio"],
                            fecha_inicio_actividad=data["fecha_inicio_actividad"], 
                            fecha_fin_actividad=data["fecha_fin_actividad"], 
                            estado=data["estado"]
                            ) 
                    else: 
                        print("validaciones desde el excel: ",validacion)
                except Exception as e:
                    return JsonResponse({"error": str(e)}, status=400)
        return JsonResponse({"error": "Importación exitosa"}, status=200)
    
#Personal
def validar_personal(item): 
    if  item["documento"] == "nan" or item["documento"] == None or item["documento"]=="": 
        raise Exception({"documento":"La columna 'Documento' esta vacia"})
    if  item["nombre_completo"] == "nan" or item["nombre_completo"] == None or item["nombre_completo"]=="": 
        raise Exception({"nombre_completo":"La columna 'Nombre completo' esta vacia"}) 
    if  item["tipo_persona"] == "nan" or item["tipo_persona"] == None or item["tipo_persona"]=="": 
        raise Exception({"tipo_persona":"La columna 'Tipo de personal' esta vacia"}) 
    if  item["empresa"] == "nan" or item["empresa"] == None or item["empresa"]=="": 
        raise Exception({"empresa":"La columna 'Empresa' esta vacia"}) 
    if  item["portal"] == "nan" or item["portal"] == None or item["portal"]=="": 
        raise Exception({"portal":"La columna 'Punto de acceso' esta vacia"}) 
    if  item["fecha_inicio_actividad"] == "nan" or item["fecha_inicio_actividad"] == None or item["fecha_inicio_actividad"]=="": 
        raise Exception({"fecha_inicio_actividad":"La columna 'Fecha inicio de actividades' esta vacia"}) 
    if  item["fecha_fin_actividad"] == "nan" or item["fecha_fin_actividad"] == None or item["fecha_fin_actividad"]=="": 
        raise Exception({"fecha_fin_actividad":"La columna 'Fecha fin de actividades' esta vacia"})
    return True

def formatoPersonal(request):
    excel = pd.DataFrame()
    excel['Documento'] = ""
    excel['Nombre completo'] = ""
    excel['Tipo de personal'] = ""
    excel['Nit Empresa'] = ""
    excel['Punto de acceso'] = ""
    excel['Fecha inicio de actividades'] = ""
    excel['Fecha fin de actividades'] = ""
    excel['Observaciones'] = ""
    excel['Estado'] = ""
        
    empresas = Empresa.objects.filter(borrado=False)
    Nit,Razon_social,Area_servicio,Fecha_inicio_actividad,Fecha_fin_actividad,Estado=[[],[],[],[],[],[]]
    for i in empresas:
        Nit.append(i.nit)
        Razon_social.append(i.razon_social)
        Area_servicio.append(i.area_servicio)
        Fecha_inicio_actividad.append(i.fecha_inicio_actividad)
        Fecha_fin_actividad.append(i.fecha_fin_actividad)
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
            
        excel2 = pd.DataFrame()
        excel2['Nit'] = Nit
        excel2['Razón social'] = Razon_social
        excel2['Area de servicio'] = Area_servicio
        excel2['Fecha inicio actividad'] = Fecha_inicio_actividad
        excel2['Fecha fin actividad'] = Fecha_fin_actividad
        excel2['Estado'] = Estado
        
    portales = PuntoAcceso.objects.filter(borrado=False)
    IdP,Nombre,Latitud,Longitud,Estado=[[],[],[],[],[]]
    for i in portales:
        IdP.append(i.pk)
        Nombre.append(i.nombre)
        Latitud.append(i.latitud)
        Longitud.append(i.longitud)
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
            
        excel3 = pd.DataFrame()
        excel3['ID'] = IdP
        excel3['Nombre'] = Nombre
        excel3['Latitud'] = Latitud
        excel3['Longitud'] = Longitud
        excel3['Estado'] = Estado
        
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        excel.to_excel(writer, sheet_name='Personal a importar', index=False)
        excel2.to_excel(writer, sheet_name='Empresas', index=False)
        excel3.to_excel(writer, sheet_name='Puntos de acceso', index=False)
        writer.save()
        filename = "Importar_Personal_AGA"
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
        return response
        
def importarPersonal(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo_excel']
        datos_excel = pd.read_excel(archivo)
        with transaction.atomic():
            for index, row in datos_excel.iterrows():
                try: 
                    data = { 
                            "documento":row["Documento"], 
                            "nombre_completo":row["Nombre completo"], 
                            "tipo_persona":row["Tipo de personal"],
                            "empresa":row["Nit Empresa"],
                            "portal":row["Punto de acceso"],
                            "fecha_inicio_actividad":row["Fecha inicio de actividades"],
                            "fecha_fin_actividad":row["Fecha fin de actividades"],
                            "observaciones":row["Observaciones"],
                            "estado":row["Estado"]
                            }
                    
                except Exception as e: 
                    raise Exception("El formato del Excel es incorrecto, por favor verifique la columna: ", str(e)) 
                try:
                    validacion = validar_personal(data) 
                
                    if validacion == True: 
                        empresa = Empresa.objects.get(nit=data["empresa"])
                        portal = PuntoAcceso.objects.get(pk=data["portal"])
                        formPersonal = Personal.objects.create(
                            documento=data["documento"], 
                            nombre_completo=data["nombre_completo"], 
                            tipo_persona=data["tipo_persona"],
                            empresa=empresa, 
                            portal_autorizado=portal,  
                            fecha_inicio_actividad=data["fecha_inicio_actividad"], 
                            fecha_fin_actividad=data["fecha_fin_actividad"], 
                            observaciones=data["observaciones"],
                            estado=data["estado"]
                            ) 
                    else: 
                        print("validaciones desde el excel: ",validacion)
                except Exception as e:
                    print(e)
                    return JsonResponse({"error": str(e)}, status=400)
        return JsonResponse({"error": "Importación exitosa"}, status=200)

#Vehiculos
def validar_vehiculo(item): 
    if  item["placa"] == "nan" or item["placa"] == None or item["placa"]=="": 
        raise Exception({"placa":"La columna 'Placa' esta vacia"})
    if  item["marca"] == "nan" or item["marca"] == None or item["marca"]=="": 
        raise Exception({"marca":"La columna 'Marca' esta vacia"}) 
    if  item["modelo"] == "nan" or item["modelo"] == None or item["modelo"]=="": 
        raise Exception({"modelo":"La columna 'Modelo' esta vacia"})
    if  item["tipo_vehiculo"] == "nan" or item["tipo_vehiculo"] == None or item["tipo_vehiculo"]=="": 
        raise Exception({"tipo_vehiculo":"La columna 'Tipo de Vehiculo' esta vacia"}) 
    if  item["empresa"] == "nan" or item["empresa"] == None or item["empresa"]=="": 
        raise Exception({"empresa":"La columna 'Nit Empresa' esta vacia"}) 
    if  item["color"] == "nan" or item["color"] == None or item["color"]=="": 
        raise Exception({"color":"La columna 'Color' esta vacia"}) 
    if  item["fecha_inicio_actividad"] == "nan" or item["fecha_inicio_actividad"] == None or item["fecha_inicio_actividad"]=="": 
        raise Exception({"fecha_inicio_actividad":"La columna 'Fecha inicio de actividades' esta vacia"}) 
    if  item["fecha_fin_actividad"] == "nan" or item["fecha_fin_actividad"] == None or item["fecha_fin_actividad"]=="": 
        raise Exception({"fecha_fin_actividad":"La columna 'Fecha fin de actividades' esta vacia"})
    return True

def formatoVehiculos(request):
    excel = pd.DataFrame()
    excel['Placa'] = ""
    excel['Marca'] = ""
    excel['Modelo'] = ""
    excel['Color'] = ""
    excel['Tipo de Vehiculo'] = ""
    excel['Nit Empresa'] = ""
    excel['Fecha inicio de actividades'] = ""
    excel['Fecha fin de actividades'] = ""
    excel['Observaciones'] = ""
    excel['Estado'] = ""
        
    empresas = Empresa.objects.filter(borrado=False)
    Nit,Razon_social,Area_servicio,Fecha_inicio_actividad,Fecha_fin_actividad,Estado=[[],[],[],[],[],[]]
    for i in empresas:
        Nit.append(i.nit)
        Razon_social.append(i.razon_social)
        Area_servicio.append(i.area_servicio)
        Fecha_inicio_actividad.append(i.fecha_inicio_actividad)
        Fecha_fin_actividad.append(i.fecha_fin_actividad)
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
            
        excel2 = pd.DataFrame()
        excel2['Nit'] = Nit
        excel2['Razón social'] = Razon_social
        excel2['Area de servicio'] = Area_servicio
        excel2['Fecha inicio actividad'] = Fecha_inicio_actividad
        excel2['Fecha fin actividad'] = Fecha_fin_actividad
        excel2['Estado'] = Estado
        
    
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        excel.to_excel(writer, sheet_name='Vehiculos a importar', index=False)
        excel2.to_excel(writer, sheet_name='Empresas', index=False)
        writer.save()
        filename = "Importar_Vehiculos_AGA"
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
        return response
        
def importarVehiculos(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo_excel']
        datos_excel = pd.read_excel(archivo)
        with transaction.atomic():
            for index, row in datos_excel.iterrows():
                try: 
                    data = { 
                            "placa":row["Placa"], 
                            "marca":row["Marca"], 
                            "modelo":row["Modelo"], 
                            "color":row["Color"], 
                            "tipo_vehiculo":row["Tipo de Vehiculo"],
                            "empresa":row["Nit Empresa"],
                            "fecha_inicio_actividad":row["Fecha inicio de actividades"],
                            "fecha_fin_actividad":row["Fecha fin de actividades"],
                            "observaciones":row["Observaciones"],
                            "estado":row["Estado"]
                            }
                    
                except Exception as e: 
                    raise Exception("El formato del Excel es incorrecto, por favor verifique la columna: ", str(e)) 
                try:
                    validacion = validar_vehiculo(data) 
                
                    if validacion == True: 
                        empresa = Empresa.objects.get(nit=data["empresa"])
                        formVehiculo = Vehiculo.objects.create(
                            placa=data["placa"], 
                            marca=data["marca"], 
                            modelo=data["modelo"], 
                            color=data["color"], 
                            tipo_vehiculo=data["tipo_vehiculo"],
                            empresa=empresa, 
                            fecha_inicio_actividad=data["fecha_inicio_actividad"], 
                            fecha_fin_actividad=data["fecha_fin_actividad"], 
                            observaciones=data["observaciones"],
                            estado=data["estado"]
                            ) 
                    else: 
                        print("validaciones desde el excel: ",validacion)
                except Exception as e:
                    print(e)
                    return JsonResponse({"error": str(e)}, status=400)
        return JsonResponse({"error": "Importación exitosa"}, status=200)
