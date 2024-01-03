with open("weather_data.csv") as data_file:
    data = data_file.readlines()

import csv

temperature = []
with open("weather_data.csv") as data_file:
    # Using the csv.reader
    data = csv.reader(data_file)
    for row in data:
        if row[1] != 'temp':
            temperature.append(row[1])

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data['temp'].to_list()


# Create dataframe from scratch:
data_dict = {
    "students": ["Amy", "John", "Angela"],
    "scores": [76, 50, 45]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



