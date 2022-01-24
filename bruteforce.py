import csv
from itertools import combinations, accumulate
import operator
from operator import itemgetter

with open("Actions.csv", newline="")as csvfile:
    csvActions = csv.reader(csvfile, delimiter=',', quotechar='|')
    actions = []
    next(csvActions)

    listActions = [[str(i[0]), int(i[1]), float(i[2]), int(i[1]) * float(i[2])] for i in csvActions]

    countPortefeuille = 0
    portefeuille = []
    for i in range(0, len(listActions)+1):
        listcombination = list(combinations(listActions, i))
        for x in listcombination:
            valuePortofolio = list(accumulate([y[1] for y in x], operator.__add__))
            if len(valuePortofolio) == 0:
                continue
            elif (valuePortofolio[-1] <= 500):
                countPortefeuille += 1
                nomsActions = [y[0] for y in x]
                rentabilite = list(accumulate([y[3] for y in x], operator.__add__))
                portefeuille.append(["Portfeuille", countPortefeuille, " - Montant",valuePortofolio[-1],"euros - rentabilité",
                rentabilite[-1], "euros - ", "Nom des Actions:", " ".join(nomsActions)])
            else:
                continue

    MeilleurPortefeuille = sorted(portefeuille, key=itemgetter(3, 5), reverse=False)
    print(' '.join([str(x) for x in MeilleurPortefeuille[-1]]))




