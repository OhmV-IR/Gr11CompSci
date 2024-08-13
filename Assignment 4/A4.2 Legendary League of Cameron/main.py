# A4.2 Legendary League of Cameron
# REDACTED(I <3 not doxxing myself)
# Take player names as strings and their associated scores(1-2000) which are stored in a dictionary
# When a blank player name is entered, ask for a minimum and a maximum(inclusive) and print all player and score pairs within that range

# Initialize a dictionary
scores = {}
# Infinite loop
while True:
    # If getting a player name or converting inputs to integers fails, do not crash the program
    try:
        # Get a player name as a string from the user
        playerName = input("Please enter a player name: ")
        # If the user does not enter a player name,
        if playerName == "":
            # Ask for a minimum and maximum, then convert them to integers
            min = int(input("Minimum: "))
            max = int(input("Maximum: "))
            # Exit the input loop and move to the main function of the program
            break
        # Otherwise, ask for a score for the player and convert it to an integer
        score = int(input("Please enter a score from 1-2000: "))
    # If input handling fails,
    except:
        # Print that the input is invalid and loop again to get new input
        print("This is not a valid input")
    # If input handling is successful,
    else:
        # If the score is between 1 and 2000(inclusive)
        if score >= 1 and score <= 2000:
            # Add the score to the dictionary using the player's name and loop again for new input
            scores[playerName] = score
        # Otherwise
        else:
            # Print that the score must be between 1 and 2000 then loop to get new input
            print("The score must be between 1 and 2000")

# For every key(player name) in the scores dictionary
for i in scores:
    # If the score is within the provided range
    if scores[i] >= min and scores[i] <= max:
        # Print the player name and the score with a space between them
        print(i, scores[i])

# Test cases
"""
Please enter a player name: REDACTED
Please enter a score from 1-2000: 2000
Please enter a player name: REDACTED
Please enter a score from 1-2000: 1
Please enter a player name: 
Minimum: 1
Maximum: 2000
REDACTED 2000
REDACTED 1
"""
"""
Please enter a player name: notinrange
Please enter a score from 1-2000: 400
Please enter a player name: inrange
Please enter a score from 1-2000: 500
Please enter a player name: notinrangehigh
Please enter a score from 1-2000: 1001
Please enter a player name: inrangehigh
Please enter a score from 1-2000: 1000
Please enter a player name: 
Minimum: 500
Maximum: 1000
inrange 500
inrangehigh 1000
"""
"""
Please enter a player name: toohigh
Please enter a score from 1-2000: 2001
The score must be between 1 and 2000
Please enter a player name: high
Please enter a score from 1-2000: 2000
Please enter a player name: tolow
Please enter a score from 1-2000: 0
The score must be between 1 and 2000
Please enter a player name: verylow
Please enter a score from 1-2000: -1
The score must be between 1 and 2000
Please enter a player name: low
Please enter a score from 1-2000: 1
Please enter a player name: 
Minimum: 400
Maximum: 500
"""
"""
Please enter a player name: special
Please enter a score from 1-2000: @#!#@()
This is not a valid input
Please enter a player name: text
Please enter a score from 1-2000: abcd
This is not a valid input
Please enter a player name: number
Please enter a score from 1-2000: 5
Please enter a player name: numbertext
Please enter a score from 1-2000: abc1032
This is not a valid input
Please enter a player name: numberspecial
Please enter a score from 1-2000: 20120#2@!
This is not a valid input
Please enter a player name: #@)!
Please enter a score from 1-2000: 200
Please enter a player name: 12031
Please enter a score from 1-2000: 400
Please enter a player name: 
Minimum: 1
Maximum: 2000
number 5
#@)! 200
12031 400
"""
"""
Please enter a player name:      
Minimum: 300
Maximum: 700
"""