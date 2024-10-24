from tkinter import *
class entryKeyWin(Toplevel):
    keyEntry = None
    def __init__(self, parent, title) :
        super().__init__(parent)

        self.keyEntry = Entry(self, font=("Veranda", 18), show = ":)")
        self.keyEntry.configure(width = 28)
        self.keyEntry.pack(pady= 16)
        self.keyEntry.configure(bg = "#0D0D0D", fg = "green", border=0)
        
        self.title(title)
        self.geometry("400x90")
        self.resizable(False, False)
        self.configure(bg = "#0D0D0D")