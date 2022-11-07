from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from vianda.models import SolicitudVianda


class SolicitudViandaForm(forms.ModelForm):
    class Meta:
        model = SolicitudVianda
        fields = ('frecuencia', 'tipo_menu', 'fecha_inicio_vianda', 'cantidad_vianda', 'estado','item_tipo_plato',
                  'usuario')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     fecha_inicio_vianda = self.cleaned_data['fecha_inicio_vianda']
    #     fecha_actual = date.now()
    #
    #     # Verifica que la fecha de inicio sea mayor a la fecha actual.
    #     if fecha_inicio_vianda < fecha_actual:
    #         raise ValidationError(
    #             {'fecha_inicio_vianda': 'La Fecha de Inicio no puede ser anterior a la fecha de hoy'},
    #             code='invalido'
    #         )
    #     return cleaned_data
