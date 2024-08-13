# L1.08b Strings as Lists
# REDACTED(I <3 not doxxing myself)
# Get a string from the user and determine how long it is

# Get a string from the user
string = input("Please enter a string:")
# Get the length of that string
stringLength = len(string)
# If the string has length(the length of the string is greater than 0),
if stringLength > 0:
    # Print the last character in the string(-1 is because arrays are indexed starting from 0)
    print(string[stringLength - 1])
# If the string has a length of 0,(could also happen if string has a negative length, but realistically impossible)
else:
    # Print that the string is empty
    print("The string is empty")

# Test cases
"""
Please enter a string: 
The string is empty
"""
"""
Please enter a string: hello
o
"""
"""
Please enter a string: Hello World 
d
"""
"""
Please enter a string: Hello World! :0 :}
}
"""
