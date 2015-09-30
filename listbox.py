#!/usr/bin/env python3

'''
Entry example which takes any entered text and displays it when the user
presses the button.
'''

import tkinter

class Listbox(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Listbox")

        listbox = tkinter.Listbox()
        listbox.insert(tkinter.END, "Io")
        listbox.insert(tkinter.END, "Europa")
        listbox.insert(tkinter.END, "Ganymede")
        listbox.insert(tkinter.END, "Callisto")
        listbox.pack(fill=tkinter.BOTH, expand=0)

if __name__ == "__main__":
    application = Listbox()
    application.mainloop()
