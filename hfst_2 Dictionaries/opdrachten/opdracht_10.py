# Maak gebruik van onderstaande dictionary.
flashkaarten = {
    "hond": "dog",
    "kat": "cat",
    "huis": "house",
    "auto": "car",
}

fouten = []

for sleutel,waarde in flashkaarten.items():
    vertaling = input(f"Wat is de vertaling van {sleutel}: ")
    if vertaling == waarde:
        print("Dit klopt!")
    else:
        print("Dit klopt niet!")
        fouten.append(waarde)
if fouten != "":
    print(f"Oefen meer op deze woorden")