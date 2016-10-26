from tkinter import*
class Application(Frame):
    def aanbiedersmenu_openen():
        def aanbiedersmenu_sluiten():
            aanbiedersmenuscherm.withdraw()
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



        afsluiten = Button(master=aanbiedersmenuscherm, text="afsluiten", command=aanbiedersmenu_sluiten)
        afsluiten.pack(padx=20, pady=20)
