# Check in #1 Branching
# REDACTED(I <3 not doxxing myself)
# Ask a person for their month of birth and the month of birth of their friend(both in integer format). 
# If the months are the same, the program should print that the months are the same and if not, print that the months are not the same
# If the input is invalid, print that this is an invalid month and not allow any further input

# Get the person's birth month as input from the user and convert it to an integer
month1 = int(input("Please enter your month of birth as a number from 1-12:"))
# Check if the month the user entered is valid(within 1-12, inclusive)
if month1 > 0 and month1 < 13:
    # Get their friend's birth month as input from the user and convert it to an integer
    month2 = int(input("Please enter your friend's month of birth as a number from 1-12:"))
    # Check if the second month the user entered is valid(within 1-12, inclusive)
    if month2 > 0 and month2 < 13:
        # If both months are valid and the months are equal,
        if month1 == month2:
            # Print that the birth months are the same
            print("You have the same birth month.")
        # If both months are valid but the months are not equal,
        else:
            # Print that the birth months are different
            print("You have different birth months.")
    # If the second month the user entered is invalid
    else:
        # Print that the month is not valid and do not continue with the program
        print('This is not a valid month.')
# If the first month is invalid,
else:
    # Print that the month is not valid and do not allow any further input
    print("This is not a valid month.")

# Test cases
"""
Please enter your month of birth as a number from 1-12: -3
This is not a valid month
"""
"""
Please enter your month of birth as a number from 1-12: 3 
Please enter your friend's month of birth as a number from 1-12: -5
This is not a valid month.
"""
"""
Please enter your month of birth as a number from 1-12: 6
Please enter your friend's month of birth as a number from 1-12: 6
You have the same birth month.
"""
"""
Please enter your month of birth as a number from 1-12: 5
Please enter your friend's month of birth as a number from 1-12: 8
You have different birth months.
"""
"""
Please enter your month of birth as a number from 1-12: 13
This is not a valid month
"""
"""
Please enter your month of birth as a number from 1-12: 7
Please enter your friend's month of birth as a number from 1-12: 13
This is not a valid month.
"""
"""
Please enter your month of birth as a number from 1-12: 0
This is not a valid month.
"""
"""
Please enter your month of birth as a number from 1-12: 5
Please enter your friend's month of birth as a number from 1-12: 0
This is not a valid month.
"""
"""
Please enter your month of birth as a number from 1-12: 1
Please enter your friend's month of birth as a number from 1-12: 4
You have different birth months.
"""