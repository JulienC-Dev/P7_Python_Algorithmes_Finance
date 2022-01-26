import csv
from itertools import accumulate
import operator

with open("Actions.csv", newline="")as csvfile:
    csvActions = csv.reader(csvfile, delimiter=',', quotechar='|')
    actions = []
    next(csvActions)
    listActions = [[str(i[0]), int(i[1]), float(i[2]), int(i[1]) * float(i[2])] for i in csvActions]
    # listportefeuille = []

    def calcul(listActions):
        for x in range(len(listActions)-1, -1, -1):
            listeAc = listActions[:x+1]
            maxPortefeuille = 500
            i = len(listeAc)
            countValeurs = 0
            portefeuille = []

            while maxPortefeuille > 0 and i > 0:
                lAction = listeAc[i-1][1]
                countValeurs += 1
                if lAction > maxPortefeuille:
                    i -= 1
                else:
                    i -= 1
                    maxPortefeuille -= lAction
                    portefeuille.append(listeAc[i])
                    if maxPortefeuille == 0:
                        valuePortofolio = list(accumulate([y[1] for y in portefeuille], operator.__add__))
                        rentabilite = list(accumulate([y[3] for y in portefeuille], operator.__add__))
                        return print("Meilleur Portefeuille :", countValeurs," - Montant",
                               valuePortofolio[-1], "euros - rentabilité", rentabilite[-1], "Nom des Actions:",
                               " ".join([x[0] for x in portefeuille]))


            # listportefeuille.append([[x[0] for x in portefeuille], valuePortofolio[-1], rentabilite[-1]])

    calcul(listActions)
    # for i in listportefeuille:
    #     print(len(i), i)

