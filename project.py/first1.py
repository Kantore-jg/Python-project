capitals={
    "france":{"cities_visited" :["paris","Lille","dijon"],
     "total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],
     "total_visits":5},
    }
travel_log=[
    {"country":"france",
     "cities" :["paris","Lille","dijon"],
     "total_visits":12},
    {"country":"Germany",
     "cities":["Berlin","Hamburg","Stuttgart"],
     "total_visits":5},
    ]


def add(country_visited, time_visited, cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["total_visits"]=time_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)
    
add("Russia", 2,["Moscow","saint petersburg"])
print(travel_log)