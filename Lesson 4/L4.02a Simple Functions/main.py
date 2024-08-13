# L4.02a Simple Functions
# REDACTED(I <3 not doxxing myself)
# Get 2 integers from the user and display all the integers from highest to lowest

# Define a new function to get an integer input from the user
def GetIntInput():
    # Infinite loop
    while True:
        # If converting the user's input into an integer fails, the program will not crash
        try:
            # Get an input from the user and try to convert it to an integer
            num1 = int(input("Please enter an integer:"))
        # If converting the user's input to an integer fails
        except:
            # Print that the integer is invalid and loop again to get new input
            print("This is not a valid integer")
        # If converting the user's input into an integer is successful
        else:
            # Return the integer as a result of this function
            return num1
# Get 2 integers from the user using the function we defined above
num1 = GetIntInput()
num2 = GetIntInput()

# If the first number is bigger than the second
if num1 > num2:
    # Print the first number first and the second one after
    print(num1)
    print(num2)
# If the second number is bigger than the first
else:
    # Print the second number first and the first one after
    print(num2)
    print(num1)

# Test cases
"""
Please enter an integer:1
Please enter an integer:2
2
1
"""
"""
Please enter an integer:abc
This is not a valid integer
Please enter an integer:32
Please enter an integer:sdjf
This is not a valid integer
Please enter an integer:45
45
32
"""
"""
Please enter an integer:!#2
This is not a valid integer
Please enter an integer:2
Please enter an integer:((*)1
This is not a valid integer
Please enter an integer:1
2
1
"""