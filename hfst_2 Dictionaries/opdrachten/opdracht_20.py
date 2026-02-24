smiley = [
    [0, 1, 0, 1, 0],
    [0, 0, 2, 0, 0],
    [3, 0, 0, 0, 3],
    [0, 3, 3, 3, 0]
]

for index in range(len(smiley)):
    lijstRij = []
    for indexRij, cijfer in enumerate(smiley[index]):
        if cijfer == 0:
            lijstRij.append(" ")
        if cijfer == 1:
            lijstRij.append("#")
        if cijfer == 2:
            lijstRij.append(".")
        if cijfer == 3:
            lijstRij.append("-")
    print(lijstRij[0],lijstRij[1],lijstRij[2],lijstRij[3],lijstRij[4])