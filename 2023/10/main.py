def parseData():
    with open('2023/10/input.txt', 'r') as f:
        data = [[char for char in line.replace("\n", "")] for line in f.readlines()]
    return data

pipes = {
    '|' : ((0, -1), (0, 1)),
    '-' : ((-1, 0), (1, 0)),
    'L' : ((0, -1), (1, 0)),
    'J' : ((0, -1), (-1, 0)),
    '7' : ((-1, 0), (0, 1)),
    'F' : ((1, 0), (0, 1)),
    '.' : ((0, 0), (0, 0))
}

def firstHalf():
    pathLen = 0
    data = parseData()
    (previousX, previousY) = findStart(data)
    (x, y) = findConnectedPipe(data, previousX, previousY)
    while data[y][x] != 'S':
        (newX, newY) = findNextPipe(data, x, y, previousX, previousY)
        (previousX, previousY) = (x, y)
        (x, y) = (newX, newY)
        pathLen += 1

    print((pathLen + 1) / 2)

def secondHalf():
    data = parseData()
    enclosedTiles = 0

    (previousX, previousY) = findStart(data)
    (x, y) = findConnectedPipe(data, previousX, previousY)
    path = [(x, y)]
    while data[y][x] != 'S':
        (newX, newY) = findNextPipe(data, x, y, previousX, previousY)
        (previousX, previousY) = (x, y)
        (x, y) = (newX, newY)
        path.append((x,y))

    data[y][x] = 'J'

    for ys, line in enumerate(data):
        for xs, pipe in enumerate(line):
            if (xs, ys) not in path:
                data[ys][xs] = " "

    for ys, line in enumerate(data):
        for xs, pipe in enumerate(line):
            if (xs,ys) in path:
                continue

            left = line[:xs]
            walls = 0
            while True:
                if 'L' in left and '7' in left:
                    left.remove('L')
                    left.remove('7')
                    walls += 1
                else:
                    break

            while True:
                if 'J' in left and 'F' in left:
                    left.remove('J')
                    left.remove('F')
                    walls += 1
                else:
                    break
            
            for char in left:
                if char == '|':
                    walls += 1

            if walls % 2 == 1:
                enclosedTiles += 1
    
    print(enclosedTiles)

                    

def findStart(data):
    for ys, line in enumerate(data):
        for xs, pipe in enumerate(line):
            if pipe == 'S':
                return (xs, ys)
            
def findConnectedPipe(data, x, y):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
                
            newX = x + dx
            newY = y + dy
            ((xEntry, yEntry), (xExit, yExit)) = pipes[data[newY][newX]]

            if (newX + xEntry == x and newY + yEntry == y) or (newX + xExit == x and newY + yExit == y):
                return newX, newY
            
def findNextPipe(data, x, y, previousX, previousY):
    ((xEntry, yEntry), (xExit, yExit)) = pipes[data[y][x]]
    if (x + xEntry != previousX or y + yEntry != previousY):
        return (x + xEntry, y + yEntry)
    else:
        return (x + xExit, y + yExit)

def printData(data):
    for line in data:
        print("".join(line))

secondHalf()