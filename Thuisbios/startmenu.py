import csv
from tkinter import *
from qrcode import *
from Thuisbios.filmtotaaltoday import *

with open('bezoekers.csv', 'r+') as bezoekerscsv:
    writer = csv.writer(bezoekerscsv, delimiter=';')
    writer.writerow(('naam', 'wachtwoord'))

with open('aanbieders.csv', 'r+') as bezoekerscsv:
    writer = csv.writer(bezoekerscsv, delimiter=';')

value = 'film'
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def venster_afsluiten():

    startscherm.withdraw()


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

        terug = Button(master=ticket, text="return", command=combine_funcs(bezoekersmenu_openen))
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

    submit = Button(master=bezoekersmenuscherm, text='Submit',command=combine_funcs(volgende, bezoekersmenu_sluiten))
    submit.pack(side=RIGHT, pady=40)

    terug = Button(master=bezoekersmenuscherm, text="return", command=combine_funcs(bezoekersmenu_sluiten)) #nieuwe functie toevoegen?
    terug.pack(side=LEFT, pady=20)

    afsluiten = Button(master=bezoekersmenuscherm, text="Afsluiten", command=bezoekersmenu_sluiten)
    afsluiten.pack(side=BOTTOM, pady=20)


def aanbiedersmenu_openen():
    def aanbiedersmenu_sluiten():
        aanbiedersmenuscherm.withdraw()
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

    wachtwoord_invullen = Entry(master=aanbiedersmenuscherm)
    wachtwoord_invullen.pack(padx=10, pady=10)

    submit = Button(master=aanbiedersmenuscherm, text="submit", command=combine_funcs(volgende_aanbiedersmenu,aanbiedersmenu_sluiten)) #naar volgende menu
    submit.pack(side=RIGHT)

    terug = Button(master=aanbiedersmenuscherm, text="return", command='') # nieuwe functie toevoegen?
    terug.pack(side=LEFT, pady=20)


    afsluiten = Button(master=aanbiedersmenuscherm, text="afsluiten", command=aanbiedersmenu_sluiten)
    afsluiten.pack(pady=20)

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