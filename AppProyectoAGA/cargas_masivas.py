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

def validar_portal(item): 
    if  item["nombre"] == "nan" or item["nombre"] == None or item["nombre"]=="": 
        raise Exception({"nombre":"La columna 'nombre' esta vacia"})
    if  item["latitud"] == "nan" or item["latitud"] == None or item["latitud"]=="": 
        raise Exception({"latitud":"La columna 'latitud' esta vacia"}) 
    if  item["longitud"] == "nan" or item["longitud"] == None or item["longitud"]=="": 
        raise Exception({"longitud":"La columna 'longitud' esta vacia"}) 
    return True

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
