# Write the Program that will calculate the sum of all
# the even number from 1 to 100, including the 1 and 100

total = 0
for number in range(2, 101, 2):
    total = total + number
# You will want to include the 1 also in the calculation
# It is going to print out using print(total+1), once everything has been calculated
print(total + 1)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2 + 1)
