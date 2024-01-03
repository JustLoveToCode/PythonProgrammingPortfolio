# To check whether the year is a Leap Year
# First Condition: We need to check if the year is evenly divisible by 4:
# If it divisible by 4, it is a Leap Year

# Second Condition: We also need to check if it is evenly divisible by 100:
# If it is not evenly divisible by 100, it is a Leap Year

# Third Condition: We also need to check if it is evenly divisible by 400:
# If it is evenly divisible by 400, it is a Leap Year.

leap_year = int(input('Please input the Year'))

if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print(f"this {leap_year} is a leap year")
        else:
            print(f"this {leap_year} is not a leap year")
    else:
        print(f"This {leap_year} is  a leap year")
else:
    print(f"This {leap_year} is not the Leap Year")
