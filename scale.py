#!/usr/bin/env python3

'''
Entry example which takes any entered text and displays it when the user
presses the button.
'''

import tkinter

class Scale(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Scale")

        scale = tkinter.Scale()
        scale.config(from_=0, to=100)
        scale.set(25)
        scale.pack(fill=tkinter.BOTH, expand=0)

if __name__ == "__main__":
    application = Scale()
    application.mainloop()
