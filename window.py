#!/usr/bin/env python3

'''
An example of an empty window with an associated window title and a set window
size.
'''

import tkinter

class Window(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Window")
        self.geometry("200x200")

if __name__ == "__main__":
    application = Window()
    application.mainloop()
