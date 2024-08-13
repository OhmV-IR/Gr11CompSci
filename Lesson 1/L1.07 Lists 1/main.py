# L1.07 Lists 1
# REDACTED(I <3 not doxxing myself)
# Make a list of numbers 1-5 then append 6 then ask the user for a number to append 
# then ask the user for a number to replace 3 with. Finally, print the list of numbers

# Make a list of numbers 1-5
numbersList = [1,2,3,4,5]
# Add 6 to end of the list of numbers
numbersList.append(6)
# Append the number that the user enters to the list of numbers
numbersList.append(int(input("Enter an integer to append to the list:")))
# Replace the 3rd element(3) with the number that the user enters
numbersList[2] = int(input("Enter an integer to replace 3 with:"))
# Print the final list of numbers
print(numbersList)

# Test cases
"""
Enter an integer to append to the list: 0
Enter an integer to replace 3 with: 0
[1, 2, 0, 4, 5, 6, 0]
"""
"""
Enter an integer to append to the list: 1
Enter an integer to replace 3 with: 2
[1, 2, 2, 4, 5, 6, 1]
"""
"""
Enter an integer to append to the list: -2
Enter an integer to replace 3 with: -8
[1, 2, -8, 4, 5, 6, -2]
"""