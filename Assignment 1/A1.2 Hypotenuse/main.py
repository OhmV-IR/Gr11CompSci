# A1.2 Hypotenuse
# REDACTED(I <3 not doxxing myself)
# # Take 2 float inputs as legs of a right-angled triangle and calculate the hypotenuse of that triangle
# then print that to the console

try:
        # Get 2 numbers from the user that represent the first and second legs of the triangle
    num1 = float(input("Please enter the length of the first leg of the triangle:"))
    num2 = float(input("Please enter the length of the second leg of the triangle:"))
    # If either of the numbers is negative, then throw an error
    if num1 < 0 or num2 < 0:
        raise ValueError
# If there is an error like we cannot conver the input to a float or the input is negative,
except:
    # Print the error message
    print("Lengths must be positive.")
# If there is no error and we have succesfully converted the input to a float and made sure it is positive
else:
    # Using the pythagorean theorem, c(the hypotenuse) is the square root of a squared + b squared
    print("The hypotenuse of the triangle is", (num1**2 + num2**2) ** 0.5)
# Test cases
"""
Please enter the length of the first leg of the triangle: 8
Please enter the length of the second leg of the triangle: 9
The hypotenuse of the triangle is 12.041594578792296
"""
"""
Please enter the length of the first leg of the triangle: 3
Please enter the length of the second leg of the triangle: 4
The hypotenuse of the triangle is 5.0
"""
"""
Please enter the length of the first leg of the triangle: 0
Please enter the length of the second leg of the triangle: 0
The hypotenuse of the triangle is 0.0
"""
"""
Please enter the length of the first leg of the triangle: -3
Please enter the length of the second leg of the triangle: 4
Lengths must be positive.
"""
"""
Please enter the length of the first leg of the triangle: 3
Please enter the length of the second leg of the triangle: -4
Lengths must be positive.
"""