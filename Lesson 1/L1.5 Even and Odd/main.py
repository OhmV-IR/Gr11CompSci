# L1.5 Even and Odd
# REDACTED(I <3 not doxxing myself)
# Get an integer input from the user and print whether it is odd or even

# Get an integer input from the user
value = int(input("Enter an integer:"))
# If the remainder of dividing the integer by 2 is zero,
if(value % 2 == 0):
    # Print that the integer is even
    print("The integer is even.")
# If the integer is not even, it must be odd
else:
    # Print that the integer is odd
    print("The integer is odd.")

# Test cases
"""
Enter an integer: 2
The integer is even.
"""
"""
Enter an integer: 7
The integer is odd.
"""
"""
Enter an integer: -6
The integer is even.
"""
"""
Enter an integer: -3
The integer is odd.
"""