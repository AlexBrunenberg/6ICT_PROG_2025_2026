# Maak gebruik van onderstaande dictionary.
flashkaarten = {
    "hond": "dog",
    "kat": "cat",
    "huis": "house",
    "auto": "car",
}

import random

fouten = []
flashcards = {}

woorden = ["hond", "kat", "huis", "auto"]

for cijfer in range(4, 0, -1):
    randomCijfer = random.randint(0, (cijfer-1))
    flashcards[woorden[randomCijfer]] = flashkaarten[woorden[randomCijfer]]
    woorden.pop(randomCijfer)


for sleutel,waarde in flashcards.items():
    vertaling = input(f"Wat is de vertaling van {sleutel}: ")
    if vertaling == waarde:
        print("Dit klopt!")
    else:
        print("Dit klopt niet!")
        fouten.append(waarde)
if fouten != []:
    print(f"Oefen meer op deze woorden: {fouten}")