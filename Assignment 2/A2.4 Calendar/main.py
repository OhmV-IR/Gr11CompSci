# A2.4 Calendar
# REDACTED(I <3 not doxxing myself)
# Get the number of days in a month(28,29,30,31), and the day of the week on which that month starts(M, T, W, R, F, S, N)
# and print a calendar showing the days of the month matched to the correct days of the week

# Infinite loop
while True:
    # If converting to an integer fails, the program will not crash
    try:
        # Try to get the number of days in the month from the user and convert the input to an integer
        numberOfDays = int(input("Please enter the number of days in the month:"))
        # Try to get the day of the week on which the month starts from the user
        startDay = input("Please enter the day on which the month starts(M, T, W, R, F, S, N):")
    # If converting the number of days in the month to an integer fails
    except:
        # Print that the input is invalid and loop again to get new input
        print("Please enter a valid input.")
    # If nothing goes wrong and the number of days input is successfully converted to an integer
    else:
        # Check that the number of days is not less than 28 or greater than 31
        if numberOfDays >= 28 and numberOfDays <= 31:
            # Check that the starting day of the week the user has entered is one of the possible days of the week
            if startDay == "M" or startDay == "T" or startDay == "W" or startDay == "R" or startDay == "F" or startDay == "S" or startDay == "N":
                # Exit the infinite loop and continue to perform the main function of the program
                break
            # If the starting day of the week the user entered is none of the possible days of the week
            else:
                # Print that the input is invalid
                print("Please enter a valid starting day of the week for the month")
        # If the number of days is less than 28 or greater than 31
        else:
            # Print that the input is invalid
            print("Please enter a valid number of days for the month")

# Print starting block of text
print(" S  M  T  W Th  F  S")
print("---------------------")

# Intialize startNumber so that the program does not crash if the starting day is N(the first day of the week)
startNumber = 0
# If the starting day of the week for the month is monday
if startDay == "M":
    # Add 3 spaces to move the cursor to monday, and don't add a newline so we keep printing on the same line
    print("   ", end="")
    # Set the start number to 1 to account for the fact that we have moved our cursor 1 column
    startNumber = 1
# If the starting day of the week for the month is tuesday
if startDay == "T":
    # Add 6 spaces to move the cursor to tuesday, and don't add a newline so we keep printing on the same line
    print("      ", end="")
    # Set the start number to 2 to account for the fact that we have moved our cursor 2 columns
    startNumber = 2
# If the starting day of the week for the month is wednesday
if startDay == "W":
    # Print 9 spaces to move the cursor to wednesday, and don't add a newline so we keep printing on the same line
    print("         ", end="")
    # Set the start number to 3 to account for the fact that we have moved our cursor 3 columns
    startNumber = 3
# If the starting day of the week for the month is thursday
if startDay == "R":
    # Print 12 spaces to move the cursor to thursday, and don't add a newline so we keep printing on the same line
    print("            ", end="")
    # Set the start number to 4 to account for the fact that we have moved the cursor 4 columns
    startNumber = 4
# If the starting day of the week for the month is friday
if startDay == "F":
    # Print 15 spaces to move the cursor to friday, and don't add a newline so we keep printing on the same line
    print("               ", end="")
    # Set the start number to 5 to account for the fact that we have moved the cursor 5 columns
    startNumber = 5
# If the starting day of the week for the month is saturday
if startDay == "S":
    # Print 18 spaces to move the cursor to saturday, and don't add a newline so we keep printing on the same line
    print("                  ", end="")
    # Set the start number to 6 to account for the fact that we have moved the cursor 6 columns
    startNumber = 6
# For every number that we need to print(1 through the number of days in the month)
for i in range(1,numberOfDays + 1):
    # Get the current number of days we have printed if the month started on sunday(the first day of the week)
    currentNumberAdjusted = i + startNumber
    # If we have reached the end of a row, 
    if currentNumberAdjusted == 7 or currentNumberAdjusted == 14 or currentNumberAdjusted == 21 or currentNumberAdjusted == 28 or currentNumberAdjusted == 35:
        # If the number only has 1 digit
        if i < 10:
            # Print 1 space, then the number and then another space and then a newline to start a new row
            print(" " + str(i) + " ")
        # If the number has 2 digits
        else:
            # Print the number, then add a space and then a newline to start a new row
            print(str(i) + " ")
    # If we have not reached the end of the row,
    else:
        # If the number only has 1 digit
        if i < 10:
            # Print a space, then the number and then another space without a newline at the end so we keep printing in the same row
            print(" " + str(i) + " ", end="")
        # If the number has 2 digits
        else:
            # Print the number, then a space without a newline at the end so we keep printing in the same row
            print(str(i) + " ", end="")

# Test cases
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): N
 S  M  T  W Th  F  S
---------------------
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): M
 S  M  T  W Th  F  S
---------------------
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): T
 S  M  T  W Th  F  S
---------------------
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): W
 S  M  T  W Th  F  S
---------------------
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): W
 S  M  T  W Th  F  S
---------------------
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): R
 S  M  T  W Th  F  S
---------------------
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): F
 S  M  T  W Th  F  S
---------------------
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
"""
"""
Please enter the number of days in the month: 31
Please enter the day on which the month starts(M, T, W, R, F, S, N): S
 S  M  T  W Th  F  S
---------------------
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): N
 S  M  T  W Th  F  S
---------------------
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): M
 S  M  T  W Th  F  S
---------------------
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): T
 S  M  T  W Th  F  S
---------------------
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): W
 S  M  T  W Th  F  S
---------------------
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): R
 S  M  T  W Th  F  S
---------------------
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): F
 S  M  T  W Th  F  S
---------------------
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): S
 S  M  T  W Th  F  S
---------------------
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): N
 S  M  T  W Th  F  S
---------------------
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): M
 S  M  T  W Th  F  S
---------------------
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): T
 S  M  T  W Th  F  S
---------------------
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): W
 S  M  T  W Th  F  S
---------------------
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): R
 S  M  T  W Th  F  S
---------------------
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): F
 S  M  T  W Th  F  S
---------------------
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29
"""
"""
Please enter the number of days in the month: 29
Please enter the day on which the month starts(M, T, W, R, F, S, N): S
 S  M  T  W Th  F  S
---------------------
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): N
 S  M  T  W Th  F  S
---------------------
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): M
 S  M  T  W Th  F  S
---------------------
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): T
 S  M  T  W Th  F  S
---------------------
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): W
 S  M  T  W Th  F  S
---------------------
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): R
 S  M  T  W Th  F  S
---------------------
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): F
 S  M  T  W Th  F  S
---------------------
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28
"""
"""
Please enter the number of days in the month: 28
Please enter the day on which the month starts(M, T, W, R, F, S, N): S
 S  M  T  W Th  F  S
---------------------
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28
"""
"""
Please enter the number of days in the month: f
Please enter a valid input.
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): M
 S  M  T  W Th  F  S
---------------------
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
"""
"""
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): U
Please enter a valid starting day of the week for the month
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): N
 S  M  T  W Th  F  S
---------------------
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
"""
"""
Please enter the number of days in the month: 26
Please enter the day on which the month starts(M, T, W, R, F, S, N): M
Please enter a valid number of days for the month
Please enter the number of days in the month: 32
Please enter the day on which the month starts(M, T, W, R, F, S, N): T
Please enter a valid number of days for the month
Please enter the number of days in the month: 30
Please enter the day on which the month starts(M, T, W, R, F, S, N): S
 S  M  T  W Th  F  S
---------------------
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
"""