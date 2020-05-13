from django.db import models


class Club(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_alternativo = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    logo = models.CharField(max_length=500, null=True, blank=True)

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

class Torneo(models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Jornada(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    numero = models.IntegerField()

    def __str__(self):
        return f'J-{self.numero}'

class Juego(models.Model):
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    equipo_local = models.ForeignKey(Club, related_name='equipo_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Club, related_name='equipo_visitante', on_delete=models.CASCADE)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    fecha = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.equipo_local} - {self.equipo_visitante}'

class EstadisticaHistoricaEquipo(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=500, null=True, blank=True)
