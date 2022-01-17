import csv
# from itertools import combinations
import copy

with open("Action.csv", newline="")as csvfile:
    csvActions = csv.reader(csvfile, delimiter=',', quotechar='|')
    actions = []
    next(csvActions)
    listActions = [[str(i[0]), int(i[1]), float(i[2]), int(i[1]) * float(i[2])] for i in csvActions]
    Portefeuille = "portefeuille"
    # p = [[print(portefeuille, (x[0], y[1]))] for x in listActions for y in listActions]
    nbAction = len(listActions)
    countPortefeuille = 0

    # def combinations(iterable, r):
    #         pool = tuple(iterable)
    #         n = len(pool)
    #         if r > n:
    #             return
    #         indices = list(range(r))
    #         yield tuple(pool[i] for i in indices)
    #         while True:
    #             for i in reversed(range(r)):
    #                 if indices[i] != i + n - r:
    #                     break
    #             else:
    #                 return
    #             indices[i] += 1
    #             for j in range(i + 1, r):
    #                 indices[j] = indices[j - 1] + 1
    #
    #             yield tuple(pool[i] for i in indices)
    #
    # listP = list(combinations(listActions, 10))
    # for i in listP:
    #     countPortefeuille += 1
    #     print("portefeuille", countPortefeuille, len(i))

    def combinations(target, listActions):
        for i in range(len(listActions)):
            new_target = copy.copy(target)
            new_data = copy.copy(listActions)
            new_target.append(listActions[i])
            new_data = listActions[i + 1:]
            # print(new_target)
            combinations(new_target, new_data)

    target = []
    combinations(target, listActions)

    # for x in listActions:
    #     for y in listActions:
    #         for v in listActions:
    #             if (y[1] == v[1]):
    #                 break
    #             for z in listActions:
    #                 if (v[1] == z[1]):
    #                     break
    #                 countPortefeuille += 1
    #                 print("portefeuille",countPortefeuille,(x[0], y[1], v[1], z[1]))

    # p = [([i for i in (x[0], y[1])]) for x in listActions for y in listActions]

    # def combinations(listActions,20):
    #     pool = tuple(iterable)

    # product(listActions)
