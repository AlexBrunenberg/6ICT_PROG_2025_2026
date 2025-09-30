# Start de opdracht met onderstaande lijst.
fruitlijst = ["appel","doerian","banaan","doerian","appel","kers",
"kers","mango","appel","appel","kers","doerian","banaan",
"appel","appel","appel","appel","banaan","appel"]

fruit_dictionary = {}

for fruit in fruitlijst:
    if fruit in fruit_dictionary:
        pass
    else:
        fruit_dictionary[fruit] = fruitlijst.count(fruit)
print(fruit_dictionary)