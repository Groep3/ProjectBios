from tkinter import *
from filmtotaaltoday import *

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
    def aanbieders():
        aanbiedersscherm = Toplevel(bezoekersmenuscherm)
        aanbiedersscherm.title('aanbieders')

        label = Label(master=aanbiedersscherm, text='aanbieders:')
        label.pack()

    def filmopties():
        films = Toplevel(bezoekersmenuscherm)
        films.title('opties voor films')

        label = Label(master=films, text='films:')
        label.pack()

    def volgende():
        ticket = Toplevel(bezoekersmenuscherm)
        ticket.title('ticket')

        label = Label(master=ticket, text='ticket')
        label.pack()

        label = Label(master=ticket, text=('Naam:\n {}'.format(naam_invullen.get())))
        label.pack()

        label = Label(master=ticket, text=('Mailadress:\n {}'.format(mail_invullen.get())))
        label.pack()

        label = Label(master=ticket, text=('film:\n{}'.format(value)))
        label.pack()

        label = Label(master=ticket, text='code:')
        label.pack()

        label = Label(master=ticket, text='een idee voor een code?')
        label.pack()

        label = Label(master=ticket, text='noteer de code')
        label.pack()


    bezoekersmenuscherm = Toplevel(startscherm)
    bezoekersmenuscherm.title('bezoekersmenu')
    naam = Label(master=bezoekersmenuscherm,text='naam')
    naam.pack()

    naam_invullen = Entry(master=bezoekersmenuscherm)
    naam_invullen.pack(padx=10, pady=10)

    mailadres = Label(master=bezoekersmenuscherm,text='mailadres')
    mailadres.pack()

    mail_invullen = Entry(master=bezoekersmenuscherm)
    mail_invullen.pack(padx=10, pady=10)

    opties_aanbieder = Label(master=bezoekersmenuscherm,text='filmkeuze')
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

    submit = Button(master=bezoekersmenuscherm, text='Submit',command=combine_funcs(volgende, bezoekersmenu_sluiten)) #command toevoegen
    submit.pack(padx=20, pady=40)




    afsluiten = Button(master=bezoekersmenuscherm, text="afsluiten", command=bezoekersmenu_sluiten)
    afsluiten.pack(padx=20, pady=20)


def aanbiedersmenu_openen():
    def aanbiedersmenu_sluiten():
        aanbiedersmenuscherm.withdraw()
    def volgende_aanbiedersmenu():
        volgende_aanbiedersmenuscherm = Toplevel(aanbiedersmenuscherm)
        volgende_aanbiedersmenuscherm.title('overzicht van gegevens')
        def volgende_aanbiedersmenu_sluiten():
            volgende_aanbiedersmenuscherm.withdraw()



        overzicht_van_nog_niet_aangeboden_films = Label(master=volgende_aanbiedersmenuscherm,text='overzicht van nog niet aangeboden films door een ander aanbieder')
        overzicht_van_nog_niet_aangeboden_films.pack()

        #alle films die nog niet worden aangeboden door aanbieders

        overzicht_van_jouw_aangeboden_films = Label(master=volgende_aanbiedersmenuscherm,text='overzicht van jouw aangeboden films')
        overzicht_van_jouw_aangeboden_films.pack()

        #alle films die je aanbiedt

        overzicht_van_jouw_bezoekers = Label(master=volgende_aanbiedersmenuscherm,text='overzicht van jouw bezoekers')
        overzicht_van_jouw_bezoekers.pack()

        #jouw bezoekers


        aanmeldcode_bezoekers = Label(master=volgende_aanbiedersmenuscherm,text='aanmeldcodes van bezoekers')
        aanmeldcode_bezoekers.pack()

        #begintijd - naam sorteren

        afsluiten = Button(master=volgende_aanbiedersmenuscherm, text="afsluiten", command=volgende_aanbiedersmenu_sluiten)
        afsluiten.pack(padx=20, pady=20)

    aanbiedersmenuscherm = Toplevel(startscherm)
    aanbiedersmenuscherm.title('aanbiedersmenu')

    gebruikersnaam = Label(master=aanbiedersmenuscherm,text='gebruikersnaam')
    gebruikersnaam.pack()

    naam_invullen = Entry(master=aanbiedersmenuscherm)
    naam_invullen.pack(padx=10, pady=10)

    wachtwoord = Label(master=aanbiedersmenuscherm,text='wachtwoord')
    wachtwoord.pack()

    wachtwoord_invullen = Entry(master=aanbiedersmenuscherm)
    wachtwoord_invullen.pack(padx=10, pady=10)

    submit = Button(master=aanbiedersmenuscherm, text="submit", command=combine_funcs(volgende_aanbiedersmenu,aanbiedersmenu_sluiten)) #naar volgende menu
    submit.pack(padx=20, pady=20)

    afsluiten = Button(master=aanbiedersmenuscherm, text="afsluiten", command=aanbiedersmenu_sluiten)
    afsluiten.pack(padx=20, pady=20)


startscherm = Tk()


label = Label(master=startscherm, text='inlogscherm', height=2)
label.pack()

aanbieder = Button(master=startscherm, text="inloggen als aanbieder", command=combine_funcs(venster_afsluiten, aanbiedersmenu_openen))
aanbieder.pack(padx=10, pady=10)

bezoeker = Button(master=startscherm, text="inloggen als bezoeker", command=combine_funcs(venster_afsluiten, bezoekersmenu_openen))
bezoeker.pack(padx=10, pady=10)

afsluiten = Button(master=startscherm, text="afsluiten", command=venster_afsluiten)
afsluiten.pack(padx=20, pady=20)


startscherm.mainloop()
