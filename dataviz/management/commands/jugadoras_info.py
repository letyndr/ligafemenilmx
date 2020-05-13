from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import ssl

from django.core.management.base import BaseCommand, CommandError
from dataviz.models import Jugadora

host = 'https://www.ligafemenil.mx'


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            jugadoras = Jugadora.objects.filter(club__nombre='Santos Laguna')
            for jugadora in jugadoras:
                if not jugadora.nombre_completo:
                    context = ssl._create_unverified_context()
                    # url = 'https://www.ligafemenil.mx/cancha/jugador/125419/eyJpZENsdWIiOiAxMTE4Nn0=/lizbeth-jacqueline-ovalle-mu%C3%B1oz'
                    # page = urllib.request.urlopen(url, context=context)
                    page = urllib.request.urlopen(jugadora.url, context=context)
                    soup = BeautifulSoup(page, 'html.parser')
                    content = soup.find(id='infoJugador')
                    nombre = content.find('h1', class_='nombre').text

                    # print(nombre)
                    # numero = content.find('h2', class_='numero').text[1:]
                    detalles = content.find_all('dl', class_='datos-jugador')

                    detalle1 = detalles[0]
                    detalle2 = detalles[1]
                    detalle3 = detalles[2]
                    detalle4 = detalles[3]

                    elements = detalle1.find_all('dd')
                    fecha_nacimiento_str = elements[0].text
                    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y')
                    lugar_nacimiento = elements[1].text

                    elements = detalle2.find_all('dd')
                    estatura =float(elements[1].text)
                    peso = float(elements[2].text[:-3])

                    debut = detalle3.find('dd').text if detalle3.find('dd') else None

                    posicion = detalle4.find('dd').text

                    print(f'\n\n\nnombre: {nombre}')
                    # print(f'numero: {numero}')
                    print(f'fec nac: {fecha_nacimiento}')
                    print(f'lug nac: {lugar_nacimiento}')
                    print(f'est: {estatura}')
                    print(f'peso: {peso}')
                    print(f'debut: {debut}')
                    print(f'posicion: {posicion}')

                    jugadora.nombre_completo = nombre
                    jugadora.fecha_nacimiento = fecha_nacimiento
                    jugadora.lugar_nacimiento = lugar_nacimiento
                    jugadora.estatura = estatura
                    jugadora.peso = peso
                    jugadora.debut =  debut
                    jugadora.posicion = posicion

                    jugadora.save()

        except expression as identifier:
            raise CommandError('Something went wrong!')

