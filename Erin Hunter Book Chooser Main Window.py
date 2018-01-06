# Copyright (C) 2016 - 2018 Dog Face Development Company

from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.iconbitmap("favicon.ico")
window.title("Erin Hunter Book Chooser")

# Text Window
label = Label( window, font = ("architects daughter", 11, "normal"), text = "Welcome to the Erin Hunter Book Chooser.\nPlease select your favorite animal below and the app will select your favorite Erin Hunter authored book.\n You can visit the website link displayed to learn more afterwards.")
            
label.pack( padx = 200, pady = 25 )

# --------------------------------------------------------
frame = Frame(window)

book = StringVar()

# Radio Buttons
radio_1 = Radiobutton( frame, font = ("architects daughter", 10, "normal"), text='Cats', \
                               variable = book, value = 'Warriors by Erin Hunter.\nVisit warriorcats.com for more information.')
radio_2 = Radiobutton( frame, font = ("architects daughter", 10, "normal"), text='Bears', \
                               variable = book, value = 'Seekers by Erin Hunter.\nVisit seekerbears.com for more information.')
radio_3 = Radiobutton(frame, font = ("architects daughter", 10, "normal"), text='Dogs', \
                                variable = book, value = 'Survivors by Erin Huter.\nVisit survivorsdogs.com for more information.')
radio_4 = Radiobutton( frame, font = ("architects daughter", 10, "normal"), text='Lions', \
                                variable = book, value = 'Bravelands by Erin Hunter.\nVisit warriorcats.com/bravelands for more information.')
radio_5 = Radiobutton( frame, font = ("architects daughter", 10, "normal"), text='Elephants', \
                                variable = book, value = 'Bravelands by Erin Hunter.\nVisit warriorcats.com/bravelands for more information. ')
radio_6 = Radiobutton( frame, font = ("architects daughter", 10, "normal"), text='Baboons', \
                                variable = book, value = 'Bravelands by Erin Hunter.\nVisit warriorcats.com/bravelands for more information.  ')

radio_1.select()

# Make a dialog box apear
def dialog():
    box.showinfo('Erin Hunter Book Selection', \
                 'Your Erin Hunter Book selection is: ' + book.get() )

# Radio Button button
btn = Button( frame, font = ("architects daughter", 10, "normal"), text = 'Choose', command = dialog)


# Pack statements
btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
radio_4.pack(side = LEFT)
radio_5.pack(side = LEFT)
radio_6.pack(side = LEFT)
frame.pack( padx = 30, pady = 15 )

window.mainloop()
    
