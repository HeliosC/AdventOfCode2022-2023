import re
input = open("2023/1/input.txt", "r")

def findCalibration(line):
    start = 0
    end = -1
    lineLen = len(line)
    while start < lineLen and not line[start].isdigit():
        start += 1

    while end > -lineLen and not line[end].isdigit():
        end -= 1

    if end <= -lineLen and start >= lineLen:
        return 0
    elif end <= -lineLen:
        return int(line[start] + line[start])
    elif start >= lineLen:
        return int(line[end] + line[end])
    else:
        return int(line[start] + line[end])

def firstHalf():    
    calibrationSum = 0
    while line := input.readline():
        calibrationSum += findCalibration(line)

    print(calibrationSum)

def secondHalf():    
    digitLetters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibrationSum = 0
    while line := input.readline():
        lineLen = len(line)
        newline = ""
        for i, char in enumerate(line):
            if char.isdigit():
                newline += char
                continue

            for index, digit in enumerate(digitLetters):
                digitLen = len(digit)
                if (i + digitLen) <= lineLen and line[i : i + digitLen] == digit:
                    newline += str(index + 1)
                    break 

        calibrationSum += findCalibration(newline)

    print(calibrationSum)

digitLetters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def findFirstDigit(line):
    lineLen = len(line)
    for i, char in enumerate(line):
        if char.isdigit():
            return char
        
        for index, digit in enumerate(digitLetters):
            digitLen = len(digit)
            if (i + digitLen) <= lineLen and line[i : i + digitLen] == digit:
                return str(index + 1)
    else:
        return "0"
    
def findLastDigit(line):
    lineLen = len(line)
    for i in range(-1, -lineLen - 1, -1):
        char = line[i]
        if char.isdigit():
            return char
        
        for index, digit in enumerate(digitLetters):
            digitLen = len(digit)
            if (i - digitLen + 1) >= -lineLen and line[i - digitLen + 1 : i + 1] == digit:
                return str(index + 1)
    else:
        return "0"

def secondHalfBis():    
    calibrationSum = 0
    while line := input.readline():
        calibrationSum += int(findFirstDigit(line) + findLastDigit(line))
    print(calibrationSum)

secondHalfBis()