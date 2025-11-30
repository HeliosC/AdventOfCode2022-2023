import re

def parseData():
    with open('2023/4/input.txt', 'r') as f:
        data = []
        for match in re.finditer(r"Card +(\d+): +(.+) \| +(.+)", f.read()):
            (id, rawWinnings, rawNumbers) = match.groups()
            winnings = getNumbers(rawWinnings)
            numbers = getNumbers(rawNumbers)
            data.append([winnings, numbers])  

    return data

def getNumbers(input):
    return [int(number) for number in re.split(r' +', input)]

def getMatchingNulmber(numbers, winnings):
    nMatches = 0
    for number in numbers:
        nMatches += (number in winnings)
    return nMatches

def firstHalf():    
    data = parseData()
    sum = 0
    for (winnings, numbers) in data:
        nMatches = getMatchingNulmber(numbers, winnings)
        if nMatches > 0:
            sum += 2**(nMatches-1)
    print(sum)

def secondhalf():
    data = parseData()
    cardsNumber = [1] * len(data)
    for i, (winnings, numbers) in enumerate(data):
        nMatches = getMatchingNulmber(numbers, winnings)
        for j in range(i + 1, i + nMatches + 1):
            cardsNumber[j] += cardsNumber[i]
    print(sum(cardsNumber))

secondhalf()