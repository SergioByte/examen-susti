# Generated by Django 3.1.4 on 2021-02-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('image', models.ImageField(default='null', upload_to='regiones', verbose_name='Miniatura')),
                ('deaths', models.CharField(max_length=10, verbose_name='Muertes')),
                ('cases', models.CharField(max_length=10, verbose_name='Casos')),
                ('estado', models.CharField(max_length=1, verbose_name='Estado')),
                ('lethality', models.CharField(max_length=4, verbose_name='Letalidad')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
    ]
