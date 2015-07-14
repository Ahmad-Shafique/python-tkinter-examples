#!/usr/bin/env python3

'''
Showing a progressbar example from the ttk submodule, with start and stop
buttons to operate the progress functionality.
'''

import tkinter, tkinter.ttk

class Progressbar(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Progressbar")

        self.progressbar = tkinter.ttk.Progressbar()
        self.progressbar.config(maximum=10)
        self.progressbar.pack()

        button = tkinter.Button(text="Start", command=self.on_start_button_clicked)
        button.pack()

        button = tkinter.Button(text="Stop", command=self.on_stop_button_clicked)
        button.pack()

    def on_start_button_clicked(self):
        self.progressbar.start(1000)

    def on_stop_button_clicked(self):
        self.progressbar.stop()

if __name__ == "__main__":
    application = Progressbar()
    application.mainloop()
