# L3.01 Slices
# REDACTED(I <3 not doxxing myself)
# Take 2 inputs from the user that represent a pair of xy coordinates, and add then to the end of a single list
# that the user terminates by typing 0 for both the x and y coordinates(they should still be added to the list)
# The program should then print a list of all the x coordinates and another list of all the y coordinates(use slices, not loops)

# If the user enters an invalid input, go back to the input stage where it failed
# 0 means x input stage, 1 means y input stage
currentInputStage = 0
# Initialize the list of coordinates
coordList = []
# Loop forever
while True:
    # iF an error occurs, do not crash the program
    try:
        # If the current input stage is 0(x coordinate stage)
        if currentInputStage == 0:
            # Get the x coordinate from the user and try to convert it to a float
            xCoord = int(input("Please enter the x coordinate:"))
            # Add the x coordinate to the list
            coordList.append(xCoord)
            # Set the current input stage to 1(y coordinate stage)
            currentInputStage = 1
        # If the current input stage is 1(y coordinate stage)
        if currentInputStage == 1:
            # Get the y coordinate from the user and try to convert it to a float
            yCoord = int(input("Please enter the y coordinate:"))
            # Add the y coordinate to the list
            coordList.append(yCoord)
            # Set the current input stage to 0(x coordinate stage)
            currentInputStage = 0
    # If an error occurs when converting a value the user inputted to a float
    except ValueError:
        # Print that the input is invalid and loop back to the same input stage where the invalid input was entered
        print("This is not a valid input, please enter a valid number")
    # If no error occurred when converting a value the user inputted to a float
    else:
        # If the user entered zero for both the x and y coordinates
        if(xCoord == 0 and yCoord == 0):
            # Exit the input loop and move to the main function of the program
            break
# Print the coordinate list starting at the beginning up until(but not including) the 2nd last number of the
# list(to exclude the double zeros at the end), skipping every other number to only get the x coordinates
print(coordList[:-2:2])
# Print the coordinate list starting at the 2nd number up until(but not including) the 2nd last number 
# of the list(to exclude the double zeros at the end), skipping every other number to only get the y coordinates
print(coordList[1:-2:2])

# Test cases
"""
Please enter the x coordinate: 1
Please enter the y coordinate: 2
Please enter the x coordinate: 0
Please enter the y coordinate: 0
[1]
[2]
"""
"""
Please enter the x coordinate: 1
Please enter the y coordinate: 2
Please enter the x coordinate: 3
Please enter the y coordinate: a
This is not a valid input, please enter a valid number
Please enter the y coordinate: 2
Please enter the x coordinate: d
This is not a valid input, please enter a valid number
Please enter the x coordinate: 1
Please enter the y coordinate: 5
Please enter the x coordinate: 0 
Please enter the y coordinate: 0
[1, 3, 1]
[2, 2, 5]
"""
"""
Please enter the x coordinate: -4
Please enter the y coordinate: -5
Please enter the x coordinate: 3
Please enter the y coordinate: 2
Please enter the x coordinate: -15
Please enter the y coordinate: 2
Please enter the x coordinate: 0
Please enter the y coordinate: 0
[-4, 3, -15]
[-5, 2, 2]
"""
"""
Please enter the x coordinate: 0
Please enter the y coordinate: 0
[]
[]
"""