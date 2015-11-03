#!/usr/bin/env python3

'''
The Frame is similar to a LabelFrame, however it lacks the label component on
the top edge. It is used to group widgets in a related group.
'''

import tkinter

class Frame(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Frame")
        self.geometry("200x200")

        frame = tkinter.Frame(padx=10, pady=10)
        frame.pack(fill=tkinter.BOTH, expand=1)

        label = tkinter.Label(frame, text="This Label is packed\nwithin the Frame.")
        label.pack(fill=tkinter.BOTH, expand=1)

if __name__ == "__main__":
    application = Frame()
    application.mainloop()
