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

# empty attraction list test
print(attractions)

# Add attractions to empty list
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destinations = attractions[destination_index].append(attraction)
        return attractions_for_destinations
    except SyntaxError:
        return

# Call function with destination and attraction parameters THEN print the updated list
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)



# Interest finder
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]

    attractions_with_interest = []

    for attraction in attractions_in_city:
      possible_attraction = attraction
      attraction_tags = attraction[1]

      for interest in interests:
        if interest in attraction_tags:
          attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

# saoPaulo_history = find_attractions("São Paulo, Brazil", ["historical site"])
# print(saoPaulo_history)

def get_attractions_for_travelers(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hello " + traveler[0] + ", we think you'll enjoy these places near " + traveler_destination + ": " 
    # For each element in traveler_attractions add concatenation
    # If last attraction in list add a "."
    for i in range(len(traveler_attractions)):
      # if last element
      if traveler_attractions[-1] == traveler_attractions[i]:
        interests_string += traveler_attractions[i]
      else:
        interests_string += "the " + traveler_attractions[i] + ", "
    return interests_string       

smills_france = get_attractions_for_travelers(['Dereck Smill', 'Paris, France', ["art", 'museum']])
print(smills_france)