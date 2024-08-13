# L1.08 Lists 2
# REDACTED(I <3 not doxxing myself)
# Get 5 integer inputs and store them in a list, then check if a user-provided integer is in the list
# If the integer is in the list, print which position it is in

# Create a list of numbers
numbers = []
# Add the numbers the user enters to the list
numbers.append(int(input("Enter the first number:")))
numbers.append(int(input("Enter the second number:")))
numbers.append(int(input("Enter the third number:")))
numbers.append(int(input("Enter the fourth number:")))
numbers.append(int(input("Enter the fifth number:")))

# Print the list
print("The list is:", numbers)

# Get a new number from the user to search the list for
input_number = int(input("Enter a new number to search for in the list: "))
# If the number the user entered is in the list,
if input_number in numbers:
  # find the position of the number in the list and print it along with the number
  print(input_number, "is in the list at position", numbers.index(input_number), ".")
# If the number the user entered is not in the list,
else:
  # Print that the number is not in the list
  print(input_number, "is not in the list.")

# Test cases
"""
Enter the first number: 1
Enter the second number: 2
Enter the third number: 3
Enter the fourth number: 4
Enter the fifth number: 5
The list is: [1, 2, 3, 4, 5]
Enter a new number to search for in the list: 3
3 is in the list at position 2 .
"""
"""
Enter the first number: 1
Enter the second number: 2
Enter the third number: 3
Enter the fourth number: 4
Enter the fifth number: 5
The list is: [1, 2, 3, 4, 5]
Enter a new number to search for in the list: 6
6 is not in the list.
"""
"""
Enter the first number: 0
Enter the second number: 0
Enter the third number: 0
Enter the fourth number: 0
Enter the fifth number: 0
The list is: [0, 0, 0, 0, 0]
Enter a new number to search for in the list: 0
0 is in the list at position 0 .
"""
"""
Enter the first number: 0
Enter the second number: 0
Enter the third number: 0
Enter the fourth number: 0
Enter the fifth number: 0
The list is: [0, 0, 0, 0, 0]
Enter a new number to search for in the list: 3
3 is not in the list.
"""
"""
Enter the first number: -1
Enter the second number: -2
Enter the third number: -3
Enter the fourth number: -4
Enter the fifth number: -5
The list is: [-1, -2, -3, -4, -5]
Enter a new number to search for in the list: -2
-2 is in the list at position 1 .
"""
"""
Enter the first number: -1
Enter the second number: -2
Enter the third number: -3
Enter the fourth number: -4
Enter the fifth number: -5
The list is: [-1, -2, -3, -4, -5]
Enter a new number to search for in the list: -6
-6 is not in the list.
"""
"""
Enter the first number: -1  
Enter the second number: -1
Enter the third number: -1
Enter the fourth number: -1
Enter the fifth number: -1
The list is: [-1, -1, -1, -1, -1]
Enter a new number to search for in the list: -1
-1 is in the list at position 0 .
"""
"""
Enter the first number: 1
Enter the second number: 1
Enter the third number: 1
Enter the fourth number: 1
Enter the fifth number: 1
The list is: [1, 1, 1, 1, 1]
Enter a new number to search for in the list: 1
1 is in the list at position 0 .
"""
"""
Enter the first number: 1
Enter the second number: 1
Enter the third number: 1
Enter the fourth number: 1
Enter the fifth number: 1
The list is: [1, 1, 1, 1, 1]
Enter a new number to search for in the list: 2
2 is not in the list.
"""
"""
Enter the first number: -1
Enter the second number: -1
Enter the third number: -1
Enter the fourth number: -1
Enter the fifth number: -1
The list is: [-1, -1, -1, -1, -1]
Enter a new number to search for in the list: -2
-2 is not in the list.
"""