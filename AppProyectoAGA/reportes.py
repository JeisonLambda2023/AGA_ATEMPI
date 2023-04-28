import pandas as pd
import xlsxwriter
from io import BytesIO
from datetime import datetime, time
from django.views.generic import ListView, View
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.shortcuts import  redirect
from .models import *
from AppProyectoAGA.models import *

def exportarVehiculos(request):
    vehiculos = Vehiculo.objects.filter(borrado=False)
    Placa,Marca,Modelo,Color,Fecha_inicio_actividad,Fecha_fin_actividad,Observaciones,Tipo_vehiculo,Estado,Empresa=[[],[],[],[],[],[],[],[],[],[]]
    for i in vehiculos:
        Placa.append(i.placa)
        Marca.append(i.marca)
        Modelo.append(i.modelo)
        Color.append(i.color)
        Fecha_inicio_actividad.append(i.fecha_inicio_actividad)
        Fecha_fin_actividad.append(i.fecha_fin_actividad)
        Observaciones.append(i.observaciones)
        if(i.tipo_vehiculo == "1"):
            Tipo_vehiculo.append("Camión")
        elif(i.tipo_vehiculo == "2"):
            Tipo_vehiculo.append("Camioneta")
        elif(i.tipo_vehiculo == "3"):
            Tipo_vehiculo.append("Motocicleta")
        elif(i.tipo_vehiculo == "4"):
            Tipo_vehiculo.append("Volqueta")
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
        Empresa.append(i.empresa)
            
        excel = pd.DataFrame()
        excel['Placa'] = Placa
        excel['Marca'] = Marca
        excel['Modelo'] = Modelo
        excel['Color'] = Color
        excel['Empresa'] = Empresa
        excel['Fecha inicio actividad'] = Fecha_inicio_actividad
        excel['Fecha fin actividad'] = Fecha_fin_actividad
        excel['Observaciones'] = Observaciones
        excel['Tipo vehiculo'] = Tipo_vehiculo
        excel['Estado'] = Estado
        
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        excel.to_excel(writer, sheet_name='Vehiculos', index=False)
        writer.save()
        filename = "Vehiculos_AGA"
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
        return response
        

def exportarPersonal(request):
    personal = Personal.objects.filter(borrado=False)
    Documento,Nombre_completo,Fecha_inicio_actividad,Fecha_fin_actividad,Observaciones,Tipo_persona,Estado,Empresa,Portal=[[],[],[],[],[],[],[],[],[]]
    for i in personal:
        Documento.append(i.documento)
        Nombre_completo.append(i.nombre_completo)
        Fecha_inicio_actividad.append(i.fecha_inicio_actividad)
        Fecha_fin_actividad.append(i.fecha_fin_actividad)
        Observaciones.append(i.observaciones)
        if(i.tipo_persona == "1"):
            Tipo_persona.append("Empleado")
        elif(i.tipo_persona == "2"):
            Tipo_persona.append("Proveedor")
        elif(i.tipo_persona == "3"):
            Tipo_persona.append("Visitante")
        elif(i.tipo_persona == "4"):
            Tipo_persona.append("Contratista")
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
        Empresa.append(i.empresa)
        Portal.append(i.portal_autorizado)
            
        excel = pd.DataFrame()
        excel['Documento'] = Documento
        excel['Nombre completo'] = Nombre_completo
        excel['Empresa'] = Empresa
        excel['Portal autorizado'] = Portal
        excel['Fecha inicio actividad'] = Fecha_inicio_actividad
        excel['Fecha fin actividad'] = Fecha_fin_actividad
        excel['Observaciones'] = Observaciones
        excel['Tipo persona'] = Tipo_persona
        excel['Estado'] = Estado
        
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        excel.to_excel(writer, sheet_name='Personal', index=False)
        writer.save()
        filename = "Personal_AGA"
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
        return response
        
        
def exportarEmpresas(request):
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
            
        excel = pd.DataFrame()
        excel['Nit'] = Nit
        excel['Razón social'] = Razon_social
        excel['Area de servicio'] = Area_servicio
        excel['Fecha inicio actividad'] = Fecha_inicio_actividad
        excel['Fecha fin actividad'] = Fecha_fin_actividad
        excel['Estado'] = Estado
        
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        excel.to_excel(writer, sheet_name='Empresas', index=False)
        writer.save()
        filename = "Empresas_AGA"
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
        return response
        
        
def exportarPortales(request):
    portales = PuntoAcceso.objects.filter(borrado=False)
    Nombre,Latitud,Longitud,Estado=[[],[],[],[]]
    for i in portales:
        Nombre.append(i.nombre)
        Latitud.append(i.latitud)
        Longitud.append(i.longitud)
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
            
        excel = pd.DataFrame()
        excel['Nombre'] = Nombre
        excel['Latitud'] = Latitud
        excel['Longitud'] = Longitud
        excel['Estado'] = Estado
        
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        excel.to_excel(writer, sheet_name='Puntos de Acceso', index=False)
        writer.save()
        filename = "PuntosDeAcceso_AGA"
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(b.getvalue(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
        return response
        
        
def exportarPermisos(request):
    permisos = Permiso.objects.filter(borrado=False)
    Portal_autorizado,Personal,Fecha_inicio_actividad,Fecha_fin_actividad,Estado=[[],[],[],[],[]]
    for i in permisos:
        Portal_autorizado.append(i.portal_autorizado)
        Personal.append(i.personal)
        Fecha_inicio_actividad.append(i.fecha_inicio_actividad)
        Fecha_fin_actividad.append(i.fecha_fin_actividad)
        if(i.estado == "1"):
            Estado.append("Activo")
        else:
            Estado.append("Inactivo")
            
        excel = pd.DataFrame()
        excel['Portal autorizado'] = Portal_autorizado
        excel['Personal'] = Personal
        excel['Fecha inicio actividad'] = Fecha_inicio_actividad
        excel['Fecha fin actividad'] = Fecha_fin_actividad
        excel['Estado'] = Estado
        
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            excel.to_excel(writer, sheet_name='Personal', index=False)
            writer.save()
            filename = "Permisos_AGA"
            content_type = 'application/vnd.ms-excel'
            response = HttpResponse(b.getvalue(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
            return response