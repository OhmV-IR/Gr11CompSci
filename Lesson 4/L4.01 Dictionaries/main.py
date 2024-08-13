# L4.01 Dictionaries
# REDACTED(I <3 not doxxing myself)
# Get a list of items and prices from the user until the user enters a blank item. Then ask the user for
# items and print their prices until the user enters a blank item, print a dollar sign and the total value of all items
# You should be able to not set a price for an item and the program will print "No price for that item" when the user tries to print it

# Initialize an empty dictionary to store the prices of all the items
prices = {}
# Infinite loop
while True:
    # If we fail converting the price input to a float, do not crash the program
    try:
        # Get an item to add a price to from the user
        itemInput = input("Please enter an item:")
        # If the item is blank
        if itemInput == "":
            # Exit the infinite 
            break
        # If the item is not blank
        else:
            # Add a new item to the dictionary of prices by using the item name and asking the user for the price
            prices[itemInput] = float(input("Please enter a price for the item:"))
    # If converting the price given by the user to a float fails,
    except ValueError:
        # Print that the input is invalid and loop again to get new input
        print("Not a valid input.")

# Infinite loop
while True:
    # Get the item that the user would like to retrieve the price fors
    item = input("What item would you like to price?:")
    # If the item is blank
    if item == "":
        # Exit the infinite loop
        break
    # If the item is not blank
    else:
        # If the item has been given a price
        if item in prices:
            # Print the price of the item stored in the dictionary and loop again to get new input
            print(prices[item])
        # If the item has not been given a price
        else:
            # Print that there is no price for the item and loop again to get new input
            print("No price for that item.")

# Set the total price of all the items to 0 to start
total = 0
# For every key(item) in the dictionary of prices
for currentItem in prices:
    # Increment the total by the price of the current item
    total = total + prices[currentItem]
# Print a dollar sign but don't add the newline at the end so we can continue printing on the same line
print("$", end="")
# Print the total value of all the items next to the dollar sign
print(total)

# Test cases
"""
Please enter an item:grape 
Please enter a price for the item:3.45
Please enter an item:orange
Please enter a price for the item:9.22
Please enter an item:olive
Please enter a price for the item:1.25
Please enter an item:
What item would you like to price?:grape
3.45
What item would you like to price?:orange
9.22
What item would you like to price?:
$13.920000000000002
"""
"""
Please enter an item:apricot
Please enter a price for the item:1.25
Please enter an item:juice
Please enter a price for the item:3.75
Please enter an item:apple
Please enter a price for the item:2.12
Please enter an item:
What item would you like to price?:orange
No price for that item.
What item would you like to price?:apricot
1.25
What item would you like to price?:
$7.12
"""
"""
Please enter an item:apricot
Please enter a price for the item:notafloat
Not a valid input.
Please enter an item:apricot
Please enter a price for the item:1.25
Please enter an item:peach
Please enter a price for the item:9.8
Please enter an item:
What item would you like to price?:peach
9.8
What item would you like to price?:apricot
1.25
What item would you like to price?:
$11.05
"""
"""
Please enter an item:9998
Please enter a price for the item:5.43
Please enter an item:9999
Please enter a price for the item:4.45
Please enter an item:   
What item would you like to price?:9998
5.43
What item would you like to price?:9999
4.45
What item would you like to price?:10000
No price for that item.
What item would you like to price?:
$9.879999999999999
"""