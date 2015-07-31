#!/usr/bin/env python3

'''
Showcasing a LabelFrame widget with a packed Label widget. The frame also
contains 10 pixel padding providing a gap within the frame edge.
'''

import tkinter

class LabelFrame(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("LabelFrame")
        self.geometry("200x200")

        labelframe = tkinter.LabelFrame(text="LabelFrame", padx=10, pady=10)
        labelframe.pack(fill=tkinter.BOTH, expand=1)

        label = tkinter.Label(labelframe, text="This Label is packed\nwithin the LabelFrame.")
        label.pack(fill=tkinter.BOTH, expand=1)

if __name__ == "__main__":
    application = LabelFrame()
    application.mainloop()
