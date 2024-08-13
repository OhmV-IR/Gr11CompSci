# A2.1 Alphabet Triangle
# REDACTED(I <3 not doxxing myself)
# Get a lowercase character input from a to z and display the capital alphabet up to that letter,
# and print it again each following line with one less letter at the end until only A is printed

# Initialize a string with all the letters of the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Infinite loop
while True:
    # If getting a string from the user fails, do not crash the program
    try:
        # Get a string input from the user
        letter = input("Enter a single lowercase letter:")
    # if getting a string from the user fails,
    except:
        # Print that the string is invalid and loop again to get new input
        print("Please enter a valid string.")
    # Make sure that the input is not a number or other special character and that the user has only entered 1 letter
    if letter.isalpha() == False or letter.isupper() == True or len(letter) > 1 or letter == "":
        # If the input is invalid, print that the user needs to enter a valid input and loop
        print("Please enter only a single lowercase letter like so: f")
    # If the input is valid
    else:
        # Convert the lowercase letter into an uppercase letter
        letter = letter.upper()
        # Exit the infinite loop
        break
# Find the inputted letter in the alphabet string and add 1 to the index(range function is exclusive)
# This variable acts as the number of rows that we need to print
numberOfRows = alphabet.index(letter) + 1
# For every row that we need to print,
for a in range(0,numberOfRows):
    # For every letter that we need to print(-1 letter so we can keep the newline seperator for the last one)
    for b in range(0,numberOfRows - a - 1):
        # Print the letters without a newline ending character
        print(alphabet[b], end="")
    # Print the last letter with a newline ending character
    print(alphabet[numberOfRows - a - 1])

# Test cases
"""
Enter a single lowercase letter:j
ABCDEFGHIJ
ABCDEFGHI
ABCDEFGH
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
"""
"""
Enter a single lowercase letter:1
Please enter only a single lowercase letter like so: f
Enter a single lowercase letter:f
ABCDEF
ABCDE
ABCD
ABC
AB
A
"""
"""
Enter a single lowercase letter:z
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXY
ABCDEFGHIJKLMNOPQRSTUVWX
ABCDEFGHIJKLMNOPQRSTUVW
ABCDEFGHIJKLMNOPQRSTUV
ABCDEFGHIJKLMNOPQRSTU
ABCDEFGHIJKLMNOPQRST
ABCDEFGHIJKLMNOPQRS
ABCDEFGHIJKLMNOPQR
ABCDEFGHIJKLMNOPQ
ABCDEFGHIJKLMNOP
ABCDEFGHIJKLMNO
ABCDEFGHIJKLMN
ABCDEFGHIJKLM
ABCDEFGHIJKL
ABCDEFGHIJK
ABCDEFGHIJ
ABCDEFGHI
ABCDEFGH
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
"""
"""
Enter a single lowercase letter:a
A
"""
"""
Enter a single lowercase letter:!
Please enter only a single lowercase letter like so: f
Enter a single lowercase letter:3
Please enter only a single lowercase letter like so: f
Enter a single lowercase letter:a
A
"""
"""
Enter a single lowercase letter:D
Please enter only a single lowercase letter like so: f
Enter a single lowercase letter:d
ABCD
ABC
AB
A
"""
"""
Enter a single lowercase letter:
Please enter only a single lowercase letter like so: f
Enter a single lowercase letter:f
ABCDEF
ABCDE
ABCD
ABC
AB
A
"""