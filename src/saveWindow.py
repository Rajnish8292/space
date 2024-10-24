from tkinter import *
from src.encANDdec import *
class saveWindow(Toplevel):
    keyEntry = None
    __keyShow_btn = None
    def __init__(self, parent, title, txt, key):
        super().__init__(parent)
        self.keyEntry = Entry(self, font=("Veranda", 18), show = "*")
        self.keyEntry.configure(width = 28)
        self.keyEntry.pack(pady= 16)
        self.keyEntry.configure(bg = "#0D0D0D", fg = "green", border=0)
        self.keyEntry.focus()
        self.title(title)
        self.geometry("400x90")
        self.resizable(False, False)
        self.configure(bg = "#0D0D0D")
        self.isKey_showing = False
        def show_key():
            if(self.isKey_showing):
                self.isKey_showing = False

                self.keyEntry.configure(show = "*")
                # print("key not showing")
            else :
                self.isKey_showing = True
                self.keyEntry.configure(show = "")
                # print("key is showing")


        keyShow_btn = Button(self, text = "o-o", command = show_key)
        keyShow_btn.configure(bg = "green", fg = "#0D0D0D", border=0)
        keyShow_btn.pack(pady = 5)
        def keyPress(e):

            if(e.keycode == 13):
                cipher_txt = encryption(txt, self.keyEntry.get())
                f = open("resource/data/{}.txt".format(title), "w")
                f.write(cipher_txt)
                f.close()
                self.destroy()
                parent.destroy()
            elif(e.keycode == 27):
                self.destroy()

        self.bind("<KeyPress>", keyPress)



