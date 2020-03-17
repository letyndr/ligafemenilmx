from django.contrib import admin

from .models import Club, Jugadora

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url')
    fields = [
        'nombre',
        'url',
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
