from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Erin Hunter Book Chooser")

label = Label( window, text = "Welcome to the Erin Hunter Book Chooser.\nPlease choose your favorite animal and the app will select your most likely favorite book written by Erin Hunter.\n You can visit the website link displayed to learn more.\n\nClick the X button to continue!")
            
label.pack( padx = 300, pady = 100 )

import mainchoice

window.mainloop()
    
