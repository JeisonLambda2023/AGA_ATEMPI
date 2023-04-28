# Generated by Django 4.1.7 on 2023-04-25 14:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0015_permiso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingreso', models.CharField(choices=[('1', 'Dentro del punto de acceso'), ('0', 'Fuera del punto de acceso')], max_length=5)),
                ('fecha_ingreso', models.DateField(default=datetime.datetime(2023, 4, 25, 9, 14, 33, 925123))),
                ('empresa', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('1', 'Dentro del punto de acceso'), ('0', 'Fuera del punto de acceso')], default=1, max_length=5)),
                ('borrado', models.BooleanField(blank=True, default=False, null=True)),
                ('personal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppProyectoAGA.personal')),
                ('vehiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AppProyectoAGA.vehiculo')),
            ],
        ),
    ]
