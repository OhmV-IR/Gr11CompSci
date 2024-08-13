# A1.1 Largest of 3 numbers
# REDACTED(I <3 not doxxing myself)
# Gather 3 numbers from the user and find which number is the largest out of the 3

while True:
  try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    num3 = int(input("Enter the third number:"))
  except:
    print("Please enter a valid integer input")
  else:
    break
# If the first number is the largest out of the 3,
if num1 >= num2 and num1 >= num3:
  # State that the first number is the largest
  print(num1, "is the largest.")
# If the second number is the largest out of the 3,
elif num2 >= num1 and num2 > num3:
  # State that the second number is the largest
  print(num2, "is the largest")
# If the third number is the largest out of the 3,
else:
  # State that the third number is the largest
  print(num3, "is the largest")
# test cases
"""
Enter the first number:2
Enter the second number:-3
Enter the third number:-1
2 is the largest.
"""
"""
Enter the first number:5
Enter the second number:9
Enter the third number:0
9 is the largest
"""
"""
Enter the first number:1
Enter the second number:2
Enter the third number:3
3 is the largest
"""
"""
Enter the first number:1
Enter the second number:1
Enter the third number:1
1 is the largest.
"""
"""
Enter the first number:a
Please enter a valid integer input
Enter the first number:1
Enter the second number:2
Enter the third number:3
3 is the largest
"""
"""
Enter the first number:1
Enter the second number:a
Please enter a valid integer input
Enter the first number:2
Enter the second number:3
Enter the third number:4
4 is the largest
"""
"""
Enter the first number:1
Enter the second number:2
Enter the third number:c
Please enter a valid integer input
Enter the first number:1
Enter the second number:2
Enter the third number:3
3 is the largest
"""