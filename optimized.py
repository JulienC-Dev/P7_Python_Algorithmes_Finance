import csv
from itertools import combinations, accumulate
import operator
from operator import itemgetter

with open("Actions.csv", newline="")as csvfile:
    csvActions = csv.reader(csvfile, delimiter=',', quotechar='|')
    actions = []
    next(csvActions)
    listActions = [[str(i[0]), int(i[1]), float(i[2]), int(i[1])] for i in csvActions]

    maxPortefeuille = 500
    portefeuille = []
    i = len(listActions)-1

    while maxPortefeuille > 0 and len(portefeuille) < 20:
        lAction = listActions[i]

        if lAction[1] > maxPortefeuille:
            i -= 1
        else:
            i -= 1
            maxPortefeuille -= lAction[1]
            portefeuille.append(lAction)
            print(lAction, maxPortefeuille)


