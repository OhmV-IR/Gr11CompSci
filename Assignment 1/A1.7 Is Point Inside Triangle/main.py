# A1.7 Is Point Inside Triangle?
# REDACTED(I <3 not doxxing myself)
# Get 3 points from a user representing a triangle and a point to check if it is inside the triangle

# Inaccuracy value to account for the small inaccuracy of the float datatype
inaccuracy = 0.000000001

# Initialize coordinate arrays
coord1 = [] 
coord2 = []
coord3 = []
point = []

# Get inputs from the user for the 3 points of the triangle and the point to check
coord1.append(float(input("Enter the x coordinate of the first point:")))
coord1.append(float(input("Enter the y coordinate of the first point:")))
coord2.append(float(input("Enter the x coordinate of the second point:")))
coord2.append(float(input("Enter the y coordinate of the second point:")))
coord3.append(float(input("Enter the x coordinate of the third point:")))
coord3.append(float(input("Enter the y coordinate of the third point:")))
point.append(float(input("Enter the x coordinate of the point you want to check:")))
point.append(float(input("Enter the y coordinate of the point you want to check:")))

# Calculate the slope of the linear equation from coordinate 1 to coordinate 2
c1c2Slope = (coord1[1] - coord2[1]) / (coord1[0] - coord2[0])
# Calculate the slope of the linear equation from coordinate 2 to coordinate 3
c2c3Slope = (coord2[1] - coord3[1]) / (coord2[0] - coord3[0])
# Calculate the slope of the linear equation from coordinate 3 to coordinate 1
c3c1Slope = (coord3[1] - coord1[1]) / (coord3[0] - coord1[0])
# Calculate the y intercept of the linear equation from coordinate 1 to coordinate 2
c1c2YIntercept = coord1[1] - c1c2Slope * coord1[0]
# Calculate the y intercept of the linear equation from coordinate 2 to coordinate 3
c2c3YIntercept = coord2[1] - c2c3Slope * coord2[0]
# Calculate the y intercept of the linear equation from coordinate 3 to coordinate 1
c3c1YIntercept = coord3[1] - c3c1Slope * coord3[0]

# Find the bottom line of the triangle
# If the line between coord1 and coord2 of the triangle has the lowest slope, make it line1(the bottom line of the triangle)
if ((c1c2Slope ** 2) ** 0.5) < ((c2c3Slope ** 2) ** 0.5) and ((c1c2Slope ** 2) ** 0.5) < ((c3c1Slope ** 2) ** 0.5):
    line1Slope = c1c2Slope
    line1Y = c1c2YIntercept
# If the line between coord2 and coord3 of the triangle has the lowest slope, make it line1(the bottom line of the triangle)
elif ((c2c3Slope ** 2) ** 0.5) < ((c1c2Slope ** 2) ** 0.5) and ((c2c3Slope ** 2) ** 0.5) < ((c3c1Slope ** 2) ** 0.5):
    line1Slope = c2c3Slope
    line1Y = c2c3YIntercept
# If the line between coord3 and coord1 of the triangle has the lowest slope, make it line1(the bottom line of the triangle)
else:
    line1Slope = c3c1Slope
    line1Y = c3c1YIntercept

# Find the left line of the triangle
# If the line between coord1 and coord2 of the triangle has the highest slope, make it line2(the left line of the triangle)
if c1c2Slope > c2c3Slope and c1c2Slope > c3c1Slope:
    line2Slope = c1c2Slope
    line2Y = c1c2YIntercept
# If the line between coord2 and coord3 of the triangle has the highest slope, make it line2(the left line of the triangle)
elif c2c3Slope > c1c2Slope and c2c3Slope > c3c1Slope:
    line2Slope = c2c3Slope
    line2Y = c2c3YIntercept
# If the line between coord3 and coord1 of the triangle has the highest slope, make it line2(the left line of the triangle)
else:
    line2Slope = c3c1Slope
    line2Y = c3c1YIntercept

# Find the right line of the triangle
# If the line between coord1 and coord2 of the triangle has the lowest slope, make it line3(the right line of the triangle)
if c1c2Slope < c2c3Slope and c1c2Slope < c3c1Slope:
    line3Slope = c1c2Slope
    line3Y = c1c2YIntercept
# If the line between coord2 and coord3 of the triangle has the lowest slope, make it line3(the right line of the triangle)
elif c2c3Slope < c1c2Slope and c2c3Slope < c3c1Slope:
    line3Slope = c2c3Slope
    line3Y = c2c3YIntercept
# If the line between coord3 and coord1 of the triangle has the lowest slope, make it line3(the right line of the triangle)
else:
    line3Slope = c3c1Slope
    line3Y = c3c1YIntercept


# find top coordinate an find which side the x coord of the point is on and use the line corresponding to
# that side to find the high Y boundary(firstYBoundary)
# If the 1st coordinate is the highest point
if coord1[1] > coord2[1] and coord1[1] > coord3[1]:
    # If the point is on the right side of the first coordinate(highest point),
    if point[0] > coord1[0]:
        # Use the right line to find the high Y boundary
        firstYBoundary = point[0] * line3Slope + line3Y
    # If the point is on the left side of the first coordinate(highest point),
    elif point[0] < coord1[0]:
        # Use the left line to find the high Y boundary
        firstYBoundary = point[0] * line2Slope + line2Y
    # If the point has the same x value as the first coordinate(highest point)
    else:
        # Use the highest point as the high Y boundary
        firstYBoundary = coord1[1]

# If the second coordinate is the highest point,
elif coord2[1] > coord1[1] and coord2[1] > coord3[1]:
    # If the point is on the right side of the second coordinate(highest point)
    if point[0] > coord2[0]:
        # Use the right line of the triangle to find the high Y boundary
        firstYBoundary = point[0] * line3Slope + line3Y
    # If the point is on the left side of the second coorinate(highest point)
    elif point[0] < coord2[0]:
        # Use the left line to find the high Y boundary
        firstYBoundary = point[0] * line2Slope + line2Y
    # If the point is aligned with the second coordinate(highest point)
    else:
        # Use the second coordinate(highest point)'s y value as the high Y boundary
        firstYBoundary = coord2[1]

# If the third coordinate is the highest point
else:
    # If the point is on the right side of the third coordinate(highest point)
    if point[0] > coord3[0]:
        # Use the right line to find the high Y boundary
        firstYBoundary = point[0] * line3Slope + line3Y
    # If the point is on the left side of the third coordinate(highest point)
    elif point[0] < coord3[0]:
        # Use the left line to find the high Y boundary
        firstYBoundary = point[0] * line2Slope + line2Y
    # If the point is aligned with the third coordinate(highest point)
    else:
        # Use the y value of the third coordinate(highest point) as the high Y boundary
        firstYBoundary = coord3[1]

# Find the high X boundary by solving the linear equation with the y value of the point to find x on the right line of the triangle
firstXBoundary = (point[1] - line3Y) / line3Slope
# Find the low X boundary by solving the linear equation with the y value of the point to find x on the left line of the triangle
secondXBoundary = (point[1] - line2Y) / line2Slope
# Find the low Y boundary by solving the linear equation with the x value of the point to find y on the bottom line of the triangle
secondYBoundary = point[0] * line1Slope + line1Y

# Get absolute value of the difference between the boundary and the point
# This will be used to account for the small floating point inaccuracy later
firstXBoundaryDiff = ((point[0] - firstXBoundary) ** 2) ** 0.5
secondXBoundaryDiff = ((point[0] - secondXBoundary) ** 2) ** 0.5
firstYBoundaryDiff = ((point[1] - firstYBoundary) ** 2) ** 0.5
secondYBoundaryDiff = ((point[1] - secondYBoundary) ** 2) ** 0.5

# If the point's x value is higher than the high X boundary 
# and the difference is more than our accounted floating point inaccuracy,
if point[0] > firstXBoundary and firstXBoundaryDiff > inaccuracy:
    # Print that the point is not inside the triangle along with the coordinates of the point
    print("The point (", point[0], ",", point[1], ") is not inside the triangle")
# If the point's x value is lower than the low X boundary
# and the difference is more than our accounted floating point inaccuracy,
elif point[0] < secondXBoundary and secondXBoundaryDiff > inaccuracy:
    # Print that the point is not inside the triangle along with the coordinates of the point
    print("The point (", point[0], ",", point[1], ") is not inside the triangle")
# If the point's y value is higher than the high Y boundary
# and the difference is more than our accounted floating point inaccuracy,
elif point[1] > firstYBoundary and firstYBoundaryDiff > inaccuracy:
    # Print that the point is not inside the triangle along with the coordinates of the point
    print("The point (", point[0], ",", point[1], ") is not inside the triangle")
# If the point's y value is lower than the low Y boundary
# and the difference is more than our accounted floating point inaccuracy,
elif point[1] < secondYBoundary and secondYBoundaryDiff > inaccuracy:
    # Print that the point is not inside the triangle along with the coordinates of the point
    print("The point (", point[0], ",", point[1], ") is not inside the triangle")
# If none of the above conditions are true, the point must either be inside the triangle
# or on one of the lines that make up the triangle
else:
    # Print that the point is inside the triangle along with the coordinates of the point
    print("The point (", point[0], ",", point[1], ") is inside the triangle")

# Test cases: https://www.desmos.com/calculator/qoruuthqf0
"""
Enter the x coordinate of the first point: 0.2
Enter the y coordinate of the first point: 0.2
Enter the x coordinate of the second point: -0.333333333
Enter the y coordinate of the second point: 2.3333333333
Enter the x coordinate of the third point: -3
Enter the y coordinate of the third point: -3
Enter the x coordinate of the point you want to check: 0
Enter the y coordinate of the point you want to check: 0.5
The point ( 0.0 , 0.5 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: -0.33333333333
Enter the y coordinate of the first point: 2.3333333333
Enter the x coordinate of the second point: -3
Enter the y coordinate of the second point: -3
Enter the x coordinate of the third point: 0.2
Enter the y coordinate of the third point: 0.2
Enter the x coordinate of the point you want to check: 0
Enter the y coordinate of the point you want to check: 0.5
The point ( 0.0 , 0.5 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: -3
Enter the y coordinate of the first point: -3
Enter the x coordinate of the second point: 0.2
Enter the y coordinate of the second point: 0.2
Enter the x coordinate of the third point: -0.33333333333333333
Enter the y coordinate of the third point: 2.3333333333333333
Enter the x coordinate of the point you want to check: 0
Enter the y coordinate of the point you want to check: 0.5
The point ( 0.0 , 0.5 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: 0.2
Enter the y coordinate of the first point: 0.2
Enter the x coordinate of the second point: -3
Enter the y coordinate of the second point: -3
Enter the x coordinate of the third point: -0.3333333333333333333
Enter the y coordinate of the third point: 2.33333333333333333
Enter the x coordinate of the point you want to check: 0
Enter the y coordinate of the point you want to check: 0.5
The point ( 0.0 , 0.5 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: -3 
Enter the y coordinate of the first point: -3
Enter the x coordinate of the second point: -0.3333333333333333333
Enter the y coordinate of the second point: 2.333333333333333
Enter the x coordinate of the third point: 0.2
Enter the y coordinate of the third point: 0.2
Enter the x coordinate of the point you want to check: 0
Enter the y coordinate of the point you want to check: 0.5
The point ( 0.0 , 0.5 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: -0.33333333333333333
Enter the y coordinate of the first point: 2.33333333333333333
Enter the x coordinate of the second point: 0.2
Enter the y coordinate of the second point: 0.2
Enter the x coordinate of the third point: -3
Enter the y coordinate of the third point: -3
Enter the x coordinate of the point you want to check: 0
Enter the y coordinate of the point you want to check: 0.5
The point ( 0.0 , 0.5 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: 0
Enter the y coordinate of the first point: 0
Enter the x coordinate of the second point: 1
Enter the y coordinate of the second point: 2
Enter the x coordinate of the third point: 3.5
Enter the y coordinate of the third point: 0.75
Enter the x coordinate of the point you want to check: 1.5
Enter the y coordinate of the point you want to check: 2
The point ( 1.5 , 2.0 ) is not inside the triangle
"""
"""
Enter the x coordinate of the first point: 3.5
Enter the y coordinate of the first point: 0.75
Enter the x coordinate of the second point: 1
Enter the y coordinate of the second point: 2
Enter the x coordinate of the third point: 0
Enter the y coordinate of the third point: 0
Enter the x coordinate of the point you want to check: 1.5
Enter the y coordinate of the point you want to check: 2
The point ( 1.5 , 2.0 ) is not inside the triangle
"""
"""
Enter the x coordinate of the first point: 0.2
Enter the y coordinate of the first point: 0.2
Enter the x coordinate of the second point: -3
Enter the y coordinate of the second point: -3
Enter the x coordinate of the third point: -0.3333333333333333333333
Enter the y coordinate of the third point: 2.333333333333333333
Enter the x coordinate of the point you want to check: -1
Enter the y coordinate of the point you want to check: 1
The point ( -1.0 , 1.0 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: 0.2
Enter the y coordinate of the first point: 0.2
Enter the x coordinate of the second point: -0.33333333333333333
Enter the y coordinate of the second point: 2.333333333333333
Enter the x coordinate of the third point: -3
Enter the y coordinate of the third point: -3
Enter the x coordinate of the point you want to check: -1
Enter the y coordinate of the point you want to check: 1
The point ( -1.0 , 1.0 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: -1
Enter the y coordinate of the first point: 4
Enter the x coordinate of the second point: -1.833 
Enter the y coordinate of the second point: -0.167
Enter the x coordinate of the third point: 0.667
Enter the y coordinate of the third point: -2.667
Enter the x coordinate of the point you want to check: 0.09
Enter the y coordinate of the point you want to check: -0.32
The point ( 0.09 , -0.32 ) is not inside the triangle
"""
"""
Enter the x coordinate of the first point: -1.833
Enter the y coordinate of the first point: -0.167
Enter the x coordinate of the second point: -1
Enter the y coordinate of the second point: 4
Enter the x coordinate of the third point: 0.667
Enter the y coordinate of the third point: -2.667
Enter the x coordinate of the point you want to check: 0.09
Enter the y coordinate of the point you want to check: -0.32
The point ( 0.09 , -0.32 ) is not inside the triangle
"""
"""
Enter the x coordinate of the first point: -1.833
Enter the y coordinate of the first point: -0.167
Enter the x coordinate of the second point: -1
Enter the y coordinate of the second point: 4
Enter the x coordinate of the third point: 0.667
Enter the y coordinate of the third point: -2.667
Enter the x coordinate of the point you want to check: -0.8
Enter the y coordinate of the point you want to check: 1
The point ( -0.8 , 1.0 ) is inside the triangle
"""
"""
Enter the x coordinate of the first point: -1
Enter the y coordinate of the first point: 4
Enter the x coordinate of the second point: -1.833
Enter the y coordinate of the second point: -0.167
Enter the x coordinate of the third point: 0.667
Enter the y coordinate of the third point: -2.667
Enter the x coordinate of the point you want to check: -0.8
Enter the y coordinate of the point you want to check: 1
The point ( -0.8 , 1.0 ) is inside the triangle
"""