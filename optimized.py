import csv
from itertools import accumulate
import operator
from operator import itemgetter

def getData(file):
    with open(file, newline="")as csvfile:
        csvActions = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvActions)
        listActions = [[str(i[0]), int(i[1]), float(i[2]), int(i[1]) * float(i[2])] for i in csvActions]
        return listActions


def calcul(listActions):
    listeportefeuille = []
    for x in range(0, len(listActions)):
        listeAc = listActions[x:]
        maxPortefeuille = 500

        portefeuille = []
        i = 0

        while maxPortefeuille > 0 and len(listeAc) > i:
            lAction = listeAc[i][1]

            if lAction > maxPortefeuille:
                i += 1
            else:
                maxPortefeuille -= lAction
                portefeuille.append(listeAc[i])
                i += 1

        valuePortofolio = list(accumulate([y[1] for y in portefeuille], operator.__add__))
        rentabilite = list(accumulate([y[3] for y in portefeuille], operator.__add__))
        listeportefeuille.append([[x[0] for x in portefeuille], valuePortofolio[-1], rentabilite[-1]])
    MeilleurPortefeuille = sorted(listeportefeuille, key=lambda montant: [montant[1] for x in listeportefeuille],
                                  reverse=True)
    print(MeilleurPortefeuille[0])


if __name__ == "__main__":
    FileActions = "Actions.csv"
    calcul(getData(FileActions))
