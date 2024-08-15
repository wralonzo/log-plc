# Generated by Django 4.2.6 on 2024-08-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del PLC')),
                ('location', models.CharField(max_length=100, verbose_name='Ubicación')),
                ('encargado', models.CharField(max_length=100, verbose_name='Nombre del encargado')),
            ],
            options={
                'verbose_name': 'PLC',
                'verbose_name_plural': 'PLC',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del sensor')),
                ('deviceId', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='equipment.device', verbose_name='PLC asociado')),
            ],
            options={
                'verbose_name': 'Sensor',
                'verbose_name_plural': 'Sensores',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del equipo')),
                ('sensorId', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='equipment.device', verbose_name='Sensor asociado')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['-name'],
            },
        ),
    ]
