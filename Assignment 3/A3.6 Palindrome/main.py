# A3.6 Palindrome
# REDACTED(I <3 not doxxing myself)
# Get a string from the user and check if it spelt the same way forwards as backwards, ignoring all digits,
# whitespace, punctuation, and case differences

# Import string library to gain access to an array of ascii characters to compare our string's letters to
import string

# Infinite loop
while True:
    # If getting a string from the user fails, it will not crash the program
    try:
        # Get a string as input from the user
        inputString = input("Please enter a string:")
    # If getting a string from the user fails
    except:
        # Print that the string is invalid and loop again to get new input
        print("Please enter a valid string.")
    # If getting a string from the user is successful
    else:
        # Make all the letters of the input string uppercase
        inputString = inputString.upper()
        # Initialize an array that will hold the input string but only with ascii characters
        asciiString = []
        # For every character of the input string
        for i in range(0,len(inputString)):
            # If the current letter is an ascii letter
            if inputString[i] in string.ascii_uppercase:
                # Add the letter to the ascii string(array of characters)
                asciiString.append(inputString[i])
        # Once we have finished processing and stripping away special characters from the input string,
        # exit the infinite loop and move to the main function of the program
        break
# If the ascii string is the same as the ascii string in reverse,
if(asciiString == asciiString[::-1]):
    # Print that the input string is a palindrome
    print("The string is a palindrome.")
# If the ascii string is not the same as the ascii string in reverse,
else:
    # Print that the input string is not a palindrome
    print("The string is not a palindrome.")

# Test cases
"""
Please enter a string: racecar
The string is a palindrome.
"""
"""
Please enter a string: hello
The string is not a palindrome.
"""
"""
Please enter a string: r1a8c4e21c6666a212r99
The string is a palindrome.
"""
"""
Please enter a string: h3e11llo0
The string is not a palindrome.
"""
"""
Please enter a string: r@ac!e*c(a))r
The string is a palindrome.
"""
"""
Please enter a string: %he#l*&^l)(o)
The string is not a palindrome.
"""
"""
Please enter a string: RaCEcAr
The string is a palindrome.
"""
"""
Please enter a string: HelLo
The string is not a palindrome.
"""
"""
Please enter a string: r@3a*c..   e ^c*ar#   
The string is a palindrome.
"""
"""
Please enter a string: h@ .. e31!ll$(o)  
The string is not a palindrome.
"""
"""
Please enter a string: A man, a plan, a canal, Panama.
The string is a palindrome.
"""
"""
Please enter a string: a toyotas a toyota
The string is a palindrome.
"""
"""
Please enter a string: /r;:|ad.ar?^
The string is a palindrome.
"""
"""
Please enter a string: Racecar
The string is a palindrome.
"""
"""
Please enter a string: a23sa5n6t778aa9tna0sa
The string is a palindrome.
"""