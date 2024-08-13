# L1.6 Tall Person
# REDACTED(I <3 not doxxing myself)
# Given a person's height, print whether they are very tall or not

# Get an integer input from the user as the person's height
height = int(input("Please enter a height(cm):"))
# If the height is 0 or negative,
if height < 1:
    # Print that the height is invalid
    print("This is not a valid height.")
# If the person is over 200cm tall,
elif height > 200:
    # Print that the person is very tall
    print("This person is very tall.")
# If the person is between 1 and 200cm tall
else:
    # Print that the person is not very tall
    print("This person is not very tall.")

# Test cases
"""
Please enter a height(cm): 95
This person is not very tall.
"""
"""
Please enter a height(cm): 216
This person is very tall.
"""
"""
Please enter a height(cm): 0
This is not a valid height.
"""
"""
Please enter a height(cm): -76
This is not a valid height.
"""