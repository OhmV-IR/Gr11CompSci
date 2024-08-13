# A1.5 Sort 4 Numbers
# REDACTED(I <3 not doxxing myself)
# Get 4 numbers as input and sort them from lowest to highest

# Get 4 numbers as input
n1 = int(input("Please enter the first integer:"))
n2 = int(input("Please enter the second integer:"))
n3 = int(input("Please enter the third integer:"))
n4 = int(input("Please enter the fourth integer:"))
# Define variables to return
first = 0
second = 0
third = 0
fourth = 0
# If the second number is smaller than the 1st,
if n2 <= n1:
    # Make the 2st number first the 1nd number second
    first = n2
    second = n1
# If the second number is smaller than the first,
else:
    # Make the 1st number first and the 2nd number second
    first = n1
    second = n2
# If the third number is smaller than the first one(the smallest one thus far),
if n3 <= first:
    # Shift all the numbers up and insert the 3rd number at the beginning
    third = second
    second = first
    first = n3
# If the third number is not smaller than the first one, check if it smaller than the second one
elif n3 <= second:
    # If it is smaller than the second one, move the second one up and insert the 3rd number second
    third = second
    second = n3
# If none of these conditions are true, it is the biggest number so far,
else:
    # and we should insert it third
    third = n3
# If the 4th number is the smallest so far,
if n4 <= first:
     # Move all the other numbers up and insert it in the first spot
    fourth = third
    third = second
    second = first
    first = n4
# If the 4th number is smaller than the second number, 
elif n4 <= second:
    # Move the second and third numbers up and insert the 4th number second
    fourth = third
    third = second
    second = n4
# If the number is smaller than the third,
elif n4 <= third:
    # Move the third number up and insert the 4th number in the third spot
    fourth = third
    third = n4
# If all of these conditions fail, the 4th number is the biggest number so far so we insert it fourth
else:
    fourth = n4
# Print the sorted numbers
print(first, second, third, fourth)

# Test cases
"""
Please enter the first integer: 0
Please enter the second integer: 0
Please enter the third integer: 0
Please enter the fourth integer: 0
0 0 0 0
"""
"""
Please enter the first integer: 1
Please enter the second integer: 2
Please enter the third integer: 3
Please enter the fourth integer: 4
1 2 3 4
"""
"""
Please enter the first integer: 4
Please enter the second integer: 3
Please enter the third integer: 2
Please enter the fourth integer: 1
1 2 3 4
"""
"""
Please enter the first integer: 1
Please enter the second integer: 4
Please enter the third integer: 3
Please enter the fourth integer: 2
1 2 3 4
"""
"""
Please enter the first integer: 2
Please enter the second integer: 1
Please enter the third integer: 4
Please enter the fourth integer: 3
1 2 3 4
"""
"""
Please enter the first integer: 2
Please enter the second integer: 3
Please enter the third integer: 3
Please enter the fourth integer: 1
1 2 3 3
"""
"""
Please enter the first integer: 7
Please enter the second integer: 0
Please enter the third integer: 7
Please enter the fourth integer: 4
0 4 7 7
"""
"""
Please enter the first integer: -1
Please enter the second integer: -2
Please enter the third integer: -3
Please enter the fourth integer: -4
-4 -3 -2 -1
"""
"""
Please enter the first integer: -4
Please enter the second integer: -1
Please enter the third integer: -2
Please enter the fourth integer: -3
-4 -3 -2 -1
"""
"""
Please enter the first integer: -3
Please enter the second integer: -4
Please enter the third integer: -1
Please enter the fourth integer: -2
-4 -3 -2 -1
"""
"""
Please enter the first integer: -2
Please enter the second integer: -3
Please enter the third integer: -4
Please enter the fourth integer: -1
-4 -3 -2 -1
"""
"""
Please enter the first integer: -1
Please enter the second integer: 0
Please enter the third integer: 3
Please enter the fourth integer: 4
-1 0 3 4
"""
"""
Please enter the first integer: 57483921293128
Please enter the second integer: 43983849895498439
Please enter the third integer: 31001201032021932130
Please enter the fourth integer: 99999999999999999999999999999999
57483921293128 43983849895498439 31001201032021932130 99999999999999999999999999999999
"""