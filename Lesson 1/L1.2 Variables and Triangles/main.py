# L1.2 Variables and Triangles
# REDACTED(I <3 not doxxing myself)
# Take a principal amount of money and an interest rate to find how much money you will have after 1 year(using 800$ and a 7% interest rate)

# define a principal(starting) amount of money
principal = 800
# define the interest rate
rate = 0.07
# define how many years the interest is calculated for
time = 1
# calculate the amount of interest and add it to the principal to get the total amount of money
money = principal + principal * rate * time
# Print how much their principal was
print("For a principal of")

print(principal)
# Print what the interest rate was
print("and an interest rate of")

print(rate)
# Print how many years the investment was collecting interest
print("the money after", time, "year(s) has grown to")
# Print the total amount of money
print(money) # You should have 856$ for your final value
#test cases
"""
For a principal of
800
and an interest rate of
0.07
the money after 1 year(s) has grown to
856
"""