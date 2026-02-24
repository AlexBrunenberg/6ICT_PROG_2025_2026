# Gebruik onderstaande gemengde structuur om de opdracht op te lossen.
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'}
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}

for index in range(len(inception_film['cast'])):
    print(f"{inception_film['cast'][index]['acteur']} speelt {inception_film['cast'][index]['rol']}")