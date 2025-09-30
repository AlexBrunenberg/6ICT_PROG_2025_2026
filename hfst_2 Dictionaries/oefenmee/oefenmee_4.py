# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# #niveau 1
# gezocht_fruit = input("Welk soor fruit zoek je: ")
# print(f"Aantal {gezocht_fruit} in mand: {fruitmand[gezocht_fruit]}")
#niveau 2
gezocht_fruit = input("Welk soor fruit zoek je: ")
if gezocht_fruit in fruitmand:
    print(f"Aantal {gezocht_fruit} in mand: {fruitmand[gezocht_fruit]}")
else:
    print(f"Kon {gezocht_fruit} niet vinden in de fruitmand.")