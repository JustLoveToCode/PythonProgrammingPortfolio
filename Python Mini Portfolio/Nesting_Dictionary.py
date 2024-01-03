# Nesting Dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in the Dictionary:

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting the Dictionary Inside the List:
travel_log_1 = [
    {"Country": 'France',
     "Cities_Visited": ["Paris", "Lille", "Dijon"],
     "Total_Visited": "12"},

    {"Country": "Germany",
     "Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"],
     "Total_Visited": "5"},
]

print(travel_log_1[0])
print(travel_log_1[0]["Country"])
print(travel_log_1[0]["Cities_Visited"])
print(travel_log_1[0]["Cities_Visited"][0])
print(travel_log_1[0]["Cities_Visited"][1])
print(travel_log_1[0]["Cities_Visited"][2])
print(travel_log_1[0]["Total_Visited"])
print(travel_log_1[1])
print(travel_log_1[1]["Cities_Visited"])
print(travel_log_1[1]["Cities_Visited"][0])
print(travel_log_1[1]["Cities_Visited"][1])
print(travel_log_1[1]["Cities_Visited"][2])
print(travel_log_1[1]["Total_Visited"])

