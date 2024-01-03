import random

all_the_names = input("Give Me Everybody Names, separated by comma\n").strip()
print(all_the_names)

# Using the split keyword to split based on the ",":
names = all_the_names.split(",")
print(names)

# Using the len to get the length of the array:
length_of_names = len(names)
print(length_of_names)

# Give you the random value from 0 to length_of_names-1 here:
random_index = random.randint(0, length_of_names-1)
print(random_index)

print(f"{names[random_index]} is going to pay for the bill today")






