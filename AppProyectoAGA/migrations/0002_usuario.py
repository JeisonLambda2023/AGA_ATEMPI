# Generated by Django 4.2 on 2023-04-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoAGA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('documento', models.BigIntegerField(unique=True)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('rol', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('borrado', models.IntegerField(blank=True, null=True)),
                ('administrador', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]