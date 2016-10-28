from lezenenschrijven import *
import requests
import xmltodict
import time
date = time.strftime('%d-%m-%Y', time.localtime())
tijd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))

def filmtotaaltoday():
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
        starttijd = films['starttijd']
        starttijd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(starttijd)))

        lst.append('{} {}\n'.format(starttijd, film))
    schijvenlijst(lst,'mogelijke films'+ ' '+date+'.csv')



def aanbiedingMaarten():
    with open('aanbiedingMaarten'+' '+date+'.csv', 'w') as f:
        f.close()

def gekozenaanbiedingenMaarten():
    with open('gekozenaanbiedingenMaarten'+' '+date+'.csv', 'w') as f:
        f.close()

def aanbiedingFlorian():
    with open('aanbiedingFlorian'+' '+date+'.csv', 'w') as f:
        f.close()
def gekozenaanbiedingenFlorian():
    with open('gekozenaanbiedingenFlorian'+' '+date+'.csv', 'w') as f:
        f.close()

def aanbiedingDonald():
    with open('aanbiedingDonald'+' '+date+'.csv', 'w') as f:
        f.close()
def gekozenaanbiedingenDonald():
    with open('gekozenaanbiedingenDonald'+' '+date+'.csv', 'w') as f:
        f.close()

def aanbiedingLiza():
    with open('aanbiedingLiza'+' '+date+'.csv', 'w') as f:
        f.close()
def gekozenaanbiedingenLiza():
    with open('gekozenaanbiedingenLiza'+' '+date+'.csv', 'w') as f:
        f.close()

def aanbiedingJody():
    with open('aanbiedingJody'+' '+date+'.csv', 'w') as f:
       f.close()
def gekozenaanbiedingenJody():
    with open('gekozenaanbiedingenJody'+' '+date+'.csv', 'w') as f:
        f.close()

def GastenMaarten():
    with open('GastenMaarten'+' '+date+'.csv', 'w') as f:
        f.close()

def GastenFlorian():
    with open('GastenFlorian'+' '+date+'.csv', 'w') as f:
        f.close()

def GastenDoanld():
    with open('GastenDonald'+' '+date+'.csv', 'w') as f:
        f.close()

def GastenJody():
    with open('GastenJody'+' '+date+'.csv', 'w') as f:
        f.close()

def GastenLiza():
    with open('GastenLiza'+' '+date+'.csv', 'w') as f:
        f.close()




filmtotaaltoday()
aanbiedingDonald()
aanbiedingFlorian()
aanbiedingJody()
aanbiedingLiza()
aanbiedingMaarten()
gekozenaanbiedingenDonald()
gekozenaanbiedingenFlorian()
gekozenaanbiedingenJody()
gekozenaanbiedingenLiza()
gekozenaanbiedingenMaarten()
GastenDoanld()
GastenFlorian()
GastenJody()
GastenLiza()
GastenMaarten()
