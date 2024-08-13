# L2.01 While loops
# REDACTED(I <3 not doxxing myself)
# Get a number from the user and keep squaring and printing it until the squaree is above 9000, then print the final square

# Get a number from the user
number = int(input("Please enter a number:"))
# Repeat until the square is over 9000
while number <= 9000:
    # Square the number
    number = number ** 2
    # Print the squared number
    print(number)
# The program will exit once the square is over 9000, which causes the while loop to terminate
    
# Test cases
"""
Please enter a number: 4
16
256
65536
"""
"""
Please enter a number: 7
49
2401
5764801
"""
"""
Please enter a number: -8
64
4096
16777216
"""
"""
Please enter a number: 256
65536
"""
"""
Please enter a number: -256
65536
"""
"""
Please enter a number: 9001
"""
"""
Please enter a number: -9001
81018001
"""