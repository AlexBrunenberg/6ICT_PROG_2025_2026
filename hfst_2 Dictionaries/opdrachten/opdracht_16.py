# Print de lengte van de acteurs in onderstaande lijst van dictionaries.
info_acteurs = [
    {"name": "Q. Tarentino", "leeftijd": 59, "lengte": 170},
    {"name": "J. Travolta", "leeftijd": 68, "lengte": 178},
    {"name": "S.L. Jackson", "leeftijd": 73},
    {"name": "U. Thurman", "leeftijd": 53, "lengte": 158}
]
print(info_acteurs[0]["name"])

for dictionary in (info_acteurs):
    if "lengte" in dictionary:
        print(f"De lengte van {dictionary["name"]} is {dictionary["lengte"]}.")
    else:
        print(f"De lengte van {dictionary["name"]} is niet gegeven.")