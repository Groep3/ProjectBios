from tkinter import *
from filmtotaal import *

def selection():
    a = lb1.selection_get()
    print(a)

root = Tk()
frame = Frame(root)
frame.pack()


lb1 = Listbox(master=root, width=50, height=10)
place = 0
while place < len(filmtotaal()):
    a = 1
    lb1.insert(a, filmtotaal()[place])
    place = place+1
    a= a+1
lb1.pack()

selectButton = Button(frame, text='Select', underline = 0,command=selection)
selectButton.pack()

root.bind('<Double-1>', lambda x: selectButton.invoke())


root.mainloop()
