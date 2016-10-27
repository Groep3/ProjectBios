from lezenenschrijven import *
def filmtotaaltoday():
    import requests
    import xmltodict
    import time
    date = time.strftime('%d-%m-%Y', time.localtime())
    api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=3yakjh3yeghyppmgt99azqkfjjfrundg&dag='+date+'&sorteer=0'
    response = requests.get(api_url)
    filmsXML = xmltodict.parse(response.text)

    lst = []
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

        lst.append('{} ({})\n'.format(film, jaar))
    schijvenlijst(lst,'mogelijke films'+ ' '+date+'.csv')

filmtotaaltoday()
