# Generated by Django 4.1.7 on 2023-05-05 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0029_alter_acceso_fecha_ingreso_alter_permiso_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceso',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 14, 28, 28, 197023)),
        ),
        migrations.AlterField(
            model_name='personal',
            name='documento',
            field=models.CharField(max_length=100),
        ),
    ]