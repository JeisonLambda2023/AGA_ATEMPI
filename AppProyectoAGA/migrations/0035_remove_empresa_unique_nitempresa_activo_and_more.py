# Generated by Django 4.1.7 on 2023-05-10 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0034_alter_acceso_fecha_ingreso_alter_usuario_documento'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='empresa',
            name='unique_nitEmpresa_activo',
        ),
        migrations.RemoveConstraint(
            model_name='permiso',
            name='unique_codigoPermiso_activo',
        ),
        migrations.RemoveConstraint(
            model_name='personal',
            name='unique_documentoPersonal_activo',
        ),
        migrations.RemoveConstraint(
            model_name='usuario',
            name='unique_documentoUsuario_activo',
        ),
        migrations.RemoveConstraint(
            model_name='vehiculo',
            name='unique_placaVehiculo_activo',
        ),
        migrations.AlterField(
            model_name='acceso',
            name='fecha_ingreso',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 8, 39, 51, 824949)),
        ),
    ]