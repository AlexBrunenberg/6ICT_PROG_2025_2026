# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingrediënt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}

# # niveau 1
# print("Recept voor worst met wortelen en erwten.")
# for sleutel,waarde in recept.items():
#     print(f"- {sleutel}: {waarde} gr.")

# niveau 2

aantal_pers = (int(input("Voor hoeveel mensen kook je: ")))/4
print("Recept voor worst met wortelen en erwten.")
for sleutel,waarde in recept.items():
    print(f"- {sleutel}: {int(waarde * aantal_pers)} gr.")