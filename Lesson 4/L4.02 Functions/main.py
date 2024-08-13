# L4.02 Functions
# REDACTED(I <3 not doxxing myself)
# Take 3 numbers from the user representing a, b and c in a quadratic equation 0 = ax^2 + bx + c
# using a function to return the values for x sorted from smallest to greatest

# Define a new function to solve the quadratic equation that takes the a, b and c values as parameters
def SolveQuadraticEquation(a,b,c):
    # Calculate the roots using the quadratic formula
    root1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    root2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    # Find which root is bigger and return the smaller root first
    try:
        if(root1 > root2):
            return root1, root2
        else:
            return root1, root2
    # If sorting the roots fail because they are complex
    except:
        # Return that the root is a complex root
        return "The roots are complex"

# Infinite loop
while True:
    # If converting any of the inputs to a float fails, do not crash the program
    try:
        # Get the a, b and c values of the quadratic equation and convert them to floats
        a = float(input("Enter the a value for the quadratic equation:"))
        b = float(input("Enter the b value for the quadratic equation:"))
        c = float(input("Enter the c value for the quadratic equation:"))
    # If converting any of the inputs to a float does fail,
    except:
        # Print that the input is invalid and loop again to get new input
        print("Please enter valid inputs.")
    # If converting the inputs to floats is successful
    else:
        # Exit the infinite loop
        break
# Set the result to what is returned by solving the quadratic equation using the values of a, b and c
result = SolveQuadraticEquation(a,b,c)
# If the quadratic equation has complex roots,
if result == "The roots are complex":
    # Print that the roots are complex
    print(result)
# If the quadratic equation does not have complex roots
else:
    # Print the roots of the quadratic equation
    print(*result)

# Test cases
"""
Enter the a value for the quadratic equation:2
Enter the b value for the quadratic equation:7
Enter the c value for the quadratic equation:1
-0.14921894064178787 -3.350781059358212
"""
"""
Enter the a value for the quadratic equation:2
Enter the b value for the quadratic equation:15
Enter the c value for the quadratic equation:-4
0.25780488547034963 -7.75780488547035
"""
"""
Enter the a value for the quadratic equation:4
Enter the b value for the quadratic equation:-3
Enter the c value for the quadratic equation:-2
1.175390529679106 -0.42539052967910607
"""
"""
Enter the a value for the quadratic equation:-2
Enter the b value for the quadratic equation:3
Enter the c value for the quadratic equation:6
-1.1374586088176875 2.6374586088176875
"""
"""
Enter the a value for the quadratic equation:-2
Enter the b value for the quadratic equation:-10
Enter the c value for the quadratic equation:5
-5.458039891549808 0.45803989154980806
"""
"""
Enter the a value for the quadratic equation:-8
Enter the b value for the quadratic equation:-1
Enter the c value for the quadratic equation:-2
The roots are complex
"""
"""
Enter the a value for the quadratic equation:notafloat
Please enter valid inputs.
Enter the a value for the quadratic equation:2
Enter the b value for the quadratic equation:notafloat
Please enter valid inputs.
Enter the a value for the quadratic equation:-2
Enter the b value for the quadratic equation:1
Enter the c value for the quadratic equation:3
-1.0 1.5
"""