# A4.1 Letter Frequency
# REDACTED(I <3 not doxxing myself)
# Get a string from the user and print how many times each character occured in the string using a dictionary

# Infinite loop
while True:
    # If getting a string from the user fails, don't crash the program
    try:
        # Get a string from the user
        userInput = input("Please enter a string: ")
    # If getting the string fails
    except:
        # Print that the string is invalid and loop again to get new input
        print("This is not a valid string.")
    # If we get a valid string from the user
    else:
        # Exit the infinite loop and move to the main function of the program
        break

# If there are no letters in the string
if len(userInput) == 0:
    # Print that there are no letters
    print("There are no letters.")
# Otherwise initialize a dictionary
else:
    dictionary = {}
    # For every letter in the string
    for i in userInput:
        # If the letter is already in the dictionary, add 1 to it's count
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        # If the letter is not already in the dictionary, initialize it's value to 1
        else:
            dictionary[i] = 1
    # For every key in the dictionary
    for i in dictionary:
        # Print the key and its associated count
        print("The character", i, "occured", dictionary[i], "time(s).")

# Test cases
"""
Please enter a string: 
There are no letters.
"""
"""
Please enter a string: sstring
The character s occured 2 time(s).
The character t occured 1 time(s).
The character r occured 1 time(s).
The character i occured 1 time(s).
The character n occured 1 time(s).
The character g occured 1 time(s).
"""
"""
Please enter a string: !@!!!##@@867673
The character ! occured 4 time(s).
The character @ occured 3 time(s).
The character # occured 2 time(s).
The character 8 occured 1 time(s).
The character 6 occured 2 time(s).
The character 7 occured 2 time(s).
The character 3 occured 1 time(s).
"""
"""
Please enter a string: this is a much longer string to perform a very easy performance test on this code and to make sure that i
t is working properly and that everything is as it should be
The character t occured 14 time(s).
The character h occured 7 time(s).
The character i occured 10 time(s).
The character s occured 11 time(s).
The character   occured 32 time(s).
The character a occured 10 time(s).
The character m occured 4 time(s).
The character u occured 3 time(s).
The character c occured 3 time(s).
The character l occured 3 time(s).
The character o occured 10 time(s).
The character n occured 8 time(s).
The character g occured 4 time(s).
The character e occured 14 time(s).
The character r occured 12 time(s).
The character p occured 4 time(s).
The character f occured 2 time(s).
The character v occured 2 time(s).
The character y occured 4 time(s).
The character d occured 4 time(s).
The character k occured 2 time(s).
The character w occured 1 time(s).
The character b occured 1 time(s).
"""