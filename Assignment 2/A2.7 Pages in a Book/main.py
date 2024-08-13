# A2.7 Pages in a Book
# REDACTED(I <3 not doxxing myself)
# Check if a user-inputted number matches the sum of all the digits of all the page numbers in a book

# Infinite loop
while True:
    # If converting the user's input to an integer fails, do not crash the program
    try:
        # Get an input from the user and convert it to an integer
        userNumber = int(input("Please enter an integer:"))
    # If Converting the user's input to an integer fails
    except:
        # Print that the input was invalid and loop again to get new input
        print("Please enter an integer.")
    # If converting the user's input to an integer was successful
    else:
        # Exit the infinite loop and move to the main function of the program
        break
# Initialize a starting total, all additions will simply build upon this number for efficiency
total = 0
# Iterate over all the possible last pages up to the number the user chose
for i in range(1, userNumber):
    # If the number has multiple digits,
    if i >= 10:
        # Convert the number into a string
        strNumber = str(i)
        # For every digit(each digit occupies a character in the string)
        for b in range(0,len(strNumber)):
            # Increase the total by each digit
            total = total + int(strNumber[b])
    # If the number only has 1 digit
    else:
        # Simply add the digit to the total
        total = total + i
    # If the new total matches the number that the user entered
    if total == userNumber:
        # Print that the user's number matches a book with the last page number of pages
        print(userNumber, "matches with a book that has", i, "pages.")
        # Exit the program successfully to prevent any further output or testing
        exit(0)
# If no matches were found, print that the user's number does not match any number of pages
print(userNumber, "does not match")

# Test cases
"""
Please enter an integer: 0
0 does not match
"""
"""
Please enter an integer: abc
Please enter an integer.
Please enter an integer: #%@as
Please enter an integer.
Please enter an integer: 56
56 does not match
"""
"""
Please enter an integer: -48
-48 does not match
"""
"""
Please enter an integer: 325
325 matches with a book that has 49 pages.
"""
"""
Please enter an integer: 90
90 matches with a book that has 18 pages.
"""
"""
Please enter an integer: 6561320
6561320 does not match
"""
"""
Please enter an integer: 3250
3250 does not match
"""
"""
Please enter an integer: 42
42 does not match
"""
"""
Please enter an integer: 3241
3241 matches with a book that has 328 pages.
"""
"""
Please enter an integer: 45
45 matches with a book that has 9 pages.
"""
"""
Please enter an integer: 10000005
10000005 matches with a book that has 418181 pages.
"""