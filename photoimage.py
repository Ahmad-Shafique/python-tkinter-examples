#!/usr/bin/env python3

'''
The PhotoImage widget allows images in the gif format to be displayed within the
Tkinter application.
'''

import tkinter

class PhotoImage(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("PhotoImage")

        photoimage = tkinter.PhotoImage(file="tkinter.gif")

        label = tkinter.Label(image=photoimage)
        label.image = photoimage
        label.pack()

if __name__ == "__main__":
    application = PhotoImage()
    application.mainloop()
