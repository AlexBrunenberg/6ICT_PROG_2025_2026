# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for fruit, aantal in fruitmand.items():
    extra = int(input(f"Hoeveel {fruit} bijkopen (huidig aantal is {aantal}): "))
    fruitmand[fruit] += extra
for fruit, aantal in fruitmand.items():
    print(f" - {aantal} {fruit}")