from tkinter import *
import csv

with open('bezoeker.csv', 'w') as bezoekerscsv:
    writer = csv.writer(bezoekerscsv, delimiter=';')
    writer.writerow(('naam', 'wachtwoord'))

def startmenu():

    root.withdraw()

    def volgende():
        window2.withdraw()
    window2 = Toplevel(master=root)

    ###################################################

    label = Label(master=window2, text='ticket:')
    label.pack()

    ##########################################################

    label = Label(master=window2, text=naam_invullen.get())
    label.pack()

    ##########################################################

    label = Label(master=window2, text=mail_invullen.get())
    label.pack()

    ####################################################

    label = Label(master=window2, text='film:')
    label.pack()

    #################################################

    label = Label(master=window2, text='code:')
    label.pack()

    label = Label(master=window2, text=naam_invullen.get() + mail_invullen.get())
    label.pack()

    ###############################################################

    label = Label(master=window2, text='noteer de code')
    label.pack()

    #########################################################################

    button1 = Button(master=window2, text='afsluiten', command=volgende)
    button1.pack(padx=10, pady=10)

    def aanbiedersmenu():
        window3.withdraw()
    window3 = Toplevel(master=root)

    #################################################################

    label = Label(master=window3, text='dit zijn de aanbieders:')
    label.pack()

    ############################################################################################

    afsluiten_aanbiedersmenu = Button(master=window3, text='afsluiten', command=aanbiedersmenu)
    afsluiten_aanbiedersmenu.pack(padx=10, pady=10)

    def filmsmenu():
        window4.withdraw()
    window4 = Toplevel(master=root)

    ###########################################################

    label = Label(master=window4, text='dit zijn de films:')
    label.pack()

    #####################################################################################
    afsluiten_filmmenu = Button(master=window4, text='afsluiten', command=filmsmenu)
    afsluiten_filmmenu.pack(padx=10, pady=10)



root = Tk()

##################################################

label = Label(master=root, text='startmenu')
label.pack()

################################################

label = Label(master=root,text='naam')
label.pack()

naam_invullen = Entry(master=root)
naam_invullen.pack(padx=10, pady=10)

##############################################

label = Label(master=root,text='mailadres')
label.pack()

mail_invullen = Entry(master=root)
mail_invullen.pack(padx=10, pady=10)

##################################################

label = Label(master=root,text='opties aanbieder')
label.pack()

button1 = Button(master=root, text='aanbieders', command=startmenu)
button1.pack(pady=10)

label = Label(master=root,text='aanbieder(werkt nog niet)')
label.pack()

aanbieder_invullen = Entry(master=root)
aanbieder_invullen.pack(padx=10, pady=10)

##########################################################

label = Label(master=root,text='opties voor films')
label.pack()

button1 = Button(master=root, text='films', command=startmenu)
button1.pack(pady=10)

label = Label(master=root,text='film(werkt nog niet)')
label.pack()

film_invullen = Entry(master=root)
film_invullen.pack(padx=10, pady=10)

###############################################################

button1 = Button(master=root, text='Submit', command=startmenu)
button1.pack(pady=10)
root.mainloop()

startmenu()

print('de buttons in de startscherm opent alle andere 3 menu"s')
