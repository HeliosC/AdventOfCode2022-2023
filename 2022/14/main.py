import sys

def parseData():
    return [[[int(coord) for coord in corner.split(',')] for corner in line.replace("\n", "").split(" -> ")] for line in open("2022/14/input.txt", "r").readlines()]

def firstHalf():
    data = parseData()
    minX = sys.maxsize
    maxX = 0
    maxY = 0
    for line in data:
        for subline in line:
            if minX > subline[0]:
                minX = subline[0]
            if maxX < subline[0]:
                maxX = subline[0]
            if maxY < subline[1]:
                maxY = subline[1]

    map = [['.' for x in range(minX, maxX + 1)] for y in range(maxY + 1)]

    for line in data:
        for subline in range(len(line) - 1):
            (x1, y1) = line[subline]
            (x2, y2) = line[subline + 1]

            if(x1 == x2):
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    map[y][x1 - minX] ='#'

            elif(y1 == y2):
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    map[y1][x - minX] ='#'

    for line in map:
        print("".join(line))

    sands = 0
    while dropSand(map, minX, maxX, maxY):
        sands += 1
    print()
    for line in map:
        print("".join(line))
    
    print(sands)
            
def dropSand(map, minX, maxX, maxY):
    sand = [500, 0]
    while True:
        x, y = sand
        if y + 1 > maxY:
            return False
        elif map[y + 1][x - minX] == '.':
            sand[1] += 1
        elif x - 1 < minX:
            return False
        elif map[y + 1][x - 1 - minX] == '.':
            sand[0] -= 1
            sand[1] += 1
        elif x + 1 > maxX:
            return False
        elif map[y + 1][x + 1 - minX] == '.':
            sand[0] += 1
            sand[1] += 1
        else:
            map[y][x - minX] = 'o'
            return True

def secondHalf():
    data = parseData()
    minX = sys.maxsize
    maxX = 0
    maxY = 0
    for line in data:
        for subline in line:
            if minX > subline[0]:
                minX = subline[0]
            if maxX < subline[0]:
                maxX = subline[0]
            if maxY < subline[1]:
                maxY = subline[1]

    maxY += 2

    map = [['.' for x in range(minX, maxX + 1)] for y in range(maxY)]
    map.append(['#' for x in range(minX, maxX + 1)])

    for line in data:
        for subline in range(len(line) - 1):
            (x1, y1) = line[subline]
            (x2, y2) = line[subline + 1]

            if(x1 == x2):
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    map[y][x1 - minX] ='#'

            elif(y1 == y2):
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    map[y1][x - minX] ='#'

    for line in map:
        print("".join(line))

    sands = 1
    #for i in range(100):
        #print("step", i)
    while extremum := dropSand2(map, minX, maxX, maxY):
        #extremum = dropSand2(map, minX, maxX, maxY)
        minX, maxX = extremum
        sands += 1
    print()
    map[0][500 - minX] = 'O'
    for line in map:
        print("".join(line))
    
    print(sands)
            
def dropSand2(map, minX, maxX, maxY):
    sand = [500, 0]
    while True:
        x, y = sand
        #print("SAND", x, y)
        if y == maxY - 1:
            #print("MAAAAAAAAX", x - minX)
            map[y][x - minX] = 'o'
            return minX, maxX
        elif map[y + 1][x - minX] == '.':
            sand[1] += 1
        elif x - 1 < minX:
            #print("EXTENF LEFT")
            for line in range(len(map)):
                map[line] = ['.'] + map[line]
            map[-1][0] = '#'
            minX -= 1

            sand[0] -= 1
            sand[1] += 1
        elif map[y + 1][x - 1 - minX] == '.':
            sand[0] -= 1
            sand[1] += 1
        elif x + 1 > maxX:
            #print("EXTENF RIGHT")
            for line in range(len(map)):
                map[line].append('.')
            map[-1][-1] = '#'
            maxX +=1

            sand[0] += 1
            sand[1] += 1
        elif map[y + 1][x + 1 - minX] == '.':
            sand[0] += 1
            sand[1] += 1
        else:
            if sand[1] == 0:
                return False
            else:
                #print(x - minX, y)
                map[y][x - minX] = 'o'
                return minX, maxX
secondHalf()