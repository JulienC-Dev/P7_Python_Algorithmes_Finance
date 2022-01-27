import csv


def getData(file):
    with open(file, newline="")as csvfile:
        csvActions = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvActions)
        listActions = [[str(i[0]), float(i[1]), float(i[2]), float(i[1]) * float(i[2])/100] for i in csvActions if float(i[1]) > 0]
        return listActions


def calcul(listActions):
    actions = sorted(listActions, key= lambda a: a[2], reverse=True)
    listeportefeuille = []
    cout = 0
    gain = 0
    for action in actions:
        if cout + action[1] <= 500:
            listeportefeuille.append(action)
            cout += action[1]
            gain += action[3]
    print(listeportefeuille, cout, gain)


if __name__ == "__main__":
    FileActions = "Data1sienna.csv"
    calcul(getData(FileActions))
