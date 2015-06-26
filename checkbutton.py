#!/usr/bin/env python3

'''
An example of a Checkbutton contained within a Window, which when clicked
displays a message indiciating the current Checkbutton state.
'''

import tkinter

class CheckButton(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("CheckButton")

        self.checkbuttonvar = tkinter.IntVar()

        checkbutton = tkinter.Checkbutton(text="Checkbutton",
                                          variable=self.checkbuttonvar,
                                          command=self.on_checkbutton_click)
        checkbutton.select()
        checkbutton.pack(fill=tkinter.BOTH, expand=1)

    def on_checkbutton_click(self):
        if self.checkbuttonvar.get() == 1:
            print("Checkbutton selected")
        else:
            print("Checkbutton not selected")

if __name__ == "__main__":
    application = CheckButton()
    application.mainloop()
