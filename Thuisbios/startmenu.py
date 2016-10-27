from tkinter import *
from lezenenschrijven import *

value = 'film'
code = 0
name = 0
mail = 0

def ticketsave():
    import time
    date = time.strftime('%d-%m-%Y', time.localtime())
    naam = name
    email = mail
    film = value
    codes = code
    ticket =('{} {} {} {}\n'.format(codes,film, naam, email))
    schijvenstring(ticket,'bezoekers'+ ' '+date+'.csv')

def createqr():
    import pyqrcode
    import random
    aanmeldcode = random.randrange(100000, 1000000)
    global code
    code = aanmeldcode
    qrcode = pyqrcode.create('{}'.format(aanmeldcode), error='L', version=10)
    qrcode.png('qrcode.png', scale=5)
    print(aanmeldcode)
    return(aanmeldcode)

    #qrcode.show()

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

        lst.append('{} ({})'.format(film, jaar))

    return(lst)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def venster_afsluiten():

    startscherm.withdraw()

def venster_terug_openen():

    def venster_terug_sluiten():

        startscherm_terug.withdraw()

    startscherm_terug = Toplevel(startscherm)
    startscherm_terug.title('startscherm')

    label = Label(master=startscherm_terug, text='Inlogscherm', height=2)
    label.pack()

    aanbieder = Button(master=startscherm_terug, text="Inloggen als aanbieder", command=combine_funcs(venster_terug_sluiten, aanbiedersmenu_openen))
    aanbieder.pack(padx=10, pady=10)

    bezoeker = Button(master=startscherm_terug, text="Inloggen als bezoeker", command=combine_funcs(venster_terug_sluiten, bezoekersmenu_openen))
    bezoeker.pack(padx=10, pady=10)

    afsluiten = Button(master=startscherm_terug, text="Afsluiten", command=venster_terug_sluiten)
    afsluiten.pack(padx=20, pady=20)




def bezoekersmenu_openen():
    def bezoekersmenu_sluiten():
       bezoekersmenuscherm.withdraw()

    def volgende():
        def volgende_afsluiten():
            ticket.withdraw()
        photo = PhotoImage(file = "qrcode.png")
        ticket = Toplevel(bezoekersmenuscherm)
        ticket.title('ticket')

        label = Label(master=ticket, text='Ticket')
        label.pack()

        label = Label(master=ticket, text=('Naam:\n {}'.format(naam_invullen.get())))
        label.pack()

        label = Label(master=ticket, text=('Uw E-mail:\n {}'.format(mail_invullen.get())))
        label.pack()

        label = Label(master=ticket, text=('Film:\n{}'.format(value)))
        label.pack()

        label = Label(master=ticket, text='Dit is uw persoonlijke code en qr code:')
        label.pack()

        label = Label(master=ticket, text=('Code:\n{}'.format(createqr())))
        label.pack()

        photo = PhotoImage(file = "qrcode.png")
        qrlabel = Label(master=ticket, image=photo)
        qrlabel.image = photo
        qrlabel.pack()

        terug = Button(master=ticket, text="return", command=combine_funcs(bezoekersmenu_openen, volgende_afsluiten))
        terug.pack(side=LEFT, pady=20)

        afsluiten = Button(master=ticket, text="afsluiten", command=volgende_afsluiten)
        afsluiten.pack(side=RIGHT)

    bezoekersmenuscherm = Toplevel(startscherm)
    bezoekersmenuscherm.title('Bezoekersmenu')
    naam = Label(master=bezoekersmenuscherm,text='Naam')
    naam.pack()

    naam_invullen = Entry(master=bezoekersmenuscherm)
    naam_invullen.pack(padx=10, pady=10)

    mailadres = Label(master=bezoekersmenuscherm,text='E-mail')
    mailadres.pack()

    mail_invullen = Entry(master=bezoekersmenuscherm)
    mail_invullen.pack(padx=10, pady=10)

    opties_aanbieder = Label(master=bezoekersmenuscherm,text='Filmkeuze')
    opties_aanbieder.pack()

    def selection():
        global value
        value = lb1.selection_get()
        return(value)

    lb1 = Listbox(master=bezoekersmenuscherm, width=50, height=10)
    place = 0
    while place < len(filmtotaaltoday()):
        indx = 1
        lb1.insert(indx, filmtotaaltoday()[place])
        place = place+1
        indx = indx+1
    lb1.pack()

    selectButton = Button(master=bezoekersmenuscherm, text='Select', underline = 0,command=selection)
    selectButton.pack(padx=10, pady=5)

    submit = Button(master=bezoekersmenuscherm, text='Submit',command=combine_funcs(volgende, bezoekersmenu_sluiten,ticketsave))
    submit.pack(side=RIGHT)

    terug = Button(master=bezoekersmenuscherm, text="Return", command=combine_funcs(bezoekersmenu_sluiten, venster_terug_openen))
    terug.pack(side=LEFT)

    afsluiten = Button(master=bezoekersmenuscherm, text="Afsluiten", command=bezoekersmenu_sluiten)
    afsluiten.pack(side=BOTTOM)


def aanbiedersmenu_openen():
    def aanbiedersmenu_sluiten():
        aanbiedersmenuscherm.withdraw()
          
    def inloggen():
        text = naam_invullen.get()
        wachtwoord = wachtwoord_invullen.get()

        if text == "Maarten" and wachtwoord == "van Dijk":
            (volgende_aanbiedersmenu())
        elif text == "Florian" and wachtwoord == "Korzelius":
            (volgende_aanbiedersmenu())
        elif text == "Donald" and wachtwoord == "Hioe":
            (volgende_aanbiedersmenu())
        elif text == "Jody" and wachtwoord == "Schuller":
            (volgende_aanbiedersmenu())
        elif text == "Liza" and wachtwoord == "ten Hoven":
            (volgende_aanbiedersmenu())   
        
    def volgende_aanbiedersmenu():
        volgende_aanbiedersmenuscherm = Toplevel(aanbiedersmenuscherm)
        volgende_aanbiedersmenuscherm.title('Overzicht van gegevens')
        def volgende_aanbiedersmenu_sluiten():
            volgende_aanbiedersmenuscherm.withdraw()

        gebruiker = Label(master=volgende_aanbiedersmenuscherm,text=naam_invullen.get())
        gebruiker.pack()

        overzicht_van_nog_niet_aangeboden_films = Label(master=volgende_aanbiedersmenuscherm,text='Een overzicht van nog niet aangeboden films door een andere aanbieder')
        overzicht_van_nog_niet_aangeboden_films.pack()

        lb1 = Listbox(master=volgende_aanbiedersmenuscherm, width=50, height=10)
        place = 0
        while place < len(filmtotaaltoday()):
            indx = 1
            lb1.insert(indx, filmtotaaltoday()[place])
            place = place+1
            indx = indx+1
        lb1.pack()

        #alle films die nog niet worden aangeboden door aanbieders. TOT NU TOE ALLE FILMS DIE ER ZIJN

        overzicht_van_jouw_aangeboden_films = Label(master=volgende_aanbiedersmenuscherm,text='Een overzicht van uw aangeboden films')
        overzicht_van_jouw_aangeboden_films.pack()

        lb1 = Listbox(master=volgende_aanbiedersmenuscherm, width=50, height=10)
        place = 0
        while place < len(filmtotaaltoday()):
            indx = 1
            lb1.insert(indx, filmtotaaltoday()[place])
            place = place+1
            indx = indx+1
        lb1.pack()

        #alle films die je aanbiedt. TOT NU TOE ALLE FILMS DIE ER ZIJN

        overzicht_van_jouw_bezoekers = Label(master=volgende_aanbiedersmenuscherm,text='Een overzicht van uw bezoekers')
        overzicht_van_jouw_bezoekers.pack()

        lb1 = Listbox(master=volgende_aanbiedersmenuscherm, width=50, height=10)
        lb1.pack()

        #jouw bezoekers


        aanmeldcode_bezoekers = Label(master=volgende_aanbiedersmenuscherm,text='De aanmeldcodes van uw bezoekers')
        aanmeldcode_bezoekers.pack()

        lb1 = Listbox(master=volgende_aanbiedersmenuscherm, width=50, height=10)
        lb1.pack()

        #begintijd - naam sorteren

        terug = Button(master=volgende_aanbiedersmenuscherm, text="return", command=combine_funcs(aanbiedersmenu_openen, volgende_aanbiedersmenu_sluiten))
        terug.pack(side=LEFT)

        afsluiten = Button(master=volgende_aanbiedersmenuscherm, text="Afsluiten", command=volgende_aanbiedersmenu_sluiten)
        afsluiten.pack(side=RIGHT)

    aanbiedersmenuscherm = Toplevel(startscherm)
    aanbiedersmenuscherm.title('Aanbiedersmenu')

    gebruikersnaam = Label(master=aanbiedersmenuscherm,text='Gebruikersnaam')
    gebruikersnaam.pack()

    naam_invullen = Entry(master=aanbiedersmenuscherm)
    naam_invullen.pack(padx=10, pady=10)

    wachtwoord = Label(master=aanbiedersmenuscherm,text='Wachtwoord')
    wachtwoord.pack()

    wachtwoord_invullen = Entry(master=aanbiedersmenuscherm,show="*")
    wachtwoord_invullen.pack(padx=10, pady=10)

    submit = Button(master=aanbiedersmenuscherm, text="submit", command=combine_funcs(inloggen,aanbiedersmenu_sluiten)) #naar volgende menu
    submit.pack(side=RIGHT)

    terug = Button(master=aanbiedersmenuscherm, text="return", command=combine_funcs(aanbiedersmenu_sluiten, venster_terug_openen))
    terug.pack(side=LEFT)


    afsluiten = Button(master=aanbiedersmenuscherm, text="afsluiten", command=aanbiedersmenu_sluiten)
    afsluiten.pack(side=BOTTOM)

startscherm = Tk()


label = Label(master=startscherm, text='Inlogscherm', height=2)
label.pack()

aanbieder = Button(master=startscherm, text="Inloggen als aanbieder", command=combine_funcs(venster_afsluiten, aanbiedersmenu_openen))
aanbieder.pack(padx=10, pady=10)

bezoeker = Button(master=startscherm, text="Inloggen als bezoeker", command=combine_funcs(venster_afsluiten, bezoekersmenu_openen))
bezoeker.pack(padx=10, pady=10)

afsluiten = Button(master=startscherm, text="Afsluiten", command=venster_afsluiten)
afsluiten.pack(padx=20, pady=20)

startscherm.mainloop()
