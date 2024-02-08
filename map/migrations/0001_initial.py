# Generated by Django 5.0.1 on 2024-02-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosAgrarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anyo_precio', models.IntegerField()),
                ('semana_precio', models.IntegerField()),
                ('codigo_grupo_producto', models.IntegerField()),
                ('grupo_producto_castellano', models.CharField(max_length=255)),
                ('grupo_producto_valenciano', models.CharField(max_length=255)),
                ('codigo_producto', models.IntegerField()),
                ('producto_castellano', models.CharField(max_length=255)),
                ('producto_valenciano', models.CharField(max_length=255)),
                ('codigo_variedad', models.IntegerField()),
                ('variedad_castellano', models.CharField(max_length=255)),
                ('variedad_valenciano', models.CharField(max_length=255)),
                ('codigo_zona', models.IntegerField()),
                ('zona_castellano', models.CharField(max_length=255)),
                ('zona_valenciano', models.CharField(max_length=255)),
                ('precio_minimo', models.FloatField()),
                ('precio_medio', models.FloatField()),
                ('precio_maximo', models.FloatField()),
            ],
        ),
    ]
