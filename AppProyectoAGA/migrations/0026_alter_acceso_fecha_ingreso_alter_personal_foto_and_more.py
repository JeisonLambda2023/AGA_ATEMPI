# Generated by Django 4.1.7 on 2023-05-03 18:58

import AppProyectoAGA.models
import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0025_alter_acceso_fecha_ingreso_alter_empresa_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceso',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 58, 5, 620832)),
        ),
        migrations.AlterField(
            model_name='personal',
            name='foto',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=AppProyectoAGA.models.guardar_imagen_personal, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])], verbose_name='Imagen del personal'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='foto',
            field=models.ImageField(blank=True, default='vehiculo.png', null=True, upload_to=AppProyectoAGA.models.guardar_imagen_vehiculo, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])], verbose_name='Imagen del vehiculo'),
        ),
    ]
