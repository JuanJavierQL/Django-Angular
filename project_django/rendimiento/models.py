from django.db import models

# Create your models here.

class Reporte(models.Model):
    """Model definition for Reporte."""

    # TODO: Define fields here

    n_id = models.IntegerField(verbose_name="Id", db_index=True)
    s_nombre = models.TextField(verbose_name="Nombre del Reporte", max_length=100)
    s_parametro = models.TextField(verbose_name="Parámetro", null=True, blank=True)
    b_activo = models.BooleanField(verbose_name="Activo")
    d_fecha_inicio_periodo = models.DateField(verbose_name="Fecha Inicio", null=True, blank=True)
    d_fecha_regitro = models.DateField(verbose_name="Fecha Registro", null=True, blank=True)


    class Meta:
        """Meta definition for Reporte."""

        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        """Unicode representation of Reporte."""
        return self.s_nombre
