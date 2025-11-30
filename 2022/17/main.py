def parseData():
    return open('2022/17/input.txt', 'r').read().replace('\n', "")

def getPieces():
    return [
        [
            ['.', '.', '@', '@', '@', '@' , '.']
        ],
        [
            ['.', '.', '.', '@', '.', '.' , '.'],
            ['.', '.', '@', '@', '@', '.' , '.'],
            ['.', '.', '.', '@', '.', '.' , '.']
        ],
        [
            ['.', '.', '@', '@', '@', '.' , '.'],
            ['.', '.', '.', '.', '@', '.' , '.'],
            ['.', '.', '.', '.', '@', '.' , '.']
        ],
        [
            ['.', '.', '@', '.', '.', '.' , '.'],
            ['.', '.', '@', '.', '.', '.' , '.'],
            ['.', '.', '@', '.', '.', '.' , '.'],
            ['.', '.', '@', '.', '.', '.' , '.']
        ],
        [
            ['.', '.', '@', '@', '.', '.' , '.'],
            ['.', '.', '@', '@', '.', '.' , '.']
        ]
    ]

def firstHalf():
    totalpieces = 1000000000000

    deltaPiece = 50 - 15
    deltaLen = 131 - 78
    firstPiece = 50

    deltaPiece = 3415 - 1710
    deltaLen = 5173 - 2591
    firstPiece = 1710

    piecesToCalculate = ((1000000000000 - 5) % 1705) + 5 + 1705
    highToAdd = (((1000000000000 - 5 - 1705) // 1705) * 1582)

    piecesToCalculate = ((totalpieces - firstPiece) % deltaPiece) + firstPiece
    highToAdd = (((totalpieces - firstPiece) // deltaPiece) * deltaLen)

    print("piecesToCalculate", piecesToCalculate)
    print("h to add", highToAdd)
    windList = parseData()
    print("len data", len(windList))
    windLength = len(windList)
    pieces = getPieces()
    grid = [['#' for _ in range(7)]]
    move = 0

    ppcm = 5 * len(windList)

    #displayGrid(grid)

    #return

    for iPiece in range(piecesToCalculate):
        if iPiece % 100000 == 0:
            print("group n", iPiece // 100000)

        piece = getPieces()[iPiece % 5]

        #find grid top
        top = 1
        while grid[-top] == ['.', '.', '.', '.', '.', '.' , '.']:
            top += 1

        #if iPiece % ppcm < 2:
        #if iPiece % 5 == 0 and move % windLength == 1:
        #print("move % windLength", move % windLength, move)
        if iPiece % 5 == 0 and move % windLength == 2:
            print("")
            print("by 5", iPiece % 5)
            #print("by w", iPiece % 5)
            print("iPiece", iPiece)
            print("piece", piece)
            print("wind", windList[move % windLength])
            print("lentop", len(grid) - top)
            print("grid")
            displayGrid(grid[-10:])
            #return

        #print(grid[-top])

        if grid[-top] == ['#', '#', '#', '#', '#', '#', '#'] and top != 1:
            print(iPiece)
            #displayGrid(grid)
            return

        #find fill with blank to prepare next piece
        grid += [['.', '.', '.', '.', '.', '.' , '.'] for _ in range(top, 4)]

        for _ in range(4, top):
            grid.pop()

        #next piece appears in grid
        for line in piece:
            grid.append(line)

        #get cases occupied by the piece
        pieceCases = []
        for y, line in enumerate(reversed(grid)):
            containsPiece = False
            for x, case in enumerate(line):
                if case == '@':
                    pieceCases.append((x, -y - 1))
                    containsPiece = True
            if not containsPiece:
                break

        while True:
            #displayGrid(grid)
            wind = windList[move % windLength]
            move += 1

            #print(wind)
            #Check if the gas can move the piece
            canMove = True
            for x, y in pieceCases:
                if (wind == '<' and (x == 0 or grid[y][x - 1] == '#')) or (wind == '>' and (x == 6 or grid[y][x + 1] == '#')):
                    canMove = False
                    break
            
            #move
            if canMove:
                for x, y in pieceCases:
                    grid[y][x] = '.'
                
                newPieceCases = []
                for x, y in pieceCases:
                    if wind == '<':
                        grid[y][x - 1] = '@'
                        newPieceCases.append((x - 1, y))
                    else:
                        grid[y][x + 1] = '@'
                        newPieceCases.append((x + 1, y))

                pieceCases = newPieceCases

            #displayGrid(grid)

            #Check if the piece can fall
            canFall = True
            for x, y in pieceCases:
                if grid[y - 1][x] == '#':
                    canFall = False
                    break

            #fall or rest
            if canFall:
                for x, y in pieceCases:
                    grid[y][x] = '.'

                newPieceCases = []
                for x, y in pieceCases:
                    grid[y - 1][x] = '@'
                    newPieceCases.append((x, y - 1))

                pieceCases = newPieceCases
            
            else:
                for x, y in pieceCases:
                    grid[y][x] = '#'
                break

    top = 1
    while grid[-top] == ['.', '.', '.', '.', '.', '.' , '.']:
        top += 1
    #displayGrid(grid)
    #print(len(grid) - top)

    print(len(grid) - top + highToAdd)

def displayGrid(grid):
    for line in reversed(grid):
        print("".join(line))

firstHalf()
