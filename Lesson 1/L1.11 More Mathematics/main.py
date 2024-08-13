# L1.11 More Mathematics
# REDACTED(I <3 not doxxing myself)
# Given the values of a, b, and c, solve the quadratic equation to find the roots

# Get the a, b, and c values from the user and convert them into floats
a = float(input("Please enter the a value:"))
b = float(input("Please enter the b value:"))
c = float(input("Please enter the c value:"))

# Calculate the roots using the quadratic formula
root1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
root2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
# Find which root is bigger and print the bigger root first
try:
    if(root1 > root2):
        print(root1, root2)
    else:
        print(root2, root1)
except:
    print("The root is a complex root")

# Test cases
"""
Please enter the a value: 2
Please enter the b value: 7
Please enter the c value: 1
-0.14921894064178787 -3.350781059358212
"""
"""
Please enter the a value: 2
Please enter the b value: 15
Please enter the c value: -4
0.25780488547034963 -7.75780488547035
"""
"""
Please enter the a value: 4
Please enter the b value: -3
Please enter the c value: -2
1.175390529679106 -0.42539052967910607
"""
"""
Please enter the a value: -2
Please enter the b value: 3
Please enter the c value: 6
2.6374586088176875 -1.1374586088176875
"""
"""
Please enter the a value: -2
Please enter the b value: -10
Please enter the c value: 5
0.45803989154980806 -5.458039891549808
"""
"""
Please enter the a value: -8
Please enter the b value: -1
Please enter the c value: -2
The root is a complex root
"""