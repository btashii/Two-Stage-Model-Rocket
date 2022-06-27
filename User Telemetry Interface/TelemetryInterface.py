from Tkinter import *
import time
import random
#used to have PIL (pillow)
#can import Raspberry functions here
import Tkinter as tk #Tkinter is renamed tk
print(tk.TkVersion)

#GENERAL NOTES
#Tkinter has a main loop keeping the window open. Can't use timer.sleep.
#In python, functions are defined by "def". They can include parameters.
#Calling this program: cd Desktop and python PythonGUI.test

#QUESTIONS/CONCERNS
#Why is label['text'] = count?
#Why is root = tk.Tk()?
#Why is Tk() after tk. ? Hypothesis: Tk() is an function name which calls the window itself


#python PythonGUI.test


root = tk.Tk() #call Tk itself and loop the main window so it stays up *very important*


time1 = ''
#clock function
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text= time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)


label = tk.Label(font = (None, 35))
label.place(relx=0.8, rely=0.2, anchor = CENTER)
label.config(fg = "black")

#status function

self = ''

def buttonClick(button_id):
    if button_id == 1:
        inside_status['text'] = "Countdown Initiated"
        # call countdown first time
        countdown(10, 0)
# root.after(0, countdown, 5)
    elif button_id == 2:
        inside_status['text'] = "Countdown Terminated"

#procedure has parameter count
def countdown(count,*,button_id):
    # change text in label
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    elif button_id2 == 2:
        return

#you can change font by doing font(family, size, style)
#The .config width and height only changes the padding(similiar to HTML)
#You can find the relative middle by using rely and relx = 0.5

label2 = tk.Label(text = "Mission Control", font = (None, 35))
label2.config(fg = "black", bg = "grey", width = 12, height = 1)
label2.place(relx=0.5, rely=0.1, anchor=CENTER)

clock = tk.Label(font = (None, 35))
clock.config(fg = "black")
clock.place(relx=0.3, rely=0.2, anchor=CENTER)

timestringlabel = tk.Label(text = "Time:",font = (None, 35))
timestringlabel.config(fg = "black")
timestringlabel.place(relx=0.2, rely=0.2, anchor=CENTER)

timestringlabel = tk.Label(text = "T-Minus:",font = (None, 35))
timestringlabel.config(fg = "black")
timestringlabel.place(relx=0.7, rely=0.2, anchor=CENTER)

button_white_png = PhotoImage(file = "white.gif")


startbutton = tk.Button(text = "START",font = (None, 30), image = button_white_png, compound = "center", command = lambda: [buttonClick(1)])
startbutton.place(relx=0.7, rely= 0.3, anchor=CENTER)
startbutton.config(width = 89, height = 35)

abortbutton = tk.Button(text = "ABORT",font = (None, 30), image = button_white_png, compound = "center", command = lambda: [buttonClick(2, 2)])
abortbutton.place(relx=0.8, rely= 0.3, anchor=CENTER)
abortbutton.config(width = 89, height = 35)


#status widget

label2 = tk.Label()
label2.config(bg = "grey", width = 25, height = 8)
label2.place(relx=0.50, rely=0.3, anchor=CENTER)

label2 = tk.Label()
label2.config(text = "Status", bg = "red", compound = "center")
label2.place(relx=0.50, rely=0.23, anchor=CENTER)


#stuff inside the status widget

inside_status = tk.Label()
inside_status.config(fg = "red", bg = "grey")
inside_status.place(relx=0.5, rely=0.3, anchor=CENTER)



#YOU HAVE TO CONVERT ALL IMAGES TO GIFS!


button = tk.Button(root, font=('Helvetica', '50'), image = button_white_png, bg = "red")
button.grid(row = 2, column = 0)
button.config(width = 50, height = 50)

root.geometry("2560x1600")
root.configure(background='white')


tick()
root.mainloop()
