import requests
import xmltodict


api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=3yakjh3yeghyppmgt99azqkfjjfrundg&dag=26-10-2016&sorteer=0'
response = requests.get(api_url)


filmsXML = xmltodict.parse(response.text)

for films in filmsXML['filmsoptv']['film']:
    film = films['titel']
    jaar = films['jaar']
    duur = films['duur']
    genre = films['genre']
    synopsis = films['synopsis']
    regisseur = films['regisseur']
    cast = films['cast']
    land = films['land']
    cover = films['cover']

    print('{} ({})'.format(film, jaar))
