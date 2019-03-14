# Generated by Django 2.1.7 on 2019-03-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendimiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='d_fecha_inicio_periodo',
            field=models.DateField(null=True, verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='d_fecha_regitro',
            field=models.DateField(null=True, verbose_name='Fecha Registro'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='n_id',
            field=models.IntegerField(verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='s_nombre',
            field=models.TextField(verbose_name='Nombre del Reporte'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='s_parametro',
            field=models.TextField(null=True, verbose_name='Parámetro'),
        ),
    ]
