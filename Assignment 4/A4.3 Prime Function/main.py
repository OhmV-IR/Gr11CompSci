# A4.3 Prime Function
# REDACTED(I <3 not doxxing myself)
# Use code from L1.09 and write a function that takes an integer and determines if the number is prime or not
# returning true/false. Use the function and a loop to print the two largest primes less than or equal to a user-defined integer

# Define a function that takes a paramater of n as an integer to check if it is a prime number or not
def IsPrime(n):
    # For every number starting at 2 up to the number that we are checking
    for currentdivisor in range(2,n):
        # If it divides evenly
        if n % currentdivisor == 0:
            # return false as the number is not a prime number
            return False
    # If all the divisors do not divide evenly, return true as the number is a prime number
    return True

# Infinite loop
while True:
    # If handling the input fails, do not crash the program
    try:
        # Get a maximum integer from the user
        max = int(input("Please enter an integer: "))
    # If input handling fails
    except:
        # Print that the input is invalid and loop again to get new input
        print("This is not a valid input")
    # If input handling is successful
    else:
        if max > 1:
            break
        else:
            print("Please enter an integer greater than 1.")

# Initialize a list that will contain all the prime numbers we find
primelist = []
# For every number starting at 2 up to and including the maximum,
for i in range(2,max+1):
    # If the number is a prime number,
    if IsPrime(i):
        # Add it to the list of prime numbers
        primelist.append(i)

# Get the number of prime numbers in the list
numberofprimes = len(primelist)
# If no prime numbers were found,
if numberofprimes == 0:
    # Print that no prime numbers were found
    print("No prime numbers found.")
# If 1 prime number was found
elif numberofprimes == 1:
    # Print the prime number
    print(primelist[numberofprimes-1])
# Otherwise(if there were 2+ prime numbers found)
else:
    # Print the second last prime number in the list
    print(primelist[numberofprimes - 2])
    # Print the last prime number in the list
    print(primelist[numberofprimes - 1])

# Test cases
"""
Please enter an integer: 4
2
3
"""
"""
Please enter an integer: textinput
This is not a valid input
Please enter an integer: 4
2
3
"""
"""
Please enter an integer: #@(!
This is not a valid input
Please enter an integer: 4
2
3
"""
"""
Please enter an integer: 2
2
"""
"""
Please enter an integer: 100000
99989
99991
"""
"""
Please enter an integer: 1
Please enter an integer greater than 1.
Please enter an integer: -2
Please enter an integer greater than 1.
Please enter an integer: 6
3
5
"""