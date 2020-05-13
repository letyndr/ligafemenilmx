from django.contrib import admin

from .models import Club, Jugadora, Torneo, Jornada, Juego

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = 'nombre_alternativo', 'url', 'logo',
    fields = [
        'nombre',
        'nombre_alternativo',
        'url',
        'logo',
    ]

@admin.register(Jugadora)
class JugadoraAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'debut', 'club', )
    list_filter = ('club', )
    fields = [
        'club',
        'nombre_completo',
        'fecha_nacimiento',
        'lugar_nacimiento',
        'estatura',
        'peso',
        'debut',
        'posicion',
        'url',
        'liga_id',
    ]

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = 'nombre',

@admin.register(Jornada)
class JornadaAdmin(admin.ModelAdmin):
    list_display = 'numero', 'torneo',
    list_filter = 'torneo',

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = 'jornada', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante', 'fecha',
    fields = ['jornada', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante', 'fecha',]

    def get_torneo(self, obj):
        return obj.jornada.torneo

    get_torneo.short_description = 'Torneo'
    get_torneo.admin_order_field = 'jornada__torneo'
    list_filter = 'jornada__torneo', 'equipo_local', 'equipo_visitante', 'jornada',
