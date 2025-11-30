import re
from sys import maxsize

def parseData():
    with open('2023/5/input.txt', 'r') as f:
        seeds = [int(seed) for seed in f.readline().replace("\n", "").split(": ")[1].split(" ")]
        data = [seeds]
        for match in re.finditer(r":\n(.+?)\n\n", f.read(), re.MULTILINE | re.DOTALL):
            categories = []
            lines = match.groups()[0].split("\n")
            for line in lines:
                categories.append([int(value) for value in line.split(" ")])

            categoriesSorted = []
            while len(categories) > 0:
                sourceMin = categories[0][1]
                categoryMin = categories[0]
                for category in categories:
                    (destinationStart, sourceStart, rangeLen) = category
                    if sourceStart < sourceMin:
                        sourceMin = sourceStart
                        categoryMin = category
                categoriesSorted.append(categoryMin)
                categories.remove(categoryMin)

            data.append(categoriesSorted)

    return data

def getDestination(source, category):
    for (destinationStart, sourceStart, rangeLen) in category:
        if source >= sourceStart and source < sourceStart + rangeLen:
            return destinationStart + source - sourceStart
    else:
        return source
    
def getDestinations(sourceStart, sourceRange, category):
    destinations = []
    sourceEnd = sourceStart + sourceRange
        
    for (destinationDataStart, sourceDataStart, rangeDataLen) in category:
        if sourceStart < sourceDataStart:
            destinations.append(sourceStart)
            newSourceStart = min(sourceEnd, sourceDataStart)
            destinations.append(newSourceStart - sourceStart)
            sourceStart = newSourceStart
        if sourceStart < sourceDataStart + rangeDataLen:
            destinations.append(destinationDataStart + sourceStart - sourceDataStart)
            newSourceStart = min(sourceEnd, sourceDataStart + rangeDataLen)
            destinations.append(newSourceStart - sourceStart)
            sourceStart = newSourceStart

        if sourceStart == sourceEnd:
            break

    if sourceStart != sourceEnd:
        destinations.append(sourceStart)
        destinations.append(sourceEnd - sourceStart)

    return destinations

def firstHalf():    
    data = parseData()
    destinationMin = maxsize
    for seed in data[0]:
        source = seed
        for category in data[1:]:
            source = getDestination(source, category)
        if (source < destinationMin):
            destinationMin = source
    print(destinationMin)

def secondHalf():    
    data = parseData()
    sources = data[0]
    for category in data[1:]:
        newSources = []
        sourcesLen = len(sources) // 2
        for iSeed in range (sourcesLen):
            (startSeed, nSeed) = (sources[2 * iSeed], sources[2 * iSeed + 1])
            newSources += getDestinations(startSeed, nSeed, category)
        sources = newSources

    destinationMin = min(sources[2::2])
    print(destinationMin)

secondHalf()