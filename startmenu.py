from tkinter import *
def startmenu():
    root.withdraw()

    def volgende():
        window2.withdraw()
    window2 = Toplevel(master=root)
    label = Label(master=window2, text='ticket:')
    label.pack()

    label = Label(master=window2, text=entry.get())
    label.pack()

    label = Label(master=window2, text=entry2.get())
    label.pack()

    label = Label(master=window2, text='film:')
    label.pack()

    button1 = Button(master=window2, text='afsluiten', command=volgende)
    button1.pack(padx=10, pady=10)

root = Tk()

label = Label(master=root, text='startmenu')
label.pack()

label = Label(master=root,text='naam')
label.pack()

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

label = Label(master=root,text='mailadres')
label.pack()

entry2 = Entry(master=root)
entry2.pack(padx=10, pady=10)

label = Label(master=root,text='opties aanbieder')
label.pack()

label = Label(master=root,text='opties voor films')
label.pack()

button1 = Button(master=root, text='Submit', command=startmenu)
button1.pack(pady=10)

root.mainloop()

startmenu()

