# Generated by Django 4.1.7 on 2023-04-17 17:37

import AppProyectoAGA.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0013_alter_personal_tipo_persona_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='foto',
            field=models.ImageField(blank=True, default='vehiculo.png', null=True, upload_to=AppProyectoAGA.models.guardar_imagen_vehiculo, verbose_name='Imagen del vehiculo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo_vehiculo',
            field=models.CharField(choices=[('1', 'Camión'), ('2', 'Camioneta'), ('3', 'Motocicleta'), ('4', 'Volqueta')], max_length=5),
        ),
    ]