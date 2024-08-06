heroes = ["Ironman", "Thor", "Hulk", "Spiderman"]

def display_heros():
    print(f"The list of Heroes are: {heroes}")

def add_heroes():
    global heroes_add
    heroes_add = input("Your Favorite heroes: ")
    
def insert_heroes():
    heroes.append(heroes_add)
    print(f"The list of Heroes are: {heroes}")

def remove_heroes():
    heroes.remove(heroes_add)
    print(f"Heroes remove: {heroes_add} {heroes}")

def sorted_heroes():
    heroes.sort()
    print(f"Heroes after sorted: {heroes}")

display_heros()
add_heroes()
insert_heroes()
remove_heroes()
sorted_heroes()
