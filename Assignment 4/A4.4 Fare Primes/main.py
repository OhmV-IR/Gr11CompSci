# A4.4 Fare Primes
# REDACTED(I <3 not doxxing myself)
# Find all fare primes(primes that when all their digits are rotated, they are still a prime number) and print out the results

# Define a function to check if a number is prime
def IsPrime(n):
    # For every number starting at 2 up to the number that we are checking,
    for i in range(2,n):
        # If the current number divides out evenly
        if n % i == 0:
            # The number is not prime so we return false
            return False
    # If no even divisor is found, return True
    return True

# Infinite loop
while True:
    # If input handling fails, do not crash the program
    try:
        # Get a maximum as an integer from the user
        max = int(input("Please enter an integer: "))
    # If input handling fails
    except:
        # Print that the input is invalid and loop again to get new input
        print("This is not a valid input.")
    else:
        # Verify that the maximum value is at least 2
        if max > 1:
            # If so, exit the loop and move to the main function of the program
            break
        else:
            # Otherwise, loop again to get new input
            print("Please enter an integer greater than 1.")

# Intialize a list that will have all the prime numbers between 2 and the maximum
primeslist = []
# Loop from 2 to the maximum number
for i in range(2,max+1):
    # If the current number is a prime number
    if IsPrime(i):
        # Add it to the list of prime numbers
        primeslist.append(i)

# Intialize a list that will have all the fare primes between 2 and the maximum
fareprimes = []
# For every prime in the list of primes
for a in range(0,len(primeslist)):
    # Convert the number into a list of characters(which are the digits of the number)
    digitsPrime = list(str(primeslist[a]))
    # Initialize a bool to true
    isFarePrime = True
    # For every digit in the prime number
    for b in range(0,len(digitsPrime)):
        # Insert the last digit that we stored at the start of the prime
        digitsPrime.insert(0, digitsPrime[len(digitsPrime) - 1])
        # Remove the last digit of the prime
        digitsPrime.pop()
        # If the shifted prime number is no loner a prime number
        if IsPrime(int("".join(digitsPrime))) == False:
            # The number is not a fare prime
            isFarePrime = False
            # Exit the loop, no need to check the other shifts
            break
    # If the number is a fare prime
    if isFarePrime:
        # Add it to the list of fare primes
        fareprimes.append(primeslist[a])

# Print all the fare primes that were found
print("The fare prime(s) between 2 and", max, "are ", end="")
print(*fareprimes, sep=", ")

# Test cases
"""
Please enter an integer: 197
The fare prime(s) between 2 and 197 are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197
"""
"""
Please enter an integer: text
This is not a valid input.
Please enter an integer: $!@(@#
This is not a valid input.
Please enter an integer: 197
The fare prime(s) between 2 and 197 are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197
"""
"""
Please enter an integer: 100000
The fare prime(s) between 2 and 100000 are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371
"""
"""
Please enter an integer: 1
Please enter an integer greater than 1.
Please enter an integer: -4
Please enter an integer greater than 1.
Please enter an integer: 3
The fare prime(s) between 2 and 3 are 2, 3
"""
"""
Please enter an integer: 256
The fare prime(s) between 2 and 256 are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199
"""