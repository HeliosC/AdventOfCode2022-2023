import re
input = open("2023/3/input.txt", "r")

def parseData():
    data = ["." + line.replace("\n", "") + "." for line in input.readlines()]
    return ["."* len(data[0])] + data + ["."* len(data[0])]

def firstHalf():    
    data = parseData()
    partnumberSum = 0
    for y, line in enumerate(data):
        x = 0
        lineLen = len(line)
        while x < lineLen:
            numberEnd = x 
            while line[numberEnd].isdigit():
                numberEnd += 1
            if numberEnd != x:
                number = int(line[x : numberEnd])
                if(isPartNumber(x, numberEnd, y, data)):
                    partnumberSum += number
                
            x = numberEnd + 1 

    print(partnumberSum)

def isPartNumber(x, x2, y, data):
    for xi in range(x - 1, x2 + 1):
        if data[y - 1][xi] != '.' or data[y + 1][xi] != '.':
            return True
    if data[y][x - 1] != '.' or data[y][x2] != '.':
        return True
    return False

def secondHalf():
    data = parseData()
    gearSum = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '*':
                numbers = []
                #Left
                if data[y][x - 1].isdigit():
                    numbers.append(findNumber(x - 1, y, data))

                #Right
                if data[y][x + 1].isdigit():
                    numbers.append(findNumber(x + 1, y, data))

                #Top
                if data[y - 1][x].isdigit():
                    numbers.append(findNumber(x, y - 1, data))
                else:
                    if data[y - 1][x - 1].isdigit():
                        numbers.append(findNumber(x - 1, y - 1, data))
                    if data[y - 1][x + 1].isdigit():
                        numbers.append(findNumber(x + 1, y - 1, data))

                #Bot
                if data[y + 1][x].isdigit():
                    numbers.append(findNumber(x, y + 1, data))
                else:
                    if data[y + 1][x - 1].isdigit():
                        numbers.append(findNumber(x - 1, y + 1, data))
                    if data[y + 1][x + 1].isdigit():
                        numbers.append(findNumber(x + 1, y + 1, data))
            
                if len(numbers) == 2:
                    gearSum += numbers[0] * numbers[1]
    print(gearSum)

def findNumber(x, y, data):
    x1 = x
    x2 = x
    while data[y][x1].isdigit():
        x1 -= 1
    while data[y][x2].isdigit():
        x2 += 1    
    return int(data[y][x1+1:x2])

secondHalf()