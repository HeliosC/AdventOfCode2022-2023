import re
import time

REGEX = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
input = open("2022/15/input.txt", "r")

def firstHalf():
    ROW = 2000000
    beaconsInRaw = set()
    rowCases = set()
    while line := input.readline():
        match = re.search(REGEX, line)
        (xSensor, ySensor, xBeacon, yBeacon) = [int(i) for i in match.groups()]

        if yBeacon == ROW:
            beaconsInRaw.add(xBeacon)

        distance = manathan(xSensor, ySensor, xBeacon, yBeacon)
        distanceToRow = abs(ySensor - ROW)
        rawToCheck = distance - distanceToRow
        if rawToCheck <= 0:
            continue

        for x in range(xSensor - rawToCheck, xSensor + rawToCheck + 1):
            rowCases.add(x)

    for beacon in beaconsInRaw:
        rowCases.discard(beacon)

    #print(len(rowCases))

def secondHalf():
    MAX_COORD = 4000000
    data = [[int(i) for i in re.search(REGEX, line).groups()] for line in input.readlines()]
    print("data parsed")
    for row in range(00000, MAX_COORD + 1):
        if row % 400000 == 0:
            print(row // 400000)

        rowCases = []

        for (xSensor, ySensor, xBeacon, yBeacon) in data:
            distance = manathan(xSensor, ySensor, xBeacon, yBeacon)
            distanceToRow = abs(ySensor - row)
            rawToCheck = distance - distanceToRow
            if rawToCheck <= 0:
                continue

            rowCases = mergeIntervalsChatGPT(rowCases, [max(0, xSensor - rawToCheck), min(MAX_COORD, xSensor + rawToCheck)])
            #print(rowCases)

        for i in range(len(rowCases) - 1):
            if rowCases[i + 1][0] - rowCases[i][1] == 2:
                #print(rowCases, "y = ", row)
                print(4000000*(rowCases[i][1] + 1) + row)
                return

        #print("NEXT", rowCases)
        continue
        #print(row, len(rowCases))
        if len(rowCases) == 1:
            print("FIND", row)
            #print("FIND y ", row)
            for x in range(MAX_COORD + 1):
                if x not in rowCases:
                    #print("FIND x ", x)
                    print(4000000 * x + row)
                    break
            break


def manathan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def mergeIntervals(list, interval):
    if len(list) == 0:
        list.append(interval)
        return list

    x, y = interval

    if y < list[0][0]:
        list = [interval] + list
        return list

    for i in range(len(list) - 1):
        _, b = list[i]
        c, _ = list[i + 1]

        if b < x < c and b < y < c:
            list.insert(i + 1, interval)
            return list
    else:
        if x > list[-1][1]:
            list.append(interval)
            return list

    start = -1
    istart = -1
    end = -1
    iend = -1
    for i, item in enumerate(list):
        a, b = item
        if a <= x <= b:
            start = a
            istart = i
        elif start == -1 and x < a:
            start = x
            istart = i

        if start != -1:
            if a <= y <= b:
                end = b
                iend = i
                break
            elif y < a:
                end = y
                iend = i - 1
                break

    else:
        end = y
        iend = len(list) - 1

    list[istart] = (start, end)
    del list[istart + 1 : iend + 1]

    return list

def mergeIntervalsChatGPT(intervals, new_interval):
  # ajouter le nouvel intervalle à la liste des intervalles courants
  intervals.append(new_interval)

  # trier les intervalles par leur premier élément
  intervals.sort(key=lambda x: x[0])

  # initialiser la liste des intervalles fusionnés
  merged = []

  # parcourir chaque intervalle
  for interval in intervals:
    # s'il n'y a pas encore d'intervalle fusionné ou si l'intervalle courant ne chevauche pas l'intervalle précédemment fusionné, ajouter l'intervalle courant à la liste des intervalles fusionnés
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)
    # sinon, fusionner l'intervalle courant et l'intervalle précédemment fusionné en un seul intervalle
    else:
      merged[-1][1] = max(merged[-1][1], interval[1])

  return merged

# exemple d'utilisation
print(mergeIntervalsChatGPT([[1,3], [8,9]], [2,6]))  # [[1,6], [8,9]]
print(mergeIntervalsChatGPT([[1,3], [8,9]], [5,6]))  # [[1,3], [5,6], [8,9]]


secondHalf()

#print(mergeIntervals([[1,5], [7, 10]], [5,7]))