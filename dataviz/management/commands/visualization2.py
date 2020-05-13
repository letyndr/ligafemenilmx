import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from dataviz.models import Club, Jornada, Torneo, Juego


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            df = pd.DataFrame(columns=['A', 'B', 'C'])
            equipos = Club.objects.all()
            for equipo in equipos:
                resultados_local = pd.DataFrame(list(Juego.objects.filter(equipo_local=equipo).values_list('equipo_visitante__nombre_alternativo', 'goles_local')))
                resultados_visitante = pd.DataFrame(list(Juego.objects.filter(equipo_visitante=equipo).values_list('equipo_local__nombre_alternativo', 'goles_visitante')))
                resultados = pd.concat([resultados_local, resultados_visitante])
                group = resultados.groupby(0).sum().reset_index()
                group.columns = ['B', 'C']
                group.insert(0, 'A', equipo.nombre_alternativo)

                df = pd.concat([df, group])
                df.to_csv('dataviz/visualization/data2.csv', index=False)
            # logos = list(Club.objects.values_list('logo', flat=True))

            # jornadas = Jornada.objects.all()
            # header = pd.Series([i for i in range(len(jornadas) + 1)])
            # df = pd.DataFrame(0, index=equipos, columns=header)

            # torneos = Torneo.objects.all()
            # num_jornada = 1
            # for torneo in torneos:
            #     jornadas = Jornada.objects.filter(torneo=torneo)
            #     for jornada in jornadas:
            #         resultados_local = pd.DataFrame.from_records(list
            #         (Juego.objects.filter(jornada=jornada).values('equipo_local__nombre', 'goles_local')))
            #         resultados_visitante = pd.DataFrame.from_records(Juego.objects.filter(jornada=jornada).values('equipo_visitante__nombre', 'goles_visitante'))
            #         resultados_local.columns = ['equipo', 'goles']
            #         resultados_visitante.columns = ['equipo', 'goles']
            #         resultados = pd.concat([resultados_local, resultados_visitante])
            #         resultados = resultados.set_index('equipo')

            #         for index, row in resultados.iterrows():
            #             df.at[index, num_jornada] = row['goles']
            #         num_jornada += 1

            # for column in df.columns[1:]:
            #     df[column] = df[column-1] + df[column]

            # df.insert(loc=0, column='logo', value=logos)
            # df.to_csv('dataviz/visualization/data.csv')

        except expression as identifier:
            raise CommandError('Something went wrong!')
