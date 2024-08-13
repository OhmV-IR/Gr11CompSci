# L1.10 String Concatenation
# REDACTED(I <3 not doxxing myself)
# Get 3 strings from the user, concatenate them and then print it

# Get 3 strings from the user and store them in variables
first_string = input("Please enter the first string:")
second_string = input("Please enter the second string:")
third_string = input("Please enter the third string:")
# Concatenate the strings by adding them together
concatenated_string = first_string + second_string + third_string
# Print the concatenated string
print("The concatenated string is:", concatenated_string)

# Test cases
"""
Please enter the first string: Hello, 
Please enter the second string: welcome to
Please enter the third string: earth
The concatenated string is: Hello,welcome toearth
"""
"""
Please enter the first string: :0 !      
Please enter the second string: ;]
Please enter the third string: :k
The concatenated string is: :0 !;]:k
"""
"""
Please enter the first string: 1 + 2
Please enter the second string: =  
Please enter the third string: 3
The concatenated string is: 1 + 2=3
"""
"""
Please enter the first string: Hello, welcome to earth!
Please enter the second string: 1 + 2 = 3
Please enter the third string: :)
The concatenated string is: Hello, welcome to earth!1 + 2 = 3:)
"""