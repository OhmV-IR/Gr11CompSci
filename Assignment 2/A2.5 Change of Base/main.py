# A2.5 Change of Base
# REDACTED(I <3 not doxxing myself)
# Divide number by base repeatedly until you get to 1 and store the remainders, the converted number is the remainders in reverse order

# Infinite loop
while True:
    # Prevent the program from crashing if the user enters an invalid input
    try:
        # Get the number in base 10 from the user and convert it to an integer
        base10Num = int(input("Please enter a number in base 10:"))
        # Get the base the user wants to conver the number to and convert it to an integer
        base = int(input("Please enter a new base within 2-9(inclusive):"))
    # If an error occurs when trying to convert a user input to an integer
    except ValueError:
        # Print that the input is invalid and loop again to get new input
        print("This is not a valid input")
    # If the user's input is successfully converted to integers
    else:
        # If the base the user entered is outside of the allowed range
        if base < 2 or base > 9:
            # Print that the input is invalid and loop again to get new input
            print("This is not a valid input")
        # If the base 10 number the user entered is less than 0
        elif base10Num < 0:
            # Print that the number must be positive and loop again to get new input
            print("The number must be positive")
        # If the input is valid
        else:
            # Exit the infinite loop and move to the main function of the program
            break

# Create a new variable to use to store the new number that we will divide by every time, start by dividing the number given
newNum = base10Num
# Create a new array to store the remainders of the division in
remainders = []
# Infinite loop
while True:
    # Add the remainder of dividing the number that we are dividing by the by the base to the array
    remainders.append(newNum % base)
    # The number we will divide in the next run is the floor of dividing the current number by the base
    newNum = int((newNum - remainders[len(remainders) - 1]) / base)
    # Once we reach zero(the number has been fully divided out)
    if newNum == 0:
        # Exit the infinite loop
        break
# Reverse the remainders to get the number in the new base
remainders.reverse()
# Print the result
print(str(base10Num) + " in base " + str(base) + " is " , end="")
print(*remainders, sep="")

# Test cases
"""
Please enter a number in base 10: 62
Please enter a new base within 2-9(inclusive): 2
62 in base 2 is 111110
"""
"""
Please enter a number in base 10: 667
Please enter a new base within 2-9(inclusive): 3
667 in base 3 is 220201
"""
"""
Please enter a number in base 10: 11573
Please enter a new base within 2-9(inclusive): 4
11573 in base 4 is 2310311
"""
"""
Please enter a number in base 10: 2024
Please enter a new base within 2-9(inclusive): 5
2024 in base 5 is 31044
"""
"""
Please enter a number in base 10: 844012
Please enter a new base within 2-9(inclusive): 6
844012 in base 6 is 30031244
"""
"""
Please enter a number in base 10: 4
Please enter a new base within 2-9(inclusive): 7
4 in base 7 is 4
"""
"""
Please enter a number in base 10: 862
Please enter a new base within 2-9(inclusive): 8
862 in base 8 is 1536
"""
"""
Please enter a number in base 10: 9999
Please enter a new base within 2-9(inclusive): 9
9999 in base 9 is 14640
"""
"""
Please enter a number in base 10: 1234
Please enter a new base within 2-9(inclusive): 1
This is not a valid input
Please enter a number in base 10: 5555
Please enter a new base within 2-9(inclusive): 5
5555 in base 5 is 134210
"""
"""
Please enter a number in base 10: 72
Please enter a new base within 2-9(inclusive): 10
This is not a valid input
Please enter a number in base 10: 72
Please enter a new base within 2-9(inclusive): 10
This is not a valid input
Please enter a number in base 10: 72
Please enter a new base within 2-9(inclusive): 2
72 in base 2 is 1001000
"""
"""
Please enter a number in base 10: abc
This is not a valid input
Please enter a number in base 10: def
This is not a valid input
Please enter a number in base 10: 18
Please enter a new base within 2-9(inclusive): 9
18 in base 9 is 20
"""
"""
Please enter a number in base 10: 15
Please enter a new base within 2-9(inclusive): h
This is not a valid input
Please enter a number in base 10: 18
Please enter a new base within 2-9(inclusive): i
This is not a valid input
Please enter a number in base 10: 13
Please enter a new base within 2-9(inclusive): 2
13 in base 2 is 1101
"""
