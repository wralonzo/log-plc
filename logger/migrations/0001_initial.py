# Generated by Django 4.2.6 on 2024-08-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0001_initial'),
        ('usergroup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=100, verbose_name='Descripión de la accion realizada')),
                ('operador', models.CharField(max_length=100, verbose_name='Nombre del operado')),
                ('equipmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment', verbose_name='Equipo')),
                ('failureTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usergroup.failuretype', verbose_name='Tipo de anomalía')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['-equipmentId'],
            },
        ),
    ]
