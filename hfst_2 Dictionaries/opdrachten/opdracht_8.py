# Los de problemen uit de opdracht op met behulp van onderstaande code.

# Niveau 1
dict_1={1: 10, 2: 20}
dict_2={3: 30, 4: 40}
dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dictionary = {}
for sleutel, waarde in dict_1.items():
    dictionary[sleutel] = waarde
for sleutel, waarde in dict_2.items():
    dictionary[sleutel] = waarde
for sleutel, waarde in dict_3.items():
    dictionary[sleutel] = waarde

print(dictionary)


# Niveau 2
dict = {'a': 'Red', 'b': 'Green', 'c': None, 'd' : None, 'e': 'Blue', 'f': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}

lijstNone = []

for sleutel, waarde in dict.items():
    if waarde == None:
        lijstNone.append(sleutel)

for index in range(len(lijstNone)):
    dict.pop(lijstNone[index])
print(dict)

# Niveau 3
dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "g": 60} 
te_verwijderen = ["d", "g", "b"]
# Resultaat: {'a': 10, 'c': 30, 'e': 50}

for index in range(len(te_verwijderen)):
    dict.pop(te_verwijderen[index])
print(dict)

# Niveau 4
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})

dict = {}

for sleutel, waarde in dict_1.items():
    if sleutel in dict_2:
        dict[sleutel] = waarde + dict_2[sleutel]
    else:
        dict[sleutel] = waarde
for sleutel, waarde in dict_2.items():
    if sleutel not in dict:
        dict[sleutel] = waarde
print(dict)