# A2.3 Diamond of Stars
# REDACTED(I <3 not doxxing myself)
# Print a diamond with pound signs a number of rows given by the user

# Infinite loop
while True:
    # If an error occurs, we will move to the except block instead of crashing
    try:
        # Try to set an input variable by converting the user's input to an integer
        numberOfRows = int(input("Please enter the number of rows:"))
    # If we fail to convert the user's input to an integer,
    except ValueError:
        # Print that the user has not entered an integer and loop again to get new input
        print("The input you entered is not an integer. Please enter an integer.")
    # If we convert the user's input to an integer successfully
    else:
        # Check that there are more than 2 rows
        if numberOfRows > 0:
            # Exit the infinite loop and continue with the program
            break
        # If the input is invalid because the number of rows is not greater than 2
        else:
            # Print that the user has not entered a valid input and loop again to get new input
            print("This is not a valid input. An integer greater than 0 is required.")

# Get the maximum number of spaces by getting the floor of dividing the number of rows by 2
maxSpaces = int((numberOfRows - (numberOfRows % 2)) / 2)
# If the number of rows is even,
if(numberOfRows % 2 == 0):
    # Decrease maxSpaces by 1 to account for the additional middle row
    maxSpaces = maxSpaces - 1
# Account for 2 rows edge case
if numberOfRows == 2:
    # Print 2 pound signs on top of each other
    print("#")
    print("#")
# Account for 1 row edge case
elif numberOfRows == 1:
    # Print a singular pound sign
    print("#")
# For all other cases
else:
    # Opening pound sign to start the diamond
    print(maxSpaces * " " + "#")

    # Print the 2nd row up to middle row(s)
    for i in range(1, maxSpaces):
        # Reduce the amount of spaces that we print on the left by 1 each row and print 2 more spaces in the middle
        # each row, starting at 1 space
        print((maxSpaces - i) * " " + "#" + (i-1) * " " + " " + (i-1) * " " + "#")

    # Middle row(s)
    # Always print the first middle row by printing 1 diamond at the left-most point and 1 after double the (maximum number of spaces - 1) + 1 space
    print("#" + (maxSpaces - 1) * " " + " " + (maxSpaces - 1) * " " + "#")
    # If the number is even, 2 middle rows are needed,
    if(numberOfRows % 2 == 0):
        # this row is printed in the exact same way as the first middle row
        print("#" + (maxSpaces - 1) * " " + " " + (maxSpaces - 1) * " " + "#")

    # If the number of rows is odd,
    if(numberOfRows % 2 != 0):
        # Iterate over after middle row to 2nd last row, i starts high and then decreases until it gets to 0
        for i in range(numberOfRows - maxSpaces - 3, -1, -1):
            # subtract maxspaces from i, make the number positive and then subtract 1 to get the number of spaces before the 1st pound sign
            # then simply add 2i + 1 spaces before the 2nd pound sign
            print(int((((i-maxSpaces) ** 2)** 0.5) - 1) * " " + "#" + i * 2 * " " + " " + "#")
    # If the number of rows is even,
    else:
        # Iterate over after middle row to 2nd last row, i starts high and then decreases until it gets to 0
        for i in range(numberOfRows - maxSpaces - 2, 1, -1):
            print(int((((i-maxSpaces-2) ** 2)** 0.5) - 1) * " " + "#" + (i-2) * " " + " " + (i-2) * " " + "#")

    # Closing pound sign
    print((maxSpaces) * " " + "#")

# Test cases
"""
Please enter the number of rows: 2
#
#
"""
"""
Please enter the number of rows: 1
#
"""
"""
Please enter the number of rows: 15
       #
      # #
     #   #
    #     #
   #       #
  #         #
 #           #
#             #
 #           #
  #         #
   #       #
    #     #
     #   #
      # #
       #
"""
"""
Please enter the number of rows: 14
      #
     # #
    #   #
   #     #
  #       #
 #         #
#           #
#           #
 #         #
  #       #
   #     #
    #   #
     # #
      #
"""
"""
Please enter the number of rows: 7
   #
  # #
 #   #
#     #
 #   #
  # #
   #
"""
"""
Please enter the number of rows: 8 
   #
  # #
 #   #
#     #
#     #
 #   #
  # #
   #
"""
"""
Please enter the number of rows: 3
 #
# #
 #
"""
"""
Please enter the number of rows: f
The input you entered is not an integer. Please enter an integer.
Please enter the number of rows: f
The input you entered is not an integer. Please enter an integer.
Please enter the number of rows: 6
  #
 # #
#   #
#   #
 # #
  #
"""
"""
Please enter the number of rows: !@
The input you entered is not an integer. Please enter an integer.
Please enter the number of rows: !@6
The input you entered is not an integer. Please enter an integer.
Please enter the number of rows: 7
   #
  # #
 #   #
#     #
 #   #
  # #
   #
"""
"""
Please enter the number of rows: 100
                                                 #
                                                # #
                                               #   #
                                              #     #
                                             #       #
                                            #         #
                                           #           #
                                          #             #
                                         #               #
                                        #                 #
                                       #                   #
                                      #                     #
                                     #                       #
                                    #                         #
                                   #                           #
                                  #                             #
                                 #                               #
                                #                                 #
                               #                                   #
                              #                                     #
                             #                                       #
                            #                                         #
                           #                                           #
                          #                                             #
                         #                                               #
                        #                                                 #
                       #                                                   #
                      #                                                     #
                     #                                                       #
                    #                                                         #
                   #                                                           #
                  #                                                             #
                 #                                                               #
                #                                                                 #
               #                                                                   #
              #                                                                     #
             #                                                                       #
            #                                                                         #
           #                                                                           #
          #                                                                             #
         #                                                                               #
        #                                                                                 #
       #                                                                                   #
      #                                                                                     #
     #                                                                                       #
    #                                                                                         #
   #                                                                                           #
  #                                                                                             #
 #                                                                                               #
#                                                                                                 #
#                                                                                                 #
 #                                                                                               #
  #                                                                                             #
   #                                                                                           #
    #                                                                                         #
     #                                                                                       #
      #                                                                                     #
       #                                                                                   #
        #                                                                                 #
         #                                                                               #
          #                                                                             #
           #                                                                           #
            #                                                                         #
             #                                                                       #
              #                                                                     #
               #                                                                   #
                #                                                                 #
                 #                                                               #
                  #                                                             #
                   #                                                           #
                    #                                                         #
                     #                                                       #
                      #                                                     #
                       #                                                   #
                        #                                                 #
                         #                                               #
                          #                                             #
                           #                                           #
                            #                                         #
                             #                                       #
                              #                                     #
                               #                                   #
                                #                                 #
                                 #                               #
                                  #                             #
                                   #                           #
                                    #                         #
                                     #                       #
                                      #                     #
                                       #                   #
                                        #                 #
                                         #               #
                                          #             #
                                           #           #
                                            #         #
                                             #       #
                                              #     #
                                               #   #
                                                # #
                                                 #
"""