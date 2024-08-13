#L1.2A Variables and Input
# REDACTED(I <3 not doxxing myself)
# Gets 2 numbers from the user and multiplies them

# Loop until a valid input is given
while(True):
    try:
        # Get the first input from the user
        firstNum = int(input("Enter your first number:"))
        # Get the second input from the user
        secondNum = int(input("Enter your second number:"))
    # If we cannot convert the input to an integer
    except:
        # Tell the user to enter a valid input
        print("Please enter a valid integer")
    # If there is no error and we have successfully converted the user's input to an integer
    else:
        # Exit the loop
        break
# Print the product of the 2 numbers
print(firstNum * secondNum)
# Test cases
"""
Enter your first number: 1
Enter your second number: 2
2
"""
"""
Enter your first number: 0
Enter your second number: 0
0
"""
"""
Enter your first number: -1
Enter your second number: 2
-2
"""