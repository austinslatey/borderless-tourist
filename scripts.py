destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt",
]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Tests function above by passing string as parameter
# print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = []
# append empty lists to attractions for each destination 
for destination in destinations:
    attractions.append([])

print(attractions)

# Add attractions to empty list
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destinations = attractions[destination_index].append(attraction)
        return attractions_for_destinations
    except SyntaxError:
        return SyntaxError

# Call function and then print updated list
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)