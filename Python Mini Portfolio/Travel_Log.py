travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ['Paris', 'Lille', 'Dijon']
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttberg"]
    }
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    print(new_country)
    # Using the append method to add it to the List
    travel_log.append(new_country)
    print(travel_log)


add_new_country("Russia", 2, ["Moscow", "San Peterberg"])
print(travel_log)
