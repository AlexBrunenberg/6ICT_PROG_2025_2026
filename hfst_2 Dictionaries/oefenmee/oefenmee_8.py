# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
stad = input("In welke stad bent u: ")
if 0 == steden_temp.get(stad, 0):
    print("Het is hier ??? °C")
else:
    print(f"Het is hiet {steden_temp[stad]} °C")