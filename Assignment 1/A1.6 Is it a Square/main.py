# A1.6 Is it a Square?
# REDACTED(I <3 not doxxing myself)
# Given 4 points, determine whether or not those 4 points form a square

# Make 4 lists that will store the coordinates in x,y, used format
coord1 = []
coord2 = []
coord3 = []
coord4 = []

# Get the coordinates of the points from the user and store them in the array
coord1.append(int(input("Enter the first point's x coordinate:")))
coord1.append(int(input("Enter the first point's y coordinate:")))
coord2.append(int(input("Enter the second point's x coordinate:")))
coord2.append(int(input("Enter the second point's y coordinate:")))
coord3.append(int(input("Enter the third point's x coordinate:")))
coord3.append(int(input("Enter the third point's y coordinate:")))
coord4.append(int(input("Enter the fourth point's x coordinate:")))
coord4.append(int(input("Enter the fourth point's y coordinate:")))

coord1Sorted = [] # top right point of the square
coord2Sorted = [] # top left point of the square
coord3Sorted = [] # bottom right point of the square
coord4Sorted = [] # bottom left point of the square

# If coord1 has the highest x and y values, it is the top right point and therefore coord1Sorted
if coord1[0] >= coord2[0] and coord1[0] >= coord3[0] and coord1[0] >= coord4[0] and coord1[1] >= coord2[1] and coord1[1] >= coord3[1] and coord1[1] >= coord4[1]:
    coord1Sorted = coord1
# If coord2 has the highest x and y values, it is the top right point and therefore coord1Sorted
elif coord2[0] >= coord1[0] and coord2[0] >= coord3[0] and coord2[0] >= coord4[0] and coord2[1] >= coord1[1] and coord2[1] >= coord3[1] and coord2[1] >= coord4[1]:
    coord1Sorted = coord2
# If coord3 has the highest x and y values, it is the top right point and therefore coord1Sorted
elif coord3[0] >= coord1[0] and coord3[0] >= coord2[0] and coord3[0] >= coord4[0] and coord3[1] >= coord1[1] and coord3[1] >= coord2[1] and coord3[1] >= coord4[1]:
    coord1Sorted = coord3
# If coord4 has the highest x and y values, it is the top right point and therefore coord1Sorted
elif coord4[0] >= coord1[0] and coord4[0] >= coord2[0] and coord4[0] >= coord4[0] and coord4[1] >= coord1[1] and coord4[1] >= coord2[1] and coord4[1] >= coord3[1]:
    coord1Sorted = coord4
# Square is rotated or rhombus is present
else:
    # If coord1 has the highest y value, it will serve as our top-right point(coord1Sorted)
    if coord1[1] > coord2[1] and coord1[1] > coord3[1] and coord1[1] > coord4[1]:
        coord1Sorted = coord1
    # If coord2 has the highest y value, it will serve as our top-right point(coord1Sorted)
    elif coord2[1] > coord1[1] and coord2[1] > coord3[1] and coord2[1] > coord4[1]:
        coord1Sorted = coord2
    # If coord3 has the highest y value, it will serve as our top-right point(coord1Sorted)
    elif coord3[1] > coord1[1] and coord3[1] > coord2[1] and coord3[1] > coord4[1]:
        coord1Sorted = coord3
    # If coord4 has the highest y value, it will serve as our top-right point(coord1Sorted)
    else:
        coord1Sorted = coord4

# If coord1 has the lowest x and highest y values, it is the top left point and therefore coord2Sorted
if coord1[0] <= coord2[0] and coord1[0] <= coord3[0] and coord1[0] <= coord4[0] and coord1[1] >= coord2[1] and coord1[1] >= coord3[1] and coord1[1] >= coord4[1]:
    coord2Sorted = coord1
# If coord2 has the lowest x and highest y values, it is the top left point and therefore coord2Sorted
elif coord2[0] <= coord1[0] and coord2[0] <= coord3[0] and coord2[0] <= coord4[0] and coord2[1] >= coord1[1] and coord2[1] >= coord3[1] and coord2[1] >= coord4[1]:
    coord2Sorted = coord2
# If coord3 has the lowest x and highest y values, it is the top left point and therefore coord2Sorted
elif coord3[0] <= coord2[0] and coord3[0] <= coord1[0] and coord3[0] <= coord4[0] and coord3[1] >= coord1[1] and coord3[1] >= coord2[1] and coord3[1] >= coord4[1]:
    coord2Sorted = coord3
# If coord4 has the lowest x and highest y values, it is the top left point and therefore coord2Sorted
elif coord4[0] <= coord2[0] and coord4[0] <= coord1[0] and coord4[0] <= coord4[0] and coord4[1] >= coord1[1] and coord4[1] >= coord2[1] and coord4[1] >= coord3[1]:
    coord2Sorted= coord4
# Square is rotated or rhombus is present
else:
    # If coord1 has the lowest x value, it will serve as our coord2Sorted(top-left point)
    if coord1[0] < coord2[0] and coord1[0] < coord3[0] and coord1[0] < coord4[0]:
        coord2Sorted = coord1
    # If coord2 has the lowest x value, it will serve as our coord2Sorted(top-left point)
    elif coord2[0] < coord1[0] and coord2[0] < coord3[0] and coord2[0] < coord4[0]:
        coord2Sorted = coord2
    # If coord3 has the lowest x value, it will serve as our coord2Sorted(top-left point)
    elif coord3[0] < coord1[0] and coord3[0] < coord2[0] and coord3[0] < coord4[0]:
        coord2Sorted = coord3
    # If coord4 has the lowest x value, it will serve as our coord2Sorted(top-left point)
    else:
        coord2Sorted = coord4

# If coord1 has the lowest y and highest x values, it is the bottom right point and therefore coord3Sorted
if coord1[1] <= coord2[1] and coord1[1] <= coord3[1] and coord1[1] <= coord4[1] and coord1[0] >= coord2[0] and coord1[0] >= coord3[0] and coord1[0] >= coord4[0]:
    coord3Sorted = coord1
# If coord2 has the lowest y and highest x values, it is the bottom right point and therefore coord3Sorted
elif coord2[1] <= coord1[1] and coord2[1] <= coord3[1] and coord2[1] <= coord4[1] and coord2[0] >= coord1[0] and coord2[0] >= coord3[0] and coord2[0] >= coord4[0]:
    coord3Sorted = coord2
# If coord3 has the lowest y and highest x values, it is the bottom right point and therefore coord3Sorted
elif coord3[1] <= coord1[1] and coord3[1] <= coord2[1] and coord3[1] <= coord4[1] and coord3[0] >= coord1[0] and coord3[0] >= coord2[0] and coord3[0] >= coord4[0]:
    coord3Sorted = coord3
# If coord4 has the lowest y and highest x values, it is the bottom right point and therefore coord3Sorted
elif coord4[1] <= coord1[1] and coord4[1] <= coord4[1] and coord4[1] <= coord4[1] and coord4[0] >= coord1[0] and coord4[0] >= coord2[0] and coord4[0] >= coord3[0]:
    coord3Sorted = coord4
# Square is rotated or rhombus is present
else:
    # If coord1 has the highest x value, it will serve as our coord3Sorted(bottom-right point)
    if coord1[0] > coord2[0] and coord1[0] > coord3[0] and coord1[0] > coord4[0]:
        coord3Sorted = coord1
    # If coord2 has the highest x value, it will serve as our coord3Sorted(bottom-right point)
    elif coord2[0] > coord1[0] and coord2[0] > coord3[0] and coord2[0] > coord4[0]:
        coord3Sorted = coord2
    # If coord3 has the highest x value, it will serve as our coord3Sorted(bottom-right point)
    elif coord3[0] > coord1[0] and coord3[0] > coord2[0] and coord3[0] > coord4[0]:
        coord3Sorted = coord3
    # If coord4 has the highest x value, it will serve as our coord3Sorted(bottom-right point)
    else:
        coord3Sorted = coord4

# If coord1 has the lowest x and y values, it is the bottom left point and therefore coord4Sorted
if coord1[1] <= coord2[1] and coord1[1] <= coord3[1] and coord1[1] <= coord4[1] and coord1[0] <= coord2[0] and coord1[0] <= coord3[0] and coord1[0] <= coord4[0]:
    coord4Sorted = coord1
# If coord2 has the lowest x and y values, it is the bottom left point and therefore coord4Sorted
elif coord2[1] <= coord1[1] and coord2[1] <= coord3[1] and coord2[1] <= coord4[1] and coord2[0] <= coord1[0] and coord2[0] <= coord3[0] and coord2[0] <= coord4[0]:
    coord4Sorted = coord2
# If coord3 has the lowest x and y values, it is the bottom left point and therefore coord4Sorted
elif coord3[1] <= coord1[1] and coord3[1] <= coord2[1] and coord3[1] <= coord4[1] and coord3[0] <= coord1[0] and coord3[0] <= coord2[0] and coord3[0] <= coord4[0]:
    coord4Sorted = coord3
# If coord3 has the lowest x and y values, it is the bottom left point and therefore coord4Sorted
elif coord4[1] <= coord1[1] and coord4[1] <= coord2[1] and coord4[1] <= coord4[1] and coord4[0] <= coord1[0] and coord4[0] <= coord2[0] and coord4[0] <= coord3[0]:
    coord4Sorted = coord4
# Square is rotated or rhombus is present
else:
    # If coord1 has the lowest y value, it will serve as our coord4Sorted(bottom-left point)
    if coord1[1] < coord2[1] and coord1[1] < coord3[1] < coord1[1] < coord4[1]:
        coord4Sorted = coord1
    # If coord2 has the lowest y value, it will serve as our coord4Sorted(bottom-left point)
    elif coord2[1] < coord1[1] and coord2[1] < coord3[1] and coord2[1] < coord4[1]:
        coord4Sorted = coord2
    # If coord3 has the lowest y value, it will serve as our coord4Sorted(bottom-left point)
    elif coord3[1] < coord1[1] and coord3[1] < coord2[1] and coord3[1] < coord4[1]:
        coord4Sorted = coord3
    # If coord4 has the lowest y value, it will serve as our coord4Sorted(bottom-left point)
    else:
        coord4Sorted = coord4

# Find the length of the 4 lines by doing the length of a line formula derived from the pythagorean theorem
line1Len = ((coord1Sorted[0] - coord3Sorted[0]) ** 2 + (coord1Sorted[1] - coord3Sorted[1]) ** 2) ** 0.5
line2Len = ((coord3Sorted[0] - coord4Sorted[0]) ** 2 + (coord3Sorted[1] - coord4Sorted[1]) ** 2) ** 0.5
line3Len = ((coord4Sorted[0] - coord2Sorted[0]) ** 2 + (coord4Sorted[1] - coord2Sorted[1]) ** 2) ** 0.5
line4Len = ((coord2Sorted[0] - coord1Sorted[0]) ** 2 + (coord2Sorted[1] - coord1Sorted[1]) ** 2) ** 0.5

# Get the length of  2 lines across the center of the shape, they should be equal if the shape is a squares
rhombusTestLine1 = ((coord1Sorted[0] - coord4Sorted[0]) ** 2 + (coord1Sorted[1] - coord4Sorted[1]) ** 2) ** 0.5
rhombusTestLine2 = ((coord2Sorted[0] - coord3Sorted[0]) ** 2 + (coord2Sorted[1] - coord3Sorted[1]) ** 2) ** 0.5

# If the perimeter lines are all of equal length and the 2 lines that go through the center connecting
# 2 opposite points of the shape are equal, then the shape formed by the coordinates is a square
if line1Len == line2Len and line1Len == line3Len and line1Len == line4Len and rhombusTestLine1 == rhombusTestLine2:
    # Print the coordinates that the user entered and state that they form a square
    print("The points (", coord1[0], ",",coord1[1],") , (", coord2[0], ",", coord2[1], ") , (", coord3[0], ",", coord3[1], ") and (", coord4[0], ",", coord4[1], ") form a square.")
# If the lines do not all have the same length or the lines passing through the center aren't
# equal, then the shape formed by the coordinates is not a square
else:
    # Print the coordinates that the user entered and state that they do not form a square
    print("The points (", coord1[0], ",",coord1[1],") , (", coord2[0], ",", coord2[1], ") , (", coord3[0], ",", coord3[1], ") and (", coord4[0], ",", coord4[1], ") do not form a square.")

# Test cases
"""
Enter the first point's x coordinate: 4
Enter the first point's y coordinate: 5
Enter the second point's x coordinate: 4
Enter the second point's y coordinate: 6
Enter the third point's x coordinate: 5
Enter the third point's y coordinate: 6
Enter the fourth point's x coordinate: 5
Enter the fourth point's y coordinate: 5
The points ( 4 , 5 ) , ( 4 , 6 ) , ( 5 , 6 ) and ( 5 , 5 ) form a square.
"""
"""
Enter the first point's x coordinate: 4
Enter the first point's y coordinate: 5
Enter the second point's x coordinate: 5
Enter the second point's y coordinate: 4
Enter the third point's x coordinate: 6
Enter the third point's y coordinate: 5
Enter the fourth point's x coordinate: 5
Enter the fourth point's y coordinate: 6
The points ( 4 , 5 ) , ( 5 , 4 ) , ( 6 , 5 ) and ( 5 , 6 ) form a square.
"""
"""
Enter the first point's x coordinate: 7
Enter the first point's y coordinate: 8
Enter the second point's x coordinate: 7
Enter the second point's y coordinate: 4
Enter the third point's x coordinate: 2
Enter the third point's y coordinate: 6
Enter the fourth point's x coordinate: 12
Enter the fourth point's y coordinate: 6
The points ( 7 , 8 ) , ( 7 , 4 ) , ( 2 , 6 ) and ( 12 , 6 ) do not form a square.
"""
"""
Enter the first point's x coordinate: 4
Enter the first point's y coordinate: 6
Enter the second point's x coordinate: 5
Enter the second point's y coordinate: 5
Enter the third point's x coordinate: 4
Enter the third point's y coordinate: 5
Enter the fourth point's x coordinate: 5
Enter the fourth point's y coordinate: 6
The points ( 4 , 6 ) , ( 5 , 5 ) , ( 4 , 5 ) and ( 5 , 6 ) form a square.
"""
"""
Enter the first point's x coordinate: 7
Enter the first point's y coordinate: 8
Enter the second point's x coordinate: 2
Enter the second point's y coordinate: 6
Enter the third point's x coordinate: 12
Enter the third point's y coordinate: 6
Enter the fourth point's x coordinate: 7
Enter the fourth point's y coordinate: 4
The points ( 7 , 8 ) , ( 2 , 6 ) , ( 12 , 6 ) and ( 7 , 4 ) do not form a square.
"""
"""
Enter the first point's x coordinate: 6
Enter the first point's y coordinate: 5
Enter the second point's x coordinate: 5
Enter the second point's y coordinate: 6
Enter the third point's x coordinate: 4
Enter the third point's y coordinate: 5
Enter the fourth point's x coordinate: 5
Enter the fourth point's y coordinate: 4
The points ( 6 , 5 ) , ( 5 , 6 ) , ( 4 , 5 ) and ( 5 , 4 ) form a square.
"""
"""
Enter the first point's x coordinate: 5
Enter the first point's y coordinate: 10
Enter the second point's x coordinate: 10
Enter the second point's y coordinate: 10
Enter the third point's x coordinate: 5
Enter the third point's y coordinate: 3
Enter the fourth point's x coordinate: 10
Enter the fourth point's y coordinate: 3
The points ( 5 , 10 ) , ( 10 , 10 ) , ( 5 , 3 ) and ( 10 , 3 ) do not form a square.
"""
"""
Enter the first point's x coordinate: 7
Enter the first point's y coordinate: 5
Enter the second point's x coordinate: 10
Enter the second point's y coordinate: 10
Enter the third point's x coordinate: 3
Enter the third point's y coordinate: 3
Enter the fourth point's x coordinate: 4
Enter the fourth point's y coordinate: 9
The points ( 7 , 5 ) , ( 10 , 10 ) , ( 3 , 3 ) and ( 4 , 9 ) do not form a square.
"""
"""
Enter the first point's x coordinate: 7
Enter the first point's y coordinate: 7
Enter the second point's x coordinate: 7
Enter the second point's y coordinate: 1
Enter the third point's x coordinate: 4
Enter the third point's y coordinate: 4
Enter the fourth point's x coordinate: 10
Enter the fourth point's y coordinate: 4
The points ( 7 , 7 ) , ( 7 , 1 ) , ( 4 , 4 ) and ( 10 , 4 ) form a square.
"""
"""
Enter the first point's x coordinate: 7
Enter the first point's y coordinate: 10
Enter the second point's x coordinate: 4
Enter the second point's y coordinate: 4
Enter the third point's x coordinate: 7
Enter the third point's y coordinate: -1
Enter the fourth point's x coordinate: 10
Enter the fourth point's y coordinate: 4
The points ( 7 , 10 ) , ( 4 , 4 ) , ( 7 , -1 ) and ( 10 , 4 ) do not form a square.
"""