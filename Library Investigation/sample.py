# P1.0 Library Investigation sample code
# REDACTED, REDACTED, REDACTED(I <3 not doxxing myself)
# Sample code demonstrating the primary functionality of the Tkinter python libary which is used to make graphical
# user interfaces. Documentation: https://tkdocs.com/tutorial/

# Import the base tkinter functions and the widgets
from tkinter import *
from tkinter import ttk


# Create the base Tkinter window, will serve as the root / absolute master object
window = Tk()

# Create variables for the first + last name, the value of these can be fetched or set at any point by running
# variablename.get() or variablename.set("new value") respectively
firstname = StringVar()
lastname = StringVar()
# Function that will be executed when the first button is clicked
def Button1Click():
    print("Button 1 clicked")
# Function that will be executed when the print name button is clicked
def PrintNameClick():
    if var1.get():
        print(firstname.get(), end=" ")
    if var2.get():
        print(lastname.get())
    if var1.get() and not var2.get():
        print()
# Set window size to 1000 pixels wide and 500 pixels high
window.geometry("1000x500")
# Add a button and call Button1Click when it is clicked, using a grid formation to place it on screen
Button(window, bg='DarkOrange1', text="Testing button 1", command=Button1Click).grid()
Button(window, bg='DarkOrange1', text="Print name",command=PrintNameClick).grid()
# Create a label and use grid formation for placement on screen
Label(window, text="First name:").grid()
# Create a text input where the user can enter text, the value of the input here is stored in the firstname variable
Entry(window, textvariable=firstname).grid()
Label(window, text="Last name:").grid()
Entry(window, textvariable=lastname).grid()
# Create a new frame and store it in the frame1 variable(not yet placed on screen)
frame1 = Frame(window)
# Set the border width of the frame to 2 pixels
frame1['borderwidth'] = 2
# Set the border of the frame to solid
frame1['relief'] = 'solid'
# Create a label inside of the frame and use a grid formation to place it on screen
#ttk.Label(frame1, text="Framed text").grid()
# Place the frame on the screen using a grid formation
frame1.grid()
# Create a new button to show a drop down menu
menubutton = Menubutton(frame1, text = "Name Select Menu", bg='gold')
# Instatiating the otions in the menu and assigning them to the open menu button
menubutton.menu = Menu(menubutton)
menubutton["menu"]= menubutton.menu
# Varaibles for each checkbutton that can be fetched
var1 = IntVar()
var2 = IntVar()
# Adds checkbuttons to the drop down menu that select which names will be printed
menubutton.menu.add_checkbutton(label = "First Name", variable = var1)
menubutton.menu.add_checkbutton(label = "Last name", variable = var2)
# packs the menubutton into the frame
menubutton.pack()
# Main process of running the GUI, this is always required
window.mainloop()

