import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

pokemen_types = {
    "type": set()
}

z = {'english', 'french', 'japanese', 'chinese'}
x = input("Which language do you perfer? ")
if x.lower() not in z:
    print("That's not a valid language ")
    x = input("Which language do you perfer? ")
for index, item in enumerate(data):
    print(index, ":", item['name'][x.lower()])

def type_search():
    y = input("Which pokemon type do you wish to search up? ")
    if y.capitalize() not in data:
        print("That's not a type!")
    for i in range(len(data)):
        if y.capitalize() in data[i]['type']:
            print (data[i]["name"][x.lower()])
type_search()

""" for x, data in enumerate(data):
    pokemen_types["type"].update(data["type"])
print(pokemen_types["type"]) """
