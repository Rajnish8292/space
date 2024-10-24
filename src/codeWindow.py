# from tkinter import *
# from src.historyWindow import historyWindow
# class codeWindow(Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.title("enter keyCode for action : \'s\' , \'h\'")
#         self.geometry("400x90")
#         self.resizable(False, False)
#         self.configure(bg = "#0D0D0D")

#         self.keyCodeEntry = Entry(self, font=("Veranda", 18))
#         self.keyCodeEntry.configure(width = 28)
#         self.keyCodeEntry.pack(pady= 16)
#         self.keyCodeEntry.configure(bg = "#0D0D0D", fg = "green", border=0)
#         self.keyCodeEntry.focus()

#         def keyPress(e):
#             if(e.keycode == 13) :
#                 keyCode_entry = self.keyCodeEntry.get()
#                 if(keyCode_entry == "s"):
#                     print("s key pressed")
#                 elif(keyCode_entry == "h"):
#                     new_historyWindow = historyWindow(parent)
#                     self.destroy()
#                     print("h key pressed")
#                 else:
#                     print("NameError : wrong key entry in codeWindw entry!")
#                     self.keyCodeEntry.delete("0", END)
#             elif (e.keycode == 27):
#                 self.keyCodeEntry.destroy()



#         self.bind("<KeyPress>", keyPress)
