# L2.03 Try-Except
# REDACTED(I <3 not doxxing myself)
# Get 2 numbers from the user, validate the input, and then try to divide them, if there is an error print that the quotient is undefined

# Keep trying to get input until it is validated
while True:
    try:
        # Get 2 numbers from the user and convert them to floats
        num1 = float(input("Please enter the first number:"))
        num2 = float(input("Please enter the second number:"))
    # If converting thet user input to a float fails
    except ValueError:
        #print that a valid number is required 
        print("A valid number is required")
        # The program will go back to the while loop and ask for input again since inputReceived has not been set to true
    # If we are able to successfully convert the user input to a float,
    else:
        # exit the infinite loop
        break
try:
    # Try to print the division of the 2 numbers
    print("The quotient of", num1, "divided by", num2, "is", num1/num2)
# If the division fails because we are trying to divide by 0
except ZeroDivisionError:
    # Print that the result of the division is undefined
    print("The quotient of", num1, "divided by", num2, "is undefined.")

# Test cases
"""
Please enter the first number: 4
Please enter the second number: 2
The quotient of 4.0 divided by 2.0 is 2.0
"""
"""
Please enter the first number: 2
Please enter the second number: 4
The quotient of 2.0 divided by 4.0 is 0.5
"""
"""
Please enter the first number: -4
Please enter the second number: -2
The quotient of -4.0 divided by -2.0 is 2.0
"""
"""
Please enter the first number: -2
Please enter the second number: 4
The quotient of -2.0 divided by 4.0 is -0.5
"""
"""
Please enter the first number: abc
A valid number is required
Please enter the first number: 32 
Please enter the second number: 8
The quotient of 32.0 divided by 8.0 is 4.0
"""
"""
Please enter the first number: 123
Please enter the second number: abc
A valid number is required
Please enter the first number: 256
Please enter the second number: 16
The quotient of 256.0 divided by 16.0 is 16.0
"""
"""
Please enter the first number: abc
A valid number is required
Please enter the first number: abc
A valid number is required
Please enter the first number: 123
Please enter the second number: abc
A valid number is required
Please enter the first number: 123
Please enter the second number: abc
A valid number is required
Please enter the first number: 123
Please enter the second number: abc
A valid number is required
Please enter the first number: 9
Please enter the second number: 0
The quotient of 9.0 divided by 0.0 is undefined.
"""
"""
Please enter the first number: 10
Please enter the second number: 0
The quotient of 10.0 divided by 0.0 is undefined.
"""
"""
Please enter the first number: -10
Please enter the second number: 0
The quotient of -10.0 divided by 0.0 is undefined.
"""
"""
Please enter the first number: 13
Please enter the second number: -0 
The quotient of 13.0 divided by -0.0 is undefined.
"""