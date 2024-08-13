# A2.6 Sums of Cubes
# REDACTED(I <3 not doxxing myself)
# Find all the perfect cubes equal to or below an integer that are a sum of 3 perfect cubes

# Infinite loop
while True:
    # If an error occurs while converting to int, the program will not crash
    try:
        # Get the maximum number that all cubes must be at or below
        maxNumber = int(input("Please enter an integer:"))
    # If converting the user's input to an integer fails
    except:
        # Print that the input is not an integer
        print("This is not an integer.")
    # If converting the user's input to an integer is successful
    else:
        # Exit the infinite loop and move to the main function of the program
        break

# Create a new list to store the perfect cubes up to the number that the user chose
perfCubes = []
totalsolutions = 0
# Create a counter variable and initialize it to 1
i = 1
# Infinite loop
while True:
    # Find the next cube by multiplying the counter by itself 3 times
    nextCube = i*i*i
    # If the next cube is more than the maximum number,
    if nextCube > maxNumber:
        # Stop adding cubes and exit the infinite loop
        break
    # If the next cube is less than or equal to the maximum number, add it to the list of perfect cubes
    perfCubes.append(nextCube)
    # Increment the counter variable by 1
    i = i + 1
# For every perfect cube up to the number that the user chose
for a in range(0,len(perfCubes)):
    # Set the current cube root by finding the position in the array(the real root is this number + 1)
    currentCubeRoot = perfCubes.index(perfCubes[a])

    # The goal of this section is to try all possible combinations of cubes that could be added to equal the possible cubelet we are checking
    # This loop will iterate over all the possible options for the 1st cube
    for b in range(0,currentCubeRoot - 2):
        # This loop will iterate over all the possible options for the 2nd cube for each 1st cube
        for c in range(b+1,currentCubeRoot - 1):
            # This loop will iterate over all the possible options for the 3rd cube for each 2nd cube
            for d in range(c+1, currentCubeRoot):
                # If the 3 perfect cubes added are equal to the cube we are checking,
                if perfCubes[b] + perfCubes[c] + perfCubes[d] == perfCubes[a]:
                    # The current cube is a cubelet
                    # Initialize the sorted cube roots
                    perfCubeRootSorted1 = 0
                    perfCubeRootSorted2 = 0
                    perfCubeRootSorted3 = 0
                    # If b is the largest cube root,
                    if b >= c and b >= d:
                        # Set the 3rd cube root to b
                        perfCubeRootSorted3 = b
                    # If c is the largest cube root,
                    elif c >= b and c >= d:
                        # Set the 3rd cube root to c
                        perfCubeRootSorted3 = c
                    # If d is the largest cube root,
                    else:
                        # Set the 3rd cube root to d
                        perfCubeRootSorted3 = d
                    # If b is the smallest cube root,
                    if b <= c and b <= d:
                        # Set the 1st cube root to b
                        perfCubeRootSorted1 = b
                    # If c is the smallest cube root,
                    elif c <= b and c <= d:
                        # Set the 1st cube root to c
                        perfCubeRootSorted1 = c
                    # If d is the smallest cube root,
                    else:
                        # Set the 1st cube root to d
                        perfCubeRootSorted1 = d
                    # If b and c were previously used
                    if perfCubeRootSorted1 == b and perfCubeRootSorted3 == c:
                        # Set the middle cube root to d
                        perfCubeRootSorted2 = d
                    # If c and b were previously used
                    elif perfCubeRootSorted1 == c and perfCubeRootSorted3 == b:
                        # Set the middle cube root to d
                        perfCubeRootSorted2 = d
                    # If c and d were previously used
                    elif perfCubeRootSorted1 == c and perfCubeRootSorted3 == d:
                        # Set the middle cube root to b
                        perfCubeRootSorted2 = b
                    # If d and c were previously used
                    elif perfCubeRootSorted1 == d and perfCubeRootSorted3 == c:
                        # Set the middle cube root to b
                        perfCubeRootSorted2 = b
                    # If a and d were previously used or d and a were previously used
                    else:
                        # Set the middle cube root to c
                        perfCubeRootSorted2 = c
                    # Print the root of the cubelet by using its position in the array + 1 and print the cubelet itself
                    # Print the roots of the smaller cubes by using their position in the array + 1
                    print(currentCubeRoot + 1, perfCubes[a], perfCubeRootSorted1 + 1, perfCubeRootSorted2 + 1, perfCubeRootSorted3 + 1, sep = ",")
                    totalsolutions = totalsolutions + 1

print(totalsolutions)
# Test cases
"""
Please enter an integer: 216
6,216,3,4,5
"""
"""
Please enter an integer: 5000
6,216,3,4,5
9,729,1,6,8
12,1728,6,8,10
"""
"""
Please enter an integer: abc
This is not an integer.
Please enter an integer: !398423
This is not an integer.
Please enter an integer: 216
6,216,3,4,5
"""
"""
Please enter an integer: 1
"""
"""
Please enter an integer: -6000000
"""
"""
Please enter an integer: 0
"""
"""
Please enter an integer: 6000000
6,216,3,4,5
9,729,1,6,8
12,1728,6,8,10
18,5832,2,12,16
18,5832,9,12,15
19,6859,3,10,18
20,8000,7,14,17
24,13824,12,16,20
25,15625,4,17,22
27,19683,3,18,24
28,21952,18,19,21
29,24389,11,15,27
30,27000,15,20,25
36,46656,4,24,32
36,46656,18,24,30
38,54872,6,20,36
40,64000,14,28,34
41,68921,2,17,40
41,68921,6,32,33
42,74088,21,28,35
44,85184,16,23,41
45,91125,5,30,40
46,97336,3,36,37
46,97336,27,30,37
48,110592,24,32,40
50,125000,8,34,44
53,148877,29,34,44
54,157464,6,36,48
54,157464,12,19,53
54,157464,27,36,45
56,175616,36,38,42
57,185193,9,30,54
58,195112,15,42,49
58,195112,22,30,54
60,216000,21,42,51
60,216000,30,40,50
63,250047,7,42,56
66,287496,33,44,55
67,300763,22,51,54
69,328509,36,38,61
70,343000,7,54,57
71,357911,14,23,70
72,373248,8,48,64
72,373248,34,39,65
72,373248,36,48,60
75,421875,12,51,66
75,421875,38,43,66
76,438976,12,40,72
76,438976,31,33,72
78,474552,39,52,65
80,512000,28,56,68
81,531441,9,54,72
81,531441,25,48,74
82,551368,4,34,80
82,551368,12,64,66
82,551368,19,60,69
84,592704,28,53,75
84,592704,42,56,70
84,592704,54,57,63
85,614125,50,61,64
87,658503,20,54,79
87,658503,26,55,78
87,658503,33,45,81
87,658503,38,48,79
88,681472,21,43,84
88,681472,25,31,86
88,681472,32,46,82
89,704969,17,40,86
90,729000,10,60,80
90,729000,25,38,87
90,729000,45,60,75
90,729000,58,59,69
92,778688,6,72,74
92,778688,54,60,74
93,804357,32,54,85
95,857375,15,50,90
96,884736,19,53,90
96,884736,48,64,80
97,912673,45,69,79
99,970299,11,66,88
100,1000000,16,68,88
100,1000000,35,70,85
102,1061208,51,68,85
103,1092727,12,31,102
105,1157625,33,70,92
106,1191016,58,68,88
108,1259712,12,72,96
108,1259712,13,51,104
108,1259712,15,82,89
108,1259712,24,38,106
108,1259712,54,72,90
110,1331000,29,75,96
111,1367631,16,47,108
112,1404928,72,76,84
113,1442897,50,74,97
114,1481544,18,60,108
114,1481544,57,76,95
115,1520875,3,34,114
116,1560896,23,86,97
116,1560896,30,84,98
116,1560896,44,60,108
117,1601613,13,78,104
120,1728000,9,55,116
120,1728000,42,84,102
120,1728000,60,80,100
121,1771561,49,84,102
122,1815848,19,92,101
123,1860867,6,51,120
123,1860867,18,96,99
123,1860867,44,51,118
125,1953125,20,85,110
126,2000376,14,84,112
126,2000376,23,94,105
126,2000376,63,84,105
127,2048383,13,65,121
129,2146689,38,57,124
132,2299968,5,76,123
132,2299968,48,69,123
132,2299968,66,88,110
133,2352637,21,70,126
134,2406104,44,102,108
134,2406104,86,95,97
135,2460375,15,90,120
137,2571353,44,73,128
138,2628072,9,108,111
138,2628072,69,92,115
138,2628072,72,76,122
138,2628072,81,90,111
139,2685619,94,96,99
140,2744000,14,108,114
140,2744000,49,98,119
140,2744000,90,95,105
141,2803221,72,85,122
142,2863288,28,46,140
142,2863288,31,64,137
144,2985984,1,71,138
144,2985984,16,96,128
144,2985984,68,78,130
144,2985984,72,96,120
145,3048625,12,81,136
145,3048625,55,75,135
147,3176523,22,75,140
150,3375000,24,102,132
150,3375000,71,73,138
150,3375000,75,100,125
150,3375000,76,86,132
151,3442951,46,47,148
152,3511808,24,80,144
152,3511808,62,66,144
153,3581577,17,102,136
156,3796416,65,87,142
156,3796416,78,104,130
159,4019679,3,121,131
159,4019679,87,102,132
160,4096000,56,112,136
160,4096000,69,123,124
162,4251528,18,108,144
162,4251528,36,57,159
162,4251528,50,96,148
162,4251528,59,93,148
162,4251528,81,108,135
164,4410944,8,68,160
164,4410944,24,128,132
164,4410944,38,120,138
164,4410944,69,99,146
167,4657463,12,86,159
168,4741632,56,106,150
168,4741632,84,112,140
168,4741632,108,114,126
170,4913000,96,107,141
170,4913000,100,122,128
171,5000211,19,114,152
171,5000211,27,90,162
171,5000211,54,80,163
171,5000211,107,108,136
172,5088448,1,135,138
174,5268024,40,108,158
174,5268024,45,126,147
174,5268024,47,97,162
174,5268024,52,110,156
174,5268024,66,90,162
174,5268024,76,96,158
174,5268024,87,116,145
175,5359375,28,119,154
176,5451776,25,92,167
176,5451776,42,86,168
176,5451776,50,62,172
176,5451776,64,92,164
177,5545233,48,137,142
178,5639752,34,80,172
178,5639752,48,133,147
179,5735339,17,57,177
180,5832000,20,120,160
180,5832000,50,76,174
180,5832000,63,126,153
180,5832000,90,120,150
180,5832000,116,118,138
181,5929741,108,109,150
"""