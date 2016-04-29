#! /usr/bin/python

import random




questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

drink = ["slutty", "Flaming", "Adios", "Incredible", "Snake"]
name = ["redhead", "Dr.Pepper", "MotherTrucker", "Hulk", "Bite"]




# Create funciton
def find_preferences():
    # Create blank dictionalry
    preferences = {}
    # Loop through dictionary
    for type, question in questions.items():
        # print each item in the dictionary
        print(question)
        # Take yes or no answer
        preferences[type] = input().lower() in ["y", "yes"]
        print("")
    return preferences

# User selected values
def make_drink(preferences):
    # Create empty list
    drink = []
    # Loop through ingredients dictionary
    for ingredient_type, liked in preferences.items():
        if not liked:
            continue
# Append random ingredient to new list
        drink.append(random.choice(ingredients[ingredient_type]))
    return drink


# ask user if they want another drink
    


drinkname = (random.choice(drink) + "" + random.choice(name))


# Call main function
def main():
    preferences = find_preferences()
    drink = make_drink(preferences)
    print("One drink coming up.")
    print ("I call it a " + drinkname)
    print("It's full of good stuff.  The recipe is:")
    for ingredient in drink:
        print("A {}".format(ingredient))

    print ("would you like another?")


if __name__ == "__main__":
    main()
