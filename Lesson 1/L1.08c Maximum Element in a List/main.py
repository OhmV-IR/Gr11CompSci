# L1.08c Maximum Element in a List
# REDACTED(I <3 not doxxing myself)
# Get a list of numbers from the user and find the biggest one

# Create an empty list of numbers
numbers = []

# Add 4 numbers of the user's choosing to the list
numbers.append(int(input("Enter a number:")))
numbers.append(int(input("Enter a second number:")))
numbers.append(int(input("Enter a third number:")))
numbers.append(int(input("Enter a fourth number:")))

# Create a new list with 4 spaces to put the sorted numbers in
numbersSorted = [0,0,0,0]
# If the second number is smaller than the 1st,
if numbers[1] <= numbers[0]:
    # Make the 2nd number first and the 1st number second
    numbersSorted[0] = numbers[1]
    numbersSorted[1] = numbers[0]
# If the first number is smaller than the first,
else:
    # Make the 1st number first and the 2nd number second
    numbersSorted[0] = numbers[0]
    numbersSorted[1] = numbers[1]
# If the third number is smaller than the first one(the smallest one thus far),
if numbers[2] <= numbersSorted[0]:
    # Shift all the numbers up and insert the 3rd number at the beginning
    numbersSorted[2] = numbersSorted[1]
    numbersSorted[1] = numbersSorted[0]
    numbersSorted[0] = numbers[2]
# If the third number is not smaller than the first one, check if it smaller than the second one
elif numbers[2] <= numbersSorted[1]:
    # If it is smaller than the second one, move the second one up and insert the 3rd number second
    numbersSorted[2] = numbersSorted[1]
    numbersSorted[1] = numbers[2]
# If none of these conditions are true, it is the biggest number so far,
else:
    # and we should insert it third
    numbersSorted[2] = numbers[2]
# If the 4th number is the smallest so far,
if numbers[3] <= numbersSorted[0]:
    # Move all the other numbers up and insert it in the first spot
    numbersSorted[3] = numbersSorted[2]
    numbersSorted[2] = numbersSorted[1]
    numbersSorted[1] = numbersSorted[0]
    numbersSorted[0] = numbers[3]
# If the 4th number is smaller than the second number, 
elif numbers[3] <= numbersSorted[1]:
    # Move the second and third numbers up and insert the 4th number second
    numbersSorted[3] = numbersSorted[2]
    numbersSorted[2] = numbersSorted[1]
    numbersSorted[1] = numbers[3]
# If the number is smaller than the third sorted number,
elif numbers[3] <= numbersSorted[2]:
    # Move the third number up and insert the 4th number in the third spot
    numbersSorted[3] = numbersSorted[2]
    numbersSorted[2] = numbers[3]
# If all of these conditions fail, the 4th number is the biggest number so far so we insert it fourth
else:
    numbersSorted[3] = numbers[3]
print("The biggest number in the list is", numbersSorted[3])

# Test cases
"""
Enter a number:1
Enter a second number:2
Enter a third number:3
Enter a fourth number:4
The biggest number in the list is 4
"""
"""
Enter a number:0
Enter a second number:0
Enter a third number:0
Enter a fourth number:0
The biggest number in the list is 0
"""
"""
Enter a number:-1
Enter a second number:-2
Enter a third number:-3
Enter a fourth number:-4
The biggest number in the list is -1
"""
"""
Enter a number:4
Enter a second number:3
Enter a third number:2
Enter a fourth number:1
The biggest number in the list is 4
"""
"""
Enter a number:7
Enter a second number:6
Enter a third number:8
Enter a fourth number:7
The biggest number in the list is 8
"""
"""
Enter a number:9
Enter a second number:9
Enter a third number:2
Enter a fourth number:0
The biggest number in the list is 9
"""