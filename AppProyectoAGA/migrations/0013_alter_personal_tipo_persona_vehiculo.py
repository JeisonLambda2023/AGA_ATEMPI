# Generated by Django 4.1.7 on 2023-04-17 13:24

import AppProyectoAGA.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0012_alter_personal_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='tipo_persona',
            field=models.CharField(choices=[('1', 'Empleado'), ('2', 'Proveedor'), ('3', 'Visitante'), ('4', 'Contratista')], max_length=5),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('fecha_inicio_actividad', models.DateField(default=datetime.date.today)),
                ('fecha_fin_actividad', models.DateField(default=datetime.date.today)),
                ('observaciones', models.TextField(blank=True, max_length=300, null=True)),
                ('tipo_vehiculo', models.CharField(choices=[('1', 'Empleado'), ('2', 'Proveedor'), ('3', 'Visitante'), ('4', 'Contratista')], max_length=5)),
                ('foto', models.ImageField(blank=True, default='user.png', null=True, upload_to=AppProyectoAGA.models.guardar_imagen_vehiculo, verbose_name='Imagen del vehiculo')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default=1, max_length=5)),
                ('borrado', models.BooleanField(blank=True, default=False, null=True)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppProyectoAGA.empresa')),
            ],
        ),
    ]
