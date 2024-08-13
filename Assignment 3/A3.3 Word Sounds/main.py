# A3.3 Word Sounds
# REDACTED(I <3 not doxxing myself)
# Convert a word to a WordSound code by following these steps:
#First, replace all letters except the first letter in the word with a digit based on the following:
# A, E, H, I, O, U, W, Y are replaced by 0
# B, F, P, V are replaced by 1
# C, G, J, K, Q are replaced by 2
# D, T are replaced by 3
# L is replaced by 4
# M, N are replaced by 5
# R is replaced by 6
# S, X, Z are replaced by 7
# Second, remove all immediate repetitions (ie. digits that are the same as the one before them.
# Third, remove all zeroes.
# Fourth, remove all characters beyond the fourth. If the WordSound code doesn't have four characters, add zeroes to the end until it does.
# Fifth, capitalize the first letter.

# Infinite loop
while True:
    # If getting input from the user fails, do not crash the program
    try:
        # Get a string from the user
        inputWord = input("Please enter a word:")
    # If getting input from the user fails
    except:
        # Print that the word is invalid and loop again to get new input
        print("This is not a valid word.")
    # If getting input from the user is successful
    else:
        # Remove the whitespace from the left and right sides of the string
        inputWord = inputWord.rstrip()
        inputWord = inputWord.lstrip()
        # Make every letter of the word uppercase
        inputWord = inputWord.upper()
        # Exit the infinite loop and move to the main function of the program
        break
# Copy the first letter of the word to the new string, the other letters will be run through the algorithm
stage1Str = inputWord[0]
# For every letter of the word except for the first letter,
for i in range(1,len(inputWord)):
    # If the letter is A,E,H,I,O,U,W, or Y, add 0 to the string instead of the letter
    if inputWord[i] == 'A' or inputWord[i] == 'E' or inputWord[i] == 'H' or inputWord[i] == 'I' or inputWord[i] == 'O' or inputWord[i] == 'U' or inputWord[i] == 'W' or inputWord[i] == 'Y':
        stage1Str = stage1Str + "0"
    # If the letter is B,F,P or V, add 1 to the string instead of the letter
    elif inputWord[i] == 'B' or inputWord[i] == 'F' or inputWord[i] == 'P' or inputWord[i] == 'V':
        stage1Str = stage1Str + "1"
    # If the letter is C,G,J,K or Q, add 2 to the string instead of the letter
    elif inputWord[i] == 'C' or inputWord[i] == 'G' or inputWord[i] == 'J' or inputWord[i] == 'K' or inputWord[i] == 'Q':
        stage1Str = stage1Str + "2"
    # If the letter is D or T, add 3 to the string instead of the letter
    elif inputWord[i] == 'D' or inputWord[i] == 'T':
        stage1Str = stage1Str + "3"
    # If the letter is L, add 4 to the string instead of the letter
    elif inputWord[i] == 'L':
        stage1Str = stage1Str + "4"
    # If the letter is M or N, add 5 to the string instead of the letter
    elif inputWord[i] == 'M' or inputWord[i] == 'N':
        stage1Str = stage1Str + "5"
    # If the letter is R, add 6 to the string instead of the letter
    elif inputWord[i] == 'R':
        stage1Str = stage1Str + "6"
    # If the letter is S, X, or Z, add 7 to the string instead of the letter
    else:
        stage1Str = stage1Str + "7"

# Copy only the first letter over again, the other letters need to run through the algorithm
stage2Str = stage1Str[0]
# Initialize the last letter as a random string(so that it doesn't match)
lastLetter = "aksjdkasjdaskdkasdjasdj"
# For the 1st to last character of the string after step 1,
for i in range(1,len(stage1Str)):
    # If the current letter is different than the last letter, add it to the new string
    if stage1Str[i] != lastLetter:
        stage2Str = stage2Str + stage1Str[i]
    # Set the last letter to the current letter
    lastLetter = stage1Str[i]

# Copy only the first letter again, the other letters will run through the algorithm
stage3Str = stage2Str[0]
# For the 1st to last characters in the string after step 2,
for i in range(1,len(stage2Str)):
    # If the current letter is not 0,
    if stage2Str[i] != '0':
        # Add the letter to the new string
        stage3Str = stage3Str + stage2Str[i]

# If there are less than 4 characters in the step 3 string
if len(stage3Str) < 4:
    # Copy the entire step 3 string to the step 4 string
    stage4Str = stage3Str
    # For every missing character,
    for i in range(len(stage4Str), 4):
        # Add 0 to the step 4 string
        stage4Str = stage4Str + "0"
# If there are more than 4 characters in the step 3 string
else:
    # Copy the first four characters of the step 3 string into the step 4 string
    stage4Str = stage3Str[:4]

# The first letter of the string was already capitalized when we handled the input because we converted all the letters to uppercase
# so we can simply print the step 4 string as the result
print(stage4Str)

# Test cases
"""
Please enter a word: Ababak
A112
"""
"""
Please enter a word: HUI
H000
"""
"""
Please enter a word: tracking
T625
"""
"""
Please enter a word:        Kulat      
K430
"""
"""
Please enter a word:     python
P350
"""
"""
Please enter a word: addition
A335
"""
"""
Please enter a word: sequence
S252
"""