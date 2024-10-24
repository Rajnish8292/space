from tkinter import *
from src.encANDdec import *
from src.saveWindow import *
class space(Toplevel):
    name = None
    __key = None

    __decipher_txt = None
    def __init__(self, parent, title, name ,encryption_key):
        super().__init__(parent)
        self.title(title)
        self.name = name

        __key = encryption_key
        f = open("resource/data/{}.txt".format(name), "a")
        f.close()

        f = open("resource/data/{}.txt".format(name), "r")
        __decipher_txt = decryption(f.read(), __key)
        f.close()
        container = Text(self, fg = "green", bg = "#0D0D0D", font =("Courier", 14), cursor="arrow")
        container.pack(fill = BOTH, expand=True)
        container.focus()
        # print("decipher text", __decipher_txt)
        container.insert(END, __decipher_txt)
        def keyPress(e):
            # print(e.keycode)
            if(e.keycode == 17):
                #encrypt and save text
                # print(container.get("1.0", END))
                save_window = saveWindow(self, title, container.get("1.0", END), __key)
                # self.destroy()
                pass
            elif(e.keycode == 27):
                self.destroy()


        self.bind("<KeyPress>", keyPress)






        


