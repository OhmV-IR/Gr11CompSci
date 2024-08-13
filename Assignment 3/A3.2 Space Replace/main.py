# A3.2 Space Replace
# REDACTED(I <3 not doxxing myself)
# Take a string as input and replace every third character in the string with a space

# Infinite loop
while True:
    # If getting a string from the user fails, do not crash the program
    try:
        # Get a string from the user
        inputString = input("Please enter a string:")
    # If getting a string from the user fails
    except:
        # Print that the string is invalid and loop again to get new input
        print("Please enter a valid string.")
    # If getting a string from the user is successful
    else:
        # Exit the infinite loop and move to the main function of the program
        break

# Create a new blank string to add the new characters to
newString = ""
# For every character in the string
for i in range(0,len(inputString)):
    # If the current character we are iterating over is a third character
    if (i+1) % 3 == 0:
        # Add a space to the modified string instead of the character
        newString = newString + " "
    # If the current character we are iterating over is not a third character
    else:
        # Add the character to the modified string
        newString = newString + inputString[i]
# Print the modified string after every 3rd character has been replaced with a space
print(newString)

# Test cases
"""
Please enter a string: heyatestingsentence
he at st ng en en e
"""
"""
Please enter a string: 1234567890
12 45 78 0
"""
"""
Please enter a string:!@#$%^ special characters
!@ $%  s ec al ch ra te s
"""
"""
Please enter a string:test cases are amazing!11!
te t  as s  re am zi g! 1!
"""