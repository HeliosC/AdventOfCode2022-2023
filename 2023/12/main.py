from time import time
from itertools import combinations
from functools import cache

def parseData():
    with open('2023/12/input.txt', 'r') as f:
        data = []
        for line in f.readlines():
            records = line.replace('\n', '').split(' ')
            data.append(([value for value in records[0]], [int(damage) for damage in records[1].split(',')]))
    return data

def firstHalf():
    arrangementsSum = 0
    data = parseData()

    for (record, damages) in data:
        totalDamage = sum(damages)
        knownDamages = record.count('#')
        unknownDamages = totalDamage - knownDamages
        damagesSpots = [i for i, x in enumerate(record) if x == "?"]

        for combinaison in list(combinations(damagesSpots, unknownDamages)):
            candidate = record[:]
            for index in combinaison:
                candidate[index] = '#'
            
            #Is combinaison valid
            candidateDamages = []
            currentDamage = 0
            isDamaged = False
            for r in candidate:
                if r == '#':
                    if isDamaged:
                        currentDamage += 1
                    else:
                        isDamaged = True
                        currentDamage = 1
                else:
                    if isDamaged:
                        isDamaged = False
                        candidateDamages.append(currentDamage)
                        currentDamage = 0
            if currentDamage > 0:
                candidateDamages.append(currentDamage)

            if candidateDamages == damages:
                arrangementsSum += 1

    print(arrangementsSum)

variationsCache = {}
def secondHalf():
    t1 = time()
    arrangementsSum = 0
    data = parseData()

    for i, (record, damages) in enumerate(data):
        variationsCache = {}

        record = "." + "".join(record) + "."
        record = "." + "?".join(["".join(record) for i in range(5)]) + "."
        damages = [damage for i in range(5) for damage in damages]

        arragements = calculateVariations(record, damages, 0)
        print(arragements)
        arrangementsSum += arragements

    print(arrangementsSum)
    print(time()-t1)

def calculateVariations(record, damages, iDamage):
    cacheKey = record + "|" + ",".join([str(damage) for damage in damages]) + "|" + str(iDamage)
    cachedValue = variationsCache.get(cacheKey) 
    if cachedValue:
        return cachedValue

    variations = 0
    damage = damages[iDamage]
    for (start, end) in nextCursors(record, damage):
        nextCusror = end
        if iDamage < len(damages) - 1:
            variations += calculateVariations(record[nextCusror:], damages, iDamage + 1)
        else:
            if '#' not in record[nextCusror:]:
                variations += 1

    variationsCache[cacheKey] = variations
    return variations

@cache
def nextCursors(record, damage):
    cursors = []
    recordLen = len(record)
    firstDamageInRecord = record.find('#')
    if firstDamageInRecord == -1:
        maxCursor = recordLen - damage
    else:
        maxCursor = min(firstDamageInRecord + damage, recordLen - damage)

    for i in range(1, maxCursor):
        if record[i-1] != '#' and all(record[j] in ('#', '?') for j in range(i, i+damage)) and record[i+damage] != '#':
            cursors.append((i, i+damage))
    return cursors

secondHalf()