from tkinter import *
def startmenu():
    root = Tk()

    label = Label(master=root, text='hoofdmenu')
    label.pack()

    label = Label(master=root,text='naam',height=4)
    label.pack()

    entry = Entry(master=root)
    entry.pack(padx=10, pady=10)

    label = Label(master=root,text='mailadres',height=6)
    label.pack()

    entry = Entry(master=root)
    entry.pack(padx=10, pady=10)

    button = Button(master=root, text='Submit', command='')
    button.pack(pady=10)


    root.mainloop()

startmenu()

print('test')
