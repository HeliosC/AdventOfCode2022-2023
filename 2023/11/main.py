def parseData():
    with open('2023/11/input.txt', 'r') as f:
        data = [[char for char in line.replace("\n", "")] for line in f.readlines()]
    return data

def printData(data):
    for line in data:
        print("".join(line))

def firstHalf():
    distanceSum = 0
    data = parseData()

    # Expand universe
    for y in range(-len(data), 0):
        if all(char == '.' for char in data[y]):
            data.insert(y, ['.'] * len(data[0]))

    for x in range(-len(data[0]), 0):
        if all(line[x] == '.' for line in data):
            for line in data:
                line.insert(x, '.')

    galaxies = findGalaxies(data)

    for i, (x1, y1) in enumerate(galaxies):
        for j in range(i):
            (x2, y2) = galaxies[j]
            distanceSum += abs(x2-x1) + abs(y2-y1)

    print(distanceSum)

def secondHalf():
    EXPAND_FACTOR = 1000000
    distanceSum = 0
    data = parseData()

    # "Expand" universe
    linesToExpand = []
    columnsToExpand = []

    for y in range(len(data)):
        if all(char == '.' for char in data[y]):
            linesToExpand.append(y)

    for x in range(len(data[0])):
        if all(line[x] == '.' for line in data):
            columnsToExpand.append(x)

    galaxies = findGalaxies(data)

    for i, (x1, y1) in enumerate(galaxies):
        for j in range(i):
            (x2, y2) = galaxies[j]
            xmin, xmax = min(x1, x2), max(x1, x2)
            ymin, ymax = min(y1, y2), max(y1, y2)

            expandedLines = 0
            for line in linesToExpand:
                if line < ymax:
                    if line > ymin:
                        expandedLines += 1
                else:
                    break

            expandedColumns = 0
            for column in columnsToExpand:
                if column < xmax:
                    if column > xmin:
                        expandedColumns += 1
                else:
                    break

            distanceSum += (xmax-xmin) + (ymax-ymin) + (EXPAND_FACTOR-1) * (expandedColumns + expandedLines)

    print(distanceSum)

def findGalaxies(data):
    galaxies = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x,y))
    return galaxies

secondHalf()