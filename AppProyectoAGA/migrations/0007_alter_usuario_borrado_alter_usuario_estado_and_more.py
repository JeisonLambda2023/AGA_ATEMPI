# Generated by Django 4.1.7 on 2023-04-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0006_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='borrado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('1', 'Administrador'), ('0', 'Operador')], default=1, max_length=5),
        ),
    ]