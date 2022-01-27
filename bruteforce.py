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
    for i in range(1, len(listActions)+1):
        listcombination = list(combinations(listActions, i))
        for x in listcombination:
            valuePortofolio = sum([y[1] for y in x])
            if (valuePortofolio <= 500):
                countPortefeuille += 1
                nomsActions = [y[0] for y in x]
                rentabilite = sum([y[3] for y in x])
                portefeuille.append([valuePortofolio, rentabilite, nomsActions])
            else:
                continue

    MeilleurPortefeuille = max(portefeuille, key=itemgetter(1))
    print(' '.join([str(x) for x in MeilleurPortefeuille]))

