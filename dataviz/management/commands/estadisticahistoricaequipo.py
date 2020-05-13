from bs4 import BeautifulSoup
import urllib.request
import ssl
from django.core.management.base import BaseCommand, CommandError
import re

from dataviz.models import Torneo, Jornada, Juego, Club

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            context = ssl._create_unverified_context()
            url = 'http://ligafemenil.mx/cancha/estadisticahistorica/1/eyJpZERpdmlzaW9uIjoiMTQiLCJpZFRlbXBvcmFkYSI6IjcwIiwgImlkVG9ybmVvIjoiMiJ9'
            page = urllib.request.urlopen(url, context=context)
            soup = BeautifulSoup(page, 'html.parser')
            table = soup.find('tbody')
            content = table.find_all('tr')
            torneo = Torneo.objects.get(nombre='Clausura 2020')
            for tr in content[1:]:
                print('\n\n\n*****************************************************')
                link = tr.find_all('a', {'class': 'loadershow'})[2]['href']
                url2 = f'http://ligafemenil.mx/{link}'
                page = urllib.request.urlopen(url2, context=context)
                soup = BeautifulSoup(page, 'html.parser')
                juegos = soup.find_all('td')
                del juegos[0]
                del juegos[-1]
                offset = 8
                for i in range(0, len(juegos), offset):
                    print('---------------------------------------------------')
                    num_jornada = re.search(r'^J-(\d+)$', juegos[i].get_text())
                    num_jornada = num_jornada.groups()[0]
                    jornada = Jornada.objects.get(torneo=torneo, numero=num_jornada)
                    print(f'Jornada: {jornada}')
                    local = juegos[i+1].get_text().strip()
                    print(f'Local: {local}')
                    equipo_local = Club.objects.get(nombre=local)
                    print(f'Equipo Local: {equipo_local}')
                    goles_local = int(juegos[i+2].get_text().strip())
                    goles_visitante = int(juegos[i+3].get_text().strip())
                    visitante = juegos[i+4].get_text().strip()
                    print(f'visitante: {visitante}')
                    equipo_visitante = Club.objects.get(nombre=visitante)
                    print(f'Equipo visitante: {equipo_visitante}')
                    fecha = juegos[i+5].get_text() + ' ' + juegos[i+6].get_text()
                    print(f'fecha: {fecha}')

                    juego = Juego.objects.filter(
                        jornada__torneo=torneo,
                        jornada=jornada,
                        equipo_local=equipo_local,
                        equipo_visitante=equipo_visitante,
                    )
                    
                    if not juego:
                        juego = Juego(
                            jornada=jornada,
                            equipo_local=equipo_local,
                            equipo_visitante=equipo_visitante,
                            goles_local=goles_local,
                            goles_visitante=goles_visitante,
                            fecha=fecha,
                        )
                        juego.save()

                # del tbody[0]
                # juegos = soup.find('tr', {'class': 'informacion fila1'})
                # print(juegos)
                # for juego in tbody:
                #     print(juego)
        except expression as identifier:
            raise CommandError('Something went wrong!')
