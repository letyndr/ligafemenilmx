from bs4 import BeautifulSoup
import urllib.request
import ssl

from django.core.management.base import BaseCommand, CommandError
from dataviz.models import Club, Jugadora

host = 'https://www.ligafemenil.mx'


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            clubes = Club.objects.all()
            for club in clubes:
                if club.nombre == 'Santos Laguna':
                    print(club)
                # club = Club.objects.get(nombre='Pachuca')
                    url = club.url
                    context = ssl._create_unverified_context()
                    page = urllib.request.urlopen(url, context=context)

                    soup = BeautifulSoup(page, 'html.parser')
                    jugadoras = soup.find_all('div', class_='card-block')

                    for index, posicion in enumerate(jugadoras):
                        a = posicion.find('a', class_='loadershow')
                        href = a['href']
                        if 'jugador' in href:
                            print(href)
                            url = host + href
                            jugadora = Jugadora(url=url, club=club)
                            # jugadora = Jugadora.objects.get(url=url)
                            jugadora.liga_id = int(url.split('/')[5])
                            jugadora.save()
        except expression as identifier:
            raise CommandError('Something went wromg!')

