# Generated by Django 4.1.7 on 2023-05-05 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0030_alter_acceso_fecha_ingreso_alter_personal_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceso',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 14, 29, 37, 856513)),
        ),
        migrations.AlterField(
            model_name='personal',
            name='documento',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]