# Start met onderstaande dictionary.
database = { # Sleutel = naam, waarde = wachtwoord
    "Jan": "FkeHsne569*",
    "Piet": "KsnOmd727^",
    "Joris": "DneSje439&",
    "Korneel": "MdsSnz863*"
}

naam = input("Wie wilt inloggen: ")
if naam not in database:
    print(f'{naam} bestaat niet in de database.')
else:
    wachtwoord = input(f"Geef wachtwoord op van {naam}.")
    if wachtwoord == database[naam]:
        print(f'Welkom {naam}!')
    else:
        print(f"Wachtwoord incorrect")