from django.db import models


class Club(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Jugadora(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    nombre_completo = models.CharField(unique=True, max_length=256, null=True, blank=True)
    fecha_nacimiento = models.DateTimeField('fecha de nacimiento', null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=256, null=True, blank=True)
    estatura = models.FloatField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    debut = models.CharField(max_length=256, null=True, blank=True)
    posicion = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    liga_id = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre_completo if self.nombre_completo else '--'

class EstadisticaJugadora(models.Model):
    jugadora = models.ForeignKey(Jugadora, on_delete=models.CASCADE, blank=True, null=True)
    juegos_jugados = models.IntegerField(default=0)
    juegos_titular = models.IntegerField(default=0)
    goles = models.IntegerField(default=0)
    autogoles = models.IntegerField(default=0)
    minutos_jugados = models.IntegerField(default=0)
    tarjetas_amarillas = models.IntegerField(default=0)
    tarjetas_rojas = models.IntegerField(default=0)
