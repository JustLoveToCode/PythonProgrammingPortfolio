order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["starter"][1])
print(order["starter"][2])
print(order["main"][1][0])
print(order["main"][1][1])
print(order["dessert"][1])
print(order["dessert"][2])