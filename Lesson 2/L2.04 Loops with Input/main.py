# L2.04 Loops with Input
# REDACTED(I <3 not doxxing myself)
# Get a list of integers from the user where the list should be terminated by entering 0
# and then print the largest integer in the list

# Initialize the list of numbers that the user will be adding numbers to

numList = []
# Loop forever
while True:
    # If something goes wrong, the progrma will not crash
    try:
        # Get an input from the user, convert it to an integer and add it to the list
        numList.append(int(input("Please enter an integer to add to the list or 0 to end the list:")))
        # If the number the user just entered is 0,
        if numList[len(numList) - 1] == 0:
            # Remove the 0 from the list
            numList.remove(numList[len(numList) - 1])
            # Exit the infinite loop
            break
    # If we are unable to convert the user's input to an integer,
    except ValueError:
        # Print that the value is not a valid integer and keep going through the loop
        print("That value is not a valid integer")
# If the list is empty, len(numList) will return 0
if len(numList) == 0:
    # If the list is empty, print that there is no maximum value
    print("There is no maximum value")
# If the list is not empty, find the largest number and print it
else:
    largestNumber = numList[0]
    # Iterate over every number in the array
    for a in numList:
        # If the current number is larger than the largest number so far,
        if a > largestNumber:
            # Make the current number the new largest number
            largestNumber = a
    # Print the largest number that we find
    print("The largest number in the list is:", largestNumber)

# Test cases
"""
Please enter an integer to add to the list or 0 to end the list: 0
There is no maximum value
"""
"""
Please enter an integer to add to the list or 0 to end the list: -0
There is no maximum value
"""
"""
Please enter an integer to add to the list or 0 to end the list: 16
Please enter an integer to add to the list or 0 to end the list: 32
Please enter an integer to add to the list or 0 to end the list: 64
Please enter an integer to add to the list or 0 to end the list: 0
The largest number in the list is: 64
"""
"""
Please enter an integer to add to the list or 0 to end the list: -2 
Please enter an integer to add to the list or 0 to end the list: -6
Please enter an integer to add to the list or 0 to end the list: -8
Please enter an integer to add to the list or 0 to end the list: -10
Please enter an integer to add to the list or 0 to end the list: 1
Please enter an integer to add to the list or 0 to end the list: 0
The largest number in the list is: 1
"""
"""
Please enter an integer to add to the list or 0 to end the list: -15
Please enter an integer to add to the list or 0 to end the list: -4
Please enter an integer to add to the list or 0 to end the list: -32
Please enter an integer to add to the list or 0 to end the list: 0
The largest number in the list is: -4
"""
"""
Please enter an integer to add to the list or 0 to end the list: 21931298321093
Please enter an integer to add to the list or 0 to end the list: 23942384982349823
Please enter an integer to add to the list or 0 to end the list: 23423492834
Please enter an integer to add to the list or 0 to end the list: 91829398123
Please enter an integer to add to the list or 0 to end the list: 59843953894534895
Please enter an integer to add to the list or 0 to end the list: 0
The largest number in the list is: 59843953894534895
"""
"""
Please enter an integer to add to the list or 0 to end the list: -4594589348234
Please enter an integer to add to the list or 0 to end the list: -239849238492384329
Please enter an integer to add to the list or 0 to end the list: -238112312391298231
Please enter an integer to add to the list or 0 to end the list: -459984329832498923848
Please enter an integer to add to the list or 0 to end the list: -7
Please enter an integer to add to the list or 0 to end the list: 0
The largest number in the list is: -7
"""
"""
Please enter an integer to add to the list or 0 to end the list: abc
That value is not a valid integer
Please enter an integer to add to the list or 0 to end the list: 123
Please enter an integer to add to the list or 0 to end the list: def
That value is not a valid integer
Please enter an integer to add to the list or 0 to end the list: 191831293
Please enter an integer to add to the list or 0 to end the list: 6
Please enter an integer to add to the list or 0 to end the list: 0
The largest number in the list is: 191831293
"""