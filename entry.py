#!/usr/bin/env python3

'''
Entry example which takes any entered text and displays it when the user
presses the button.
'''

import tkinter

class Entry(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Entry")

        self.entry = tkinter.Entry()
        self.entry.pack(fill=tkinter.BOTH, expand=0)

        button = tkinter.Button(text="Enter", command=self.on_button_click)
        button.pack(fill=tkinter.BOTH, expand=0)

    def on_button_click(self):
        print(self.entry.get())

if __name__ == "__main__":
    application = Entry()
    application.mainloop()
