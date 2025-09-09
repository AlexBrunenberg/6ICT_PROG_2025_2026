def seconden_in_leven(leeftijd, sekse):
    """ return de seconden die een persoon nog leeft
            Tip! een jaar is gemiddeld 365.25 dagen 
                 gebruik ook de formule uit oefening 7

        Maak hiervoor gebruik van:
            - de huidige leeftijd van de persoon.
            - De sekse van de persoon.
    
        Een man wordt gemiddeld 80 jaar,
        een vrouw wordt gemiddeld 84 jaar.
    """
    if sekse == "man":
        print(80-leeftijd)
        return int((80-leeftijd)*365.25*24*60*60)
    elif sekse == "vrouw":
        print(84-leeftijd)
        return int((84-leeftijd)*365.25*24*60*60)


print( seconden_in_leven(0, "vrouw")  ) # 2650838400
print( seconden_in_leven(74, "man")   ) # 189345600
print( seconden_in_leven(56, "vrouw") ) # 883612800
