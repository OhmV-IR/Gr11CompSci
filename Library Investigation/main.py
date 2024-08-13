# P1.0 Library Investigation
# REDACTED, REDACTED, REDACTED(I <3 not doxxing myself)
# Challenge criteria:
# - Must be able to add any text into any box
# - Must be able to reference the value of any box by typing it's coordinate number using the coordinate system
# - Must be able to perform additions using multiple boxes of data, accounting for possible incorrect inputs(just not crashing)
# - Must be able to add more rows/columns upon user input, implementing a scrollbar if needed
# - OPTIONAL: Save the table to a file and be able to load the saved table from the file again

from tkinter import * # primary intialization / base components of tkinter
from tkinter import ttk # widgets/modules of tkinter

# Get a grid value from it's row and column coordinates
def GetGridValue(r, c):
    # Get the object that it is in the row/column position provided
    data = spreadsheetFrame.grid_slaves(row=r, column=c)
    # If the value of the box has never been set before, the variable will not have been instantiated and this will crash
    try:
        # Get the name of the text variable by using the textvariable property of the entry
        varname = data[0].cget('textvariable')
        # Print the value of the variable by getting the value from the name
        return data[0].getvar(varname)
    # If the value of the box has never been set before
    except:
        # Return no value
        return "0"
    
# Set the value of a box on the grid given the row/column coordinates and the new value to set
def SetGridValue(r, c, val):
    # Get the object that is at the provided row/column coordinates
    data = spreadsheetFrame.grid_slaves(row=r, column=c)
    # Get it's textvariable attribute
    varname = data[0].cget('textvariable')
    # Set the value of the variable to the new value
    data[0].setvar(varname, val)

# Print the entire grid of values to the console
def PrintGrid():
    # Get grid size int [columns,rows] format
    gridsize = spreadsheetFrame.grid_size()
    # For every row
    for a in range(0,gridsize[1]):
        # For every column in that row,
        for b in range(0,gridsize[0]):
            # Print the coordinates of the box
            print("Box at coordinates", a, ",", b)
            # Get the entry from the row column coordinates
            data = spreadsheetFrame.grid_slaves(row=a, column=b)
            # If the box value has not been set yet, this will crash
            try:
                # Get the name of the text variable by using the textvariable property of the entry
                varname = data[0].cget('textvariable')
                # Print the value of the variable by getting the value from the name
                print(data[0].getvar(varname))
            # If the box value has not been set yet,
            except:
                # Print no value
                print("0")

# Whenever an entry is changed, this function will be called with the new value of the variable and the operation that was performed on it
def EntryChanged(newvalue, operation):
    # There are many things that could go wrong in parsing the formula, so we just encase this in a try/except to prevent crashes
    try:
        # Turn the new value into a list of characters
        newval = list(newvalue)
        # If we left the cell(don't want to try and parse a formula that we're halfway through typing)
        if operation == "focusout":
            # If the first character is an equal sign
            if newval[0] == '=':
                # Debug logging
                print("Attempted to process formula:", newvalue)
                # For every character in the new value
                for i in range(0,len(newval)):
                    # If the current character is an opening bracket
                    if newval[i] == '(':
                        # Move to the next character
                        i = i + 1
                        # Initialize lists which will contain the digits of the row/column coordinates
                        rowChars = []
                        columnChars = []
                        # Infinite loop
                        while True:
                            # If we reach the comma seperating the row and column number, exit the loop
                            if newval[i] == ',':
                                break
                            # Otherwise, add the character to the list of digits representing the row number
                            else:
                                rowChars.append(newval[i])
                                # Increment i to move to the next character
                                i = i + 1
                        # Increment i to move past the comma
                        i = i + 1
                        # Infinite loop
                        while True:
                            # If we hit the closing bracket that ends the coordinates, break out of the loop
                            if newval[i] == ')':
                                break
                            # Otherwise, add the character to the list of digits for the column number
                            else:
                                columnChars.append(newval[i])
                                # Increment i to move to the next character
                                i = i + 1
                        # If this is not the end of the formula,
                        if i + 1 < len(newval):
                            # Increment i to move to the next character
                            i = i + 1
                            # If the formula is a sum of multiple cells
                            if newval[i] == ':':
                                # Get the starting row number as a string by forming all the characters of it into a string
                                startingRowStr = "".join(rowChars)
                                # Get the starting column number as a string by forming all the characters of it into a string
                                startingColumnStr = "".join(columnChars)
                                # Increment i by 2 to get to the start of the row number
                                i = i + 2
                                # Initiailize lists that will make up the digits of the ending row/column numbers
                                endingRowChars = []
                                endingColumnChars = []
                                # Infinite loop
                                while True:
                                    # If we reach the comma that seperates the row and column numbers, break out of the loop
                                    if newval[i] == ',':
                                        break
                                    # Otherwise, add the current character to the digits of the row
                                    else:
                                        endingRowChars.append(newval[i])
                                        # Increment i to move to the next character
                                        i = i + 1
                                # Increment i to move to the start of the column number
                                i = i + 1
                                # Infinite loop
                                while True:
                                    # If we reach the end of the column number, break
                                    if newval[i] == ')':
                                        break
                                    # Otherwise, add the current character to the digits of the column number
                                    else:
                                        endingColumnChars.append(newval[i])
                                        # Increment i to move to the next character
                                        i = i + 1
                                # Initialize a total that starts at 0
                                total = 0
                                # Convert the lists of characters to strings by joining all the characters together
                                endingRowStr = "".join(endingRowChars)
                                endingColumnStr = "".join(endingColumnChars)
                                # For every row that is included in the formula
                                for a in range(int(startingRowStr), int(endingRowStr) + 1):
                                    # For every column that is included in the formula
                                    for b in range(int(startingColumnStr), int(endingColumnStr) + 1):
                                        # Add the value of that cell to the total
                                        total = total + float(GetGridValue(a,b))
                                # Get the size of the grid
                                gridsize = spreadsheetFrame.grid_size()
                                # For every row in the grid,
                                for a in range(0,gridsize[1]):
                                    # For every column in the grid,
                                    for b in range(0,gridsize[0]):
                                        # If the grid value of the current cell is equal to the formula that we parsed
                                        if GetGridValue(a,b) == newvalue:
                                            # Set the value of that cell to the total
                                            SetGridValue(a,b, total)
                                            # Stop parsing the formula any further
                                            return True
                            # If the formula does not have a semicolon after the coordinates
                            else:
                                # Join the digits of the row number
                                rowStr = "".join(rowChars)
                                # Join the digits of the column number
                                columnStr = "".join(columnChars)
                                # Get the size of the full grid
                                gridsize = spreadsheetFrame.grid_size()
                                # For every row,
                                for a in range(0,gridsize[1]):
                                    # For every column
                                    for b in range(0,gridsize[0]):
                                        # If the value of the current cell is equal to the value of the formula we tried to parse
                                        if GetGridValue(a, b) == newvalue:
                                            # Set the grid value of the current cell to the value of the cell with the coordinates provided in the formula
                                            SetGridValue(a,b, GetGridValue(int(rowStr), int(columnStr)))
                                            # Stop parsing the formula any further
                                            return True
                        # If the formula ends      
                        else:
                            # Get the row/column number by joining all the digits
                            rowStr = "".join(rowChars)
                            columnStr = "".join(columnChars)
                            # Get the total grid size
                            gridsize = spreadsheetFrame.grid_size()
                            # For every row,
                            for a in range(0,gridsize[1]):
                                # For every column
                                for b in range(0,gridsize[0]):
                                    # If the grid value of the current cell is equal to the formula that we parsed
                                    if GetGridValue(a, b) == newvalue:
                                        # Set the value of that cell to the value of the cell provided in the coordinates
                                        SetGridValue(a,b, GetGridValue(int(rowStr), int(columnStr)))
                                        # Stop parsing the formula any further
                                        return True
    # If parsing the formula fails
    except:
        # Stop parsing the formula any further
        return False
    # If there is no formula to be parsed, return true     
    return True
# Add a new cell at the provided row/column coordinates
def AddNewCell(r,c):
    # Create a new entry in the spreadsheet frame using the row column coordinates and create a new string variable for it's value
    # Add the EntryChanged function as the validation function so that it is called when the vlaue is changed to parse any formulas
    ttk.Entry(spreadsheetFrame, textvariable=StringVar(spreadsheetFrame), validate="all", validatecommand=entryChangedWrapper).grid(row=r, column=c, sticky=W)
# Add a column to the table
def AddColumn():
    # Get the total size of the grid
    gridsize = spreadsheetFrame.grid_size()
    # Enforce a maximum number of columns to prevent them from going off-screen
    if gridsize[0] < 6:
        # For every row, starting at the top row
        for i in range(gridsize[1],0,-1):
            # Add a row using the current row in the new column(column is 0-indexed so the column size is the new index)
            AddNewCell(gridsize[1] - i, gridsize[0])
    # Add a row to the table
def AddRow():
    # Get the total size of the grid
    gridsize = spreadsheetFrame.grid_size()
    # Enforce a maximum number of rows to prevent them from going off-screen
    if gridsize[1] < 20:
        # For every column, starting at the left-most column
        for i in range(gridsize[0], 0, -1):
            # Add a new cell using the new row(row is 0-indexed so the row size is the new index) and the current column
            AddNewCell(gridsize[1], gridsize[0] - i)
# Create the main window
window = Tk()
# Using a resolution of 1000 pixels wide and 500 pixels tall
window.geometry('1000x500')
# Set the title of the window to excel speedsheet
window.title("Excel speedsheet")
entryChangedWrapper = (window.register(EntryChanged), '%P', '%V')
# Add buttons to the main window
ttk.Button(window, text="Print grid values", command=PrintGrid).grid(row=0, column=0)
ttk.Button(window, text="Add column", command=AddColumn).grid(row=1, column=0)
ttk.Button(window, text="Add row", command=AddRow).grid(row=2, column = 0)
# Create the spreadsheet frame and make it a child of the main window
spreadsheetFrame = ttk.Frame(window)
# Render the spreadsheet frame
spreadsheetFrame.grid(row=3, column=1)
# Add a starting entry
AddNewCell(0,0)
# Tkinter loop, pops up the GUI and keeps the program running
window.mainloop()