# Generated by Django 4.1.7 on 2023-05-09 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0033_remove_permiso_unique_codigo_activo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceso',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 7, 45, 36, 768756)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='documento',
            field=models.BigIntegerField(),
        ),
    ]
