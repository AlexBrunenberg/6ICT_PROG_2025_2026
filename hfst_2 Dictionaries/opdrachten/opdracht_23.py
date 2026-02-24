namen = ['jan','piet','joris','korneel', 'toon', 'riemke', 'jo', 'alysa', 'emanuel', 'dorian', 'els']


def filter_namen(namen: list):
    klinkers = "aeiou"
    teller = 0
    gefilterdeNamen = []
    for index, naam in enumerate(namen):
        if 2 < len(naam) < 7:
            if "s" not in naam:
                for index, letter in enumerate(naam):
                    if letter in klinkers:
                        teller += 1
                print(teller)
                if teller >= 2:
                    gefilterdeNamen.append(naam) 
                    teller = 0
        else:
            pass
    return(gefilterdeNamen)

print(filter_namen(namen))