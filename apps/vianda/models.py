from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class TipoPlato(models.Model):
    descripcion = models.CharField(max_length=200)
    es_activo = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion


class SolicitudVianda(models.Model):
    SEMANAL = 'Semanal'
    QUINCENAL = 'Quincenal'
    FRECUENCIA_CHOICES = [
        (SEMANAL, 'Semanal'),
        (QUINCENAL, 'Quincenal'),
    ]
    FRECUENCIA_CHOICES = [
        (SEMANAL, 'Semanal'),
        (QUINCENAL, 'Quincenal'),
    ]

    NORMAL = 'Normal'
    DIABETICO = 'Diabetico'
    VEGETARIANO = 'Vegetariano'
    TIPO_MENU_CHOICES = [
        (NORMAL, 'Normal'),
        (DIABETICO, 'Diabetico'),
        (VEGETARIANO, 'Vegetariano'),
    ]

    PENDIENTE = 'Pendiente'
    CONFIRMADO = 'Confirmado'
    CANCELADO = 'Cancelado'
    ESTADOS = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADO, 'Confirmado'),
        (CANCELADO, 'Cancelado'),
    ]

    frecuencia = models.CharField(
        max_length=9,
        choices=FRECUENCIA_CHOICES,
        default=SEMANAL,
    )
    tipo_menu = models.CharField(
        max_length=11,
        choices=TIPO_MENU_CHOICES,
        default=SEMANAL,
    )
    fecha_inicio_vianda = models.DateField(verbose_name='Fecha Inicio de Vianda')
    cantidad_vianda = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default=PENDIENTE,
    )
    item_tipo_plato = models.ManyToManyField(TipoPlato)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viandas')

    def __str__(self):
        return f"{self.frecuencia} Tipo Menu {self.tipo_menu }"
