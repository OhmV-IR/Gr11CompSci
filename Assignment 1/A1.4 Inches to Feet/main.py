# A1.4 Inches to Feet
# REDACTED(I <3 not doxxing myself)
# Given the number of inches, display the number of feet and inches

# Gather the number of inches from the user
inches = int(input("Please enter the number of inches:"))
# Get the number of feet by dividing by 12 and removing the decimal
feet = inches // 12
# Get the number of inches remaining by getting the remainder of dividing by 12(the decimal we threw away)
remainingInches = inches % 12
# If there is only 1 inch,
if inches == 1:
    # Only print the singular form of inch
    print(inches, "inch")
# If there are multiple inches,
elif inches < 12 and inches > 0:
    # Only print the plural form of inches
    print(inches, "inches")
# If there is only 1 foot and no extra inches,
elif feet == 1 and remainingInches == 0:
    # Only print the singular form of feet
    print(feet, "foot")
# If there is only 1 foot and 1 extra inch,
elif feet == 1 and remainingInches == 1:
    # Print the singular form of feet and inches
    print(feet, "foot", remainingInches, "inch")
# If there is only 1 foot and more than 1 extra inch
elif feet == 1:
    # Print the singular form of feet and plural form of inches
    print(feet, "foot", remainingInches, "inches")
# If there is more than 1 foot and no extra inches,
elif feet > 1 and remainingInches == 0:
    # Print only the plural form of feet
    print(feet, "feet")
# If there is more than 1 foot and 1 extra inch
elif feet > 1 and remainingInches == 1:
    # Print the plural form of feet and singular form of inches
    print(feet, "feet", remainingInches, "inch")
# If there is more than 1 foot and more than 1 extra inch
elif feet > 1 and remainingInches > 1:
    # Print the plural form of feet and inches
    print(feet, "feet", remainingInches, "inches")
# If none of the above conditions match the input,
else:
    # Print that the input is invalid
    print("This is not a valid length.")
# test cases
"""
Please enter the number of inches: 1
1 inch
"""
"""
Please enter the number of inches: 2
2 inches
"""
"""
Please enter the number of inches: 12
1 foot
"""
"""
Please enter the number of inches: 13
1 foot 1 inch
"""
"""
Please enter the number of inches: 14
1 foot 2 inches
"""
"""
Please enter the number of inches: 24
2 feet
"""
"""
Please enter the number of inches: 25
2 feet 1 inch
"""
"""
Please enter the number of inches: 26
2 feet 2 inches
"""
"""
Please enter the number of inches: -1
This is not a valid length.
"""