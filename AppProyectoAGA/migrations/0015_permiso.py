# Generated by Django 4.1.7 on 2023-04-19 20:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0014_alter_vehiculo_foto_alter_vehiculo_tipo_vehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio_actividad', models.DateField(default=datetime.date.today)),
                ('fecha_fin_actividad', models.DateField(default=datetime.date.today)),
                ('codigo', models.CharField(max_length=200, unique=True)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default=1, max_length=5)),
                ('borrado', models.BooleanField(blank=True, default=False, null=True)),
                ('personal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppProyectoAGA.personal')),
                ('portal_autorizado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppProyectoAGA.puntoacceso')),
            ],
        ),
    ]