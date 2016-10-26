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
    bezoekersmenuscherm = Toplevel(startscherm)
    bezoekersmenuscherm.title('bezoekersmenu')
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
