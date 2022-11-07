from django.contrib import admin

# Register your models here.
from vianda.models import TipoPlato, SolicitudVianda


@admin.register(TipoPlato)
class TipoPlatoAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


@admin.register(SolicitudVianda)
class SolicitudViandaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


