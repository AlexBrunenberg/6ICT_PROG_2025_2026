sport_uitslagen = {
    "Emma" : [2,3,1,4,2],
    "Liam" : [1,2,1,3,0],
    "Noah" : [0,1,2,1,3],
    "Sarah" : [3,3,4,2,1],
    "Kiana" : [1,0,2,1,2],
    "Lucas" : [ 2,1,3,1,0]
}

gemiddelde_scores = {}
totale_uitslagen = {}

for naam, scores in sport_uitslagen.items():
    totale_uitslag = 0
    for score in scores:
        totale_uitslag = totale_uitslag + score
    gemiddelde_score = totale_uitslag / 5
    gemiddelde_scores[naam] = gemiddelde_score
    totale_uitslagen[naam] = totale_uitslag
score_hoogste = 0
score_laagste = 100
for namen, scores in gemiddelde_scores.items():
    if score_hoogste < gemiddelde_scores[namen]:
        naam_hoogste = namen
        score_hoogste = gemiddelde_scores[namen]
    if score_laagste > gemiddelde_scores[namen]:
        naam_laagste = namen
        score_laagste = gemiddelde_scores[namen]
print(gemiddelde_scores)
print(naam_hoogste, totale_uitslagen[naam_hoogste])
print(naam_laagste, totale_uitslagen[naam_laagste])