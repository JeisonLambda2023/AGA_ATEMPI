import pandas as pd
import os
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import sys

BASE_DIR = settings.BASE_DIR

def cargar_Portales(self,request):
    file = request.FILES["excel"]
    if file:
        self._items = []
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            try:
                data = {
                    # "portales":,
                    "nombre":row["Nombre"],
                    "latitud":row["Latitud"],
                    "longitud":row["Longitud"],
                    }
            except Exception as e:
                return JsonResponse({'error':f"El formato del Excel es incorrecto, por favor verifique la columna: {str(e)}"}, status=400)
