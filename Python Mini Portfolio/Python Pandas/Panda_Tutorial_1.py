import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Using the data[] to get the Different Row(Horizontal) of the Data:
# Getting the Data for the grey_squirrel:
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
# Using the len function:
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrel_count)
# Using the len function:
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrel_count)
# Using the len function:
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)


# Print all the Data
# print(gray_squirrel)
# Print only the First Few Data:
# print(gray_squirrel.head)
# Print the count of the Data:
# print(gray_squirrel_count)

# This is the Dictionary:
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

# Converting the Data in the Dictionary into the DataFrame:
df = pandas.DataFrame(data_dict)
# Converting the Data to_csv format:
df.to_csv("squirrel_count.csv")


