#!/usr/bin/env python3

'''
An example of three labels packed into three separate PanedWindow areas with
values set for the width of handle and sash.
'''

import tkinter

class PanedWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Label")

        panedwindow = tkinter.PanedWindow()
        panedwindow.config(handlesize=10)
        panedwindow.config(sashwidth=5)
        panedwindow.config(sashrelief=tkinter.RAISED)
        panedwindow.pack(fill=tkinter.BOTH, expand=1)

        label = tkinter.Label(text="Label in Pane 1")
        panedwindow.add(label)
        label = tkinter.Label(text="Label in Pane 2")
        panedwindow.add(label)
        label = tkinter.Label(text="Label in Pane 3")
        panedwindow.add(label)

if __name__ == "__main__":
    application = PanedWindow()
    application.mainloop()
