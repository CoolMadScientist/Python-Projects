programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Test"] = "Test"

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit items in dictionary
#programming_dictionary["Bug"] = "an animal"

# Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

##################################################################

# Nesting

capitals = {
    "France": "Paris",
    "Germany":"Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Pris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nest a dictionary in a dictionary

travel_log = {
    "France": {'cities_visited': ["paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {'cities_visited': ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 0}
}

# Nesting Dictionary in a list

travel_log = [
    {
        "Country": "France", 
        'cities_visited': ["paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    
    {
        "country": "Germany", 
        'cities_visited': ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 0
    },
]