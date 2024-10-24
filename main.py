from tkinter import * 
import tkcalendar
from tkcalendar import Calendar
import json
from src.stringMethod import * # contains method for split and replace
from datetime import *
from src.encryptionWindow import entryKeyWin
from src.space import space
# from src.codeWindow import codeWindow
app_detail_data = open("intro.json").read() # load file "intro.json"
app_detail = json.loads(app_detail_data) # parse json format to dict format

# main window
root = Tk()
# keyWin = None
# widgets
today = datetime.now()
# calendar widget
cal = Calendar(root, selectmode = 'day', year = today.year, month = today.month, day = today.day,)
cal.config()
cal.pack()
cal.configure(background = "#0D0D0D", foreground = "green", bordercolor = "green", headersbackground = "green", headersforeground = "black", selectbackground = "green", selectforeground = "black", disabledselectbackground = "#00cc00", disabledselectforeground = "black",normalbackground = "#0D0D0D", normalforeground = "green", othermonthbackground = "#0D0D0D", othermonthforeground="#0D0D0D", othermonthweforeground = "#0D0D0D", othermonthwebackground = "#0D0D0D", weekendbackground = "#0D0D0D", weekendforeground = "green", tooltipbackground = "green")

# print present date selecton on calendar widget on  terminal
def printDate():
    # global keyWin
    date = str(cal.selection_get())
    keyWin = entryKeyWin(root, date)
    keyWin.keyEntry.focus()
    def destroKeyWin(e):
        if(e.keycode == 27):
            keyWin.destroy()
        elif(e.keycode == 13):
            new_space = space(root, date, date, keyWin.keyEntry.get())
            keyWin.destroy()

    keyWin.bind("<KeyPress>", destroKeyWin)



# key press when focus on main window 
def rootKeyPress(e):
    # print(e.keycode)
    if (e.keycode == 13) :
        printDate()
    elif (e.keycode == 27) : 
        root.destroy()
    elif (e.keycode == 17) :
        new_codeWindow = codeWindow(root)
        print("ctrl button clicked!")

# load button
btn = Button(root, text = "Load",height = 30, width =30, command=printDate)
btn.pack(pady = 40)
btn.configure(bg = "green", fg = "black")

# configure main window setting 
root.title(app_detail["name"] + " " + str(app_detail["version"]))
root.geometry("500x300")
root.resizable(False, False) # disable resizing of main window
root.configure(bg = "#0D0D0D")
root.bind("<KeyPress>", rootKeyPress) # bind event with main window
mainloop() # display all content above it

print("program exit!")