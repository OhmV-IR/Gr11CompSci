# L1.4 Branching 1
# REDACTED(I <3 not doxxing myself)
# Find the letter grade given a percentage mark from the user

# Get the number mark from the user
mark = int(input("Enter a mark:"))
# If the mark is less than or equal to 100 and greater than or equal to 80
if mark <= 100 and mark >= 80:
    # Print that the mark is equivalent to an A letter grade
    print("A mark of", mark, "is an A.")
# If the mark is less than 80 and greater than or equal to 70
elif mark < 80 and mark >= 70:
    # Print that the mark is equivalent to an B letter grade
    print("A mark of", mark, "is a B.")
# If the mark is less than 70 and greater than or equal to 60
elif mark < 70 and mark >= 60:
    # Print that the mark is equivalent to an C letter grade
    print("A mark of", mark, "is a C.")
# If the mark is less than 60 and greater than or equal to 50
elif mark < 60 and mark >= 50:
    # Print that the mark is equivalent to an D letter grade
    print("A mark of", mark, "is a D.")
# If the mark is less than 50 and greater than or equal to zero
elif mark < 50 and mark >= 0:
    # Print that the mark is equivalent to an F letter grade
    print("A mark of", mark, "is an F.")
# If the mark has not triggered any of the above conditions, 
# it must be above 100 or below zero, in which case it is not valid
else:
    # Print that the mark is not valid
    print("This is not a valid mark.")

# Test cases
"""
Enter a mark:95
A mark of 95 is an A.
"""
"""
A mark of 78 is a B.
"""
"""
Enter a mark:66
A mark of 66 is a C.
"""
"""
Enter a mark:52
A mark of 52 is a D.
"""
"""
Enter a mark:43
A mark of 43 is an F.
"""
"""
Enter a mark:101
This is not a valid mark.
"""
"""
Enter a mark:-2
This is not a valid mark.
"""