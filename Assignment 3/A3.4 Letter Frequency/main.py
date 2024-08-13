# A3.4 Letter Frequency
# REDACTED(I <3 not doxxing myself)
# Get a string from the user and print how frequently each letter occured in that string

# Infinite loop
while True:
    # If the program fails to interpret the user's input, do not crash the program
    try:
        # Get a string from the user
        userString = input("Please enter a string:")
    # If getting a string from the user fails,
    except:
        # Print that the string is invalid and loop again to get new input
        print("Please enter a valid string.")
    # If getting a string from the user is successful,
    else:
        # If the string is blank
        if userString == "":
            # Print that there are no letters
            print("There are no letters.")
            # Exit the program as we do not need to do any further testing
            exit()
        # If the string is not blank
        else:
            # Exit the infinite input loop and move to the main function of the program
            break
# Initialize a list to store the letters of the string
letters = []
# Initialize a list to store the frequency of those letters, the indexes of this list will correspond with the indexes of the letters list
frequencies = []

# For every letter in the input string
for i in range(0,len(userString)):
    # If finding the position of the current letter in the letters list fails, do not crash the program
    try:
        # Find the position current letter in the letters list
        index = letters.index(userString[i])
    # If finding the position of the current letter in the letters list fails
    except ValueError:
        # Add the letter to the end of the letters list
        letters.append(userString[i])
        # Add the corresponding frequency for that letter and set it to 1
        frequencies.append(1)
    # If finding the position of the current letter in the letters list is successful
    else:
        # Add 1 to the frequency of that letter using its position in the letters list as the lists corrrespond to each other
        frequencies[index] = frequencies[index] + 1

# For every entry in the letters list
for i in range(0,len(letters)):
    # Print the character and how many times it occured using the letters and frequency lists
    print("The character", letters[i], "occurred", frequencies[i], "time(s).")

# Test cases
"""
Please enter a string: testing
The character t occurred 2 time(s).
The character e occurred 1 time(s).
The character s occurred 1 time(s).
The character i occurred 1 time(s).
The character n occurred 1 time(s).
The character g occurred 1 time(s).
"""
"""
Please enter a string:    magically magic utopia
The character   occurred 5 time(s).
The character m occurred 2 time(s).
The character a occurred 4 time(s).
The character g occurred 2 time(s).
The character i occurred 3 time(s).
The character c occurred 2 time(s).
The character l occurred 2 time(s).
The character y occurred 1 time(s).
The character u occurred 1 time(s).
The character t occurred 1 time(s).
The character o occurred 1 time(s).
The character p occurred 1 time(s).
"""
"""
Please enter a string: I wish That MANY MOONS Come
The character I occurred 1 time(s).
The character   occurred 5 time(s).
The character w occurred 1 time(s).
The character i occurred 1 time(s).
The character s occurred 1 time(s).
The character h occurred 2 time(s).
The character T occurred 1 time(s).
The character a occurred 1 time(s).
The character t occurred 1 time(s).
The character M occurred 2 time(s).
The character A occurred 1 time(s).
The character N occurred 2 time(s).
The character Y occurred 1 time(s).
The character O occurred 2 time(s).
The character S occurred 1 time(s).
The character C occurred 1 time(s).
The character o occurred 1 time(s).
The character m occurred 1 time(s).
The character e occurred 1 time(s).
"""
"""
Please enter a string: ....@@a9a@912345
The character . occurred 4 time(s).
The character @ occurred 3 time(s).
The character a occurred 2 time(s).
The character 9 occurred 2 time(s).
The character 1 occurred 1 time(s).
The character 2 occurred 1 time(s).
The character 3 occurred 1 time(s).
The character 4 occurred 1 time(s).
The character 5 occurred 1 time(s).
"""
"""
Please enter a string: 
There are no letters.
"""
"""
Please enter a string: morning
The character m occurred 1 time(s).
The character o occurred 1 time(s).
The character r occurred 1 time(s).
The character n occurred 2 time(s).
The character i occurred 1 time(s).
The character g occurred 1 time(s).
"""