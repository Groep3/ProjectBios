from tkinter import *

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

        label = Label(master=ticket, text=naam_invullen.get())
        label.pack()

        label = Label(master=ticket, text=mail_invullen.get())
        label.pack()

        label = Label(master=ticket, text='film:')
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

    opties_aanbieder = Label(master=bezoekersmenuscherm,text='opties aanbieder')
    opties_aanbieder.pack()

    aanbieders = Button(master=bezoekersmenuscherm, text='aanbieders', command=aanbieders)
    aanbieders.pack(pady=10)

    aanbieder = Label(master=bezoekersmenuscherm,text='aanbieder(werkt nog niet)')
    aanbieder.pack()

    aanbieder_invullen = Entry(master=bezoekersmenuscherm)
    aanbieder_invullen.pack(padx=10, pady=10)

    opties_voor_films = Label(master=bezoekersmenuscherm,text='opties voor films')
    opties_voor_films.pack()

    films = Button(master=bezoekersmenuscherm, text='films', command=filmopties)
    films.pack(pady=10)

    film = Label(master=bezoekersmenuscherm,text='film(werkt nog niet)')
    film.pack()

    film_invullen = Entry(master=bezoekersmenuscherm)
    film_invullen.pack(padx=10, pady=10)

    submit = Button(master=bezoekersmenuscherm, text='Submit',command=combine_funcs(volgende, bezoekersmenu_sluiten)) #command toevoegen
    submit.pack(padx=20, pady=40)


    afsluiten = Button(master=bezoekersmenuscherm, text="afsluiten", command=bezoekersmenu_sluiten)
    afsluiten.pack(padx=20, pady=20)


def aanbiedersmenu_openen():
    def aanbiedersmenu_sluiten():
        aanbiedersmenuscherm.withdraw()
    aanbiedersmenuscherm = Toplevel(startscherm)
    aanbiedersmenuscherm.title('aanbiedersmenu')
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
