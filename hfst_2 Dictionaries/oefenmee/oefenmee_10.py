# Vul eerst aan. Daarna pas uitvoeren!
dictionary = {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}

""" Geef aan wat volgende code print"""
" Vul aan: "
print(dictionary) #{"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}

" Vul aan: "
for x in dictionary: #
    print(x)

" Vul aan: "
print( list(dictionary.keys())) # "a" "b" "c" "d" "e"

" Vul aan: "
print( dictionary.get("e", 4)) # 3

" Vul aan: "
print( list(dictionary.values())) # 0 1 1 2 3

" Vul aan: "
print( dictionary.get("q", 4)) # 4

" Vul aan: "
for x, y in dictionary.items(): # 0 "a" 1 "b" 1 "c" 2 "d" 3 "e"
    print(y, x)

" Vul aan: "
for x in dictionary.values(): # 0 1 1 2 3
    print(x)

" Vul aan: "
print( dictionary.pop("c")) #

"Vul aan: "
print( list(dictionary.items()) ) # "a" 0 "b" 1 "d" 2 "e" 3