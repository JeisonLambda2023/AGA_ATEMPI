# Generated by Django 4.1.7 on 2023-05-05 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0027_alter_acceso_fecha_ingreso_alter_permiso_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceso',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 12, 27, 11, 941677)),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='codigo',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
