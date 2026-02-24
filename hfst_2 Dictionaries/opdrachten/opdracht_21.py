lijst_2D = [
    [11, 12, 34, 14],
    [32, 22, 23, 24],
    [31, 32, 33, 12] 
]

def max_vinder(lijst_2D):
    max = 0
    for index in range(len(lijst_2D)):
        for indexNummer, waarde in enumerate(lijst_2D[index]):
            if waarde > max:
                max = waarde
                indexMax = index
    return(max, indexMax)

    
print(max_vinder(lijst_2D))    