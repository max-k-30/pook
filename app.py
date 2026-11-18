import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
pokedox = open('./moves.json', encoding='utf8')
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
dati = json.load(pokedox)
# print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

# pokemen_types = {
#     "type": set()
# }


z = {'english', 'french', 'japanese', 'chinese'}
x = input("Which language do you perfer? ")
while x.lower() not in z:
    print("That's not a valid language ")
    x = input("Which language do you perfer? ")
for pokemon in data:
    print(pokemon['name'][x.lower()])



def type_search():
    finished = False
    while finished == False:
        y = input("Which pokemon type do you wish to search for? ")
        for pokemon in data:
            if y.capitalize() in pokemon['type']:
                print (pokemon["name"][x.lower()])
                finished = True
        if finished == False:
            print("That's not a type")
type_search()

def name_search():
    finished = False
    while finished == False:
        a = input('Which pokemon would you like to search? ')
        for pokemon in data:
            name = pokemon['name'][x.lower()]
            if a.lower() in name.lower():
                print(pokemon['name'][x.lower()])
                finished = True
        if finished == False:
            print("No results were found!")
name_search()

def potential_moves():
    finished1 = False
    finished2 = False
    while finished == False:
        type1 = input("Input the first type of your pokemon: ")
        type2 = input("Input the second type of your pokemon to see their available moves. If your pokemon does not have a second type, input first type: ")
        for i in range(len(dati)):
            if type1.capitalize() in dati[i]['type']:
                print(dati[i]['ename'])
                finished1 = True
            if type2.capitalize() in dati[i]['type']:
                print(dati[i]['ename'])
                finished2 = True
    if finished1 == False:
            print('No results found for ' type! ')
            

                

potential_moves()