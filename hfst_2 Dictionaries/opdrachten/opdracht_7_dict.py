artikelen = { 
    "appels": 1.50,
    "nananen": 0.75,
    "brood": 2.30,
    "melk": 1.20,
    "eieren": 2.00,
    "kaas": 3.50,
    "kip": 5.75,
    "tomaten": 1.00,
    "aardappelen": 0.80,
    "ontbijtgranen": 3.25
}

artikel = ""
prijs = 0
aantal = 0
while artikel != "STOP":
    artikel = input("Welk artikel wilt u kopen: ")
    if artikel in artikelen:
        aantal += 1
        prijs += artikelen[artikel]
        print(f"{artikel} toegevoegd")
    else:
        print(f"{artikel} bestaat niet.")
print(f"U heeft {aantal} artikelen gekocht. Deze kosten samen {prijs} euro")