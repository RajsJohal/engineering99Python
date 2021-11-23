# a function that takes in a string
#if that string exists in cocktails file
#return "Coming Right Up"
#Otherwise return "Not on the menu sorry

def cocktail_order(cocktail: str) -> str:
    with open("cocktails.txt") as file:
        cocktail_list = file.read().split("\n")
        for drinks in cocktail_list:
            if cocktail == drinks:
                return f"One {cocktail} Coming Right Up!"

        return "Not on the menu, Sorry"


print(cocktail_order("Mojito"))

# A function that takes in a string
# If it does not already exist in the menu,
# add it to the menu
# Otherwise print a warning that the cocktail is already
# on the menu (bonus: raise an error)


def add_drink_to_menu(drink: str):
    with open("cocktails.txt", "a+") as file:
        cocktail_list = file.read().split("\n")
        for drinks in cocktail_list:
            if drink == drinks:
                return f"{drink} is already on our menu"

        return f"We will add {drink} to the menu"
        file.append(f"{drink}\n")


print(add_drink_to_menu("Long Island Ice Tea"))
