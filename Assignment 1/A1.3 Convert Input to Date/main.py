# A1.3 Convert Input to Date
# REDACTED(I <3 not doxxing myself)
# Gather input from a user to check if a date is valid and print whether it is a valid date or not

# If any part of the following 4 lines of code fails, then the input is not a valid date
try:
    # Gather the day, month, and year of the date from the user
    day = input("Please enter the current day:")
    month = input("Please enter the current month:")
    year = input("Please enter the current year:")
    # Convert the user's inputs into integers, while keeping the raw string inputs in case this fails to print to console
    dayInt = int(day)
    monthInt = int(month)
    yearInt = int(year)
    # If any of the integers are less than 0, the input is not a valid date and throw an error
    if dayInt < 0 or monthInt < 0 or yearInt < 0:
        raise ValueError
    # If the month is more than 12, it is not a valid date and throw an error
    if monthInt > 12:
        raise ValueError
    # For january, march, may, july, august, october or december, if there is more than 31 days, throw an error
    if monthInt == 1 or monthInt == 3 or monthInt == 5 or monthInt == 7 or monthInt == 8 or monthInt == 10 or monthInt == 12:
        if dayInt > 31:
            raise ValueError
    # For april, june, september or november, if there is more than 30 days, throw an error
    if monthInt == 4 or monthInt == 6 or monthInt == 9 or monthInt == 11:
         if dayInt > 30:
            raise ValueError
    # For febuary(the only month left), if there is more than 28 days, throw an error
    if monthInt == 2:
        if dayInt > 28:
            raise ValueError
# If any part of the code fails or one of the conditions that makes the date invalid is triggered,
except:
    # print that the input is not a valid date
    print("Day", day, "month", month, "year", year, "is not a valid date.")
# If all the code runs successfully and none of the conditions that makes the date invalid are triggered, 
else:
    # print that the input is a valid date
    print("Day", day, "month", month, "year", year, "is a valid date.")
# Test cases
"""
Please enter the current day: -1
Please enter the current month: 2
Please enter the current year: 3
Day -1 month 2 year 3 is not a valid date.
"""
"""
Please enter the current day: 0.5
Please enter the current month: 0.2
Please enter the current year: 0.2
Day 0.5 month 0.2 year 0.2 is not a valid date.
"""
"""
Please enter the current day: 32
Please enter the current month: 1
Please enter the current year: 2008
Day 32 month 1 year 2008 is not a valid date.
"""
"""
Please enter the current day: 31
Please enter the current month: 4
Please enter the current year: 3
Day 31 month 4 year 3 is not a valid date.
"""
"""
Please enter the current day: 29
Please enter the current month: 2
Please enter the current year: 1
Day 29 month 2 year 1 is not a valid date.
"""
"""
Please enter the current day: 26
Please enter the current month: 12
Please enter the current year: 2008
Day 26 month 12 year 2008 is a valid date.
"""