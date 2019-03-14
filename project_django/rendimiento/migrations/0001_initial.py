# Generated by Django 2.1.7 on 2019-03-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_id', models.IntegerField()),
                ('s_nombre', models.TextField(verbose_name='Nombre')),
                ('s_parametro', models.TextField(verbose_name='Parámetro')),
                ('b_activo', models.BooleanField(verbose_name='Activo')),
                ('d_fecha_inicio_periodo', models.DateField(verbose_name='Fecha_Inicio')),
                ('d_fecha_regitro', models.DateField(verbose_name='Fecha_Registro')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
            },
        ),
    ]