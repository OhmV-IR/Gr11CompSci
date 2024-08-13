# L2.01b Different Types of Loops
# REDACTED(I <3 not doxxing myself)
# Turn the starter code below into a while loop instead of a for loop

# Starter code
"""
fruits = ["banana", "apple", "mango"]
i = 0
for fruit in fruits:
  print("Current fruit :", fruit)
"""

# Initialize the list of fruits
fruits = ["banana", "apple", "mango"]
# Initialize an incrementor that we use to terminate the while loop and iterate through the array of fruits
i = 0
# Until we reach the end of the array, keep looping
while (i < len(fruits)):
    # Print the current fruit using the i value to find the current fruit in the list
    print("Current fruit :", fruits[i])
    # Add 1 to the incrementor to move on to the next fruit
    i = i + 1

# Test cases
"""
Current fruit : banana
Current fruit : apple
Current fruit : mango
"""