# L1.3 Input with Input
# REDACTED(I <3 not doxxing myself)
# Get the age of the user and tell the user how old they will be next year

# Loop the instruction to ask for input and convert it until we receive a valid input
while True:
    try:
        # ask the user to enter their age and try to convert it to an integer
        age = int(input("Please enter your age:"))
    except:
        # If converting the user's input to an integer fails, tell them to enter a valid input
        print("Please enter a valid integer input")
    else:
        # If a valid input is entered and it is successfully converted to an integer, exit the loop
        break
# Print how old the user will be next year
print("You will be", age + 1, "years old next year.")
# test cases
"""
Please enter your age: 3
You will be 4 years old next year.
"""
"""
Please enter your age: -1
You will be 0 years old next year.
"""
"""
Please enter your age: 0
You will be 1 years old next year.
"""