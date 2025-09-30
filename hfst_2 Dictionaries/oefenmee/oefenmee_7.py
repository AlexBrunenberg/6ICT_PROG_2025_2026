# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}

while True:
    naam = input("Wat is je naam: ")
    if naam == "STOP":
        break
    elif 0 == gasten.get(naam, 0):
        print(f"De naam {naam} staat niet op de lijst.")
    else:
        print(f"Welkom {gasten[naam]} {naam}. Kom binnen.")
        gasten.pop(naam)