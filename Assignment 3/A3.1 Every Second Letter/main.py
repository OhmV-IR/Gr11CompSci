# A3.1 Every Second Letter
# REDACTED(I <3 not doxxing myself)
# Get a string from the user and print every other letter of that string

# Infinite loop
while True:
    # Try to get a string from the user
    try:
        # Get a string from the user
        inputString = input("Please enter a string:")
    # If getting a string from the user fails
    except:
        # Print that the string is invalid
        print("This is not a valid string.")
    # If getting a string from the user is successful
    else:
        # If the string is blank
        if inputString == "":
            # Print that the string cannot be blank(null) and loop again to get new input
            print("The string cannot be blank.")
        # If the string is not blank
        else:
            # Exit the input loop and move to the main function of the program
            break

# Get every other letter of the string by stripping from the start to the end of the string with a step of 2 and store it in a new string
newString = inputString[::2]
# Print the new string with every other letter of the original string
print(newString)

# Test cases
"""
Please enter a string: 
The string cannot be blank.
Please enter a string: abc
ac
"""
"""
Please enter a string: hello this is a big sentence for testing purposes
hloti sabgsnec o etn upss
"""
"""
Please enter a string: 1234567890
13579
"""
"""
Please enter a string: :) !@ 32134 smiley faces are cool
: @314sie ae r ol
"""
