import functools

cards = ['A', 'K', 'Q', 'J', 'T'] + [str(i) for i in range(9, 1, -1)]
cards2 = ['A', 'K', 'Q', 'T'] + [str(i) for i in range(9, 1, -1)] + ['J']

def parseData():
    data = []
    with open('2023/7/input.txt', 'r') as f:
        for line in f.readlines():
            dataSplitted = line.replace("\n", "").split(" ")
            data.append((dataSplitted[0], int(dataSplitted[1])))
    return data

def handTypeValue(hand):
    symbols = {}
    for card in hand:
        if card in symbols:
            symbols[card] += 1
        else:
            symbols[card] = 1

    return getTypeBySymbols(symbols)

def handTypeValue2(hand):
    symbols = {}
    jNumber = 0
    for card in hand:
        if card == 'J':
            jNumber += 1
            continue

        if card in symbols:
            symbols[card] += 1
        else:
            symbols[card] = 1

    bestSympbolMultiplicity = 0
    bestSymbol = 'J'
    for (symbol, multiplicity) in symbols.items():
        if multiplicity > bestSympbolMultiplicity:
            bestSympbolMultiplicity = multiplicity
            bestSymbol = symbol

    if bestSymbol == 'J':
        symbols[bestSymbol] = jNumber
    else:
        symbols[bestSymbol] += jNumber

    return getTypeBySymbols(symbols)

def getTypeBySymbols(symbols):
    multiplicities = list(symbols.values())
    if 5 in multiplicities:
        return 6
    if 4 in multiplicities:
        return 5
    if 3 in multiplicities:
        if 2 in multiplicities:
            return 4
        else:
            return 3
    if 2 in multiplicities:
        multiplicities.remove(2)
        if 2 in multiplicities:
            return 2
        else:
            return 1
    return 0

def compareDataByHand(data1, data2):
    return compareHands(data1[0], data2[0])

def compareHands(hand1, hand2):
    if hand1 == hand2:
        return 0
    
    for i, card1 in enumerate(hand1):
        card1Value = cards.index(card1)
        card2Value = cards.index(hand2[i])
        if card1Value < card2Value:
            return 1
        elif card1Value > card2Value:
            return -1
    
def compareDataByHand2(data1, data2):
    return compareHands2(data1[0], data2[0])

def compareHands2(hand1, hand2):
    if hand1 == hand2:
        return 0
    
    for i, card1 in enumerate(hand1):
        card1Value = cards2.index(card1)
        card2Value = cards2.index(hand2[i])
        if card1Value < card2Value:
            return 1
        elif card1Value > card2Value:
            return -1

def firstHalf():    
    data = parseData()
    handsByType = [[], [], [], [], [], [], []]
    for (hand, bid) in data:
        handsByType[handTypeValue(hand)].append((hand, bid))

    for i, hands in enumerate(handsByType):
        handsByType[i] = sorted(hands, key=functools.cmp_to_key(compareDataByHand))

    total = 0
    rank = 1
    for hands in handsByType:
        for (hand, bid) in hands:
            total += bid * rank
            rank += 1

    print(total)

def secondHalf():    
    data = parseData()
    handsByType = [[], [], [], [], [], [], []]
    for (hand, bid) in data:
        handsByType[handTypeValue2(hand)].append((hand, bid))

    for i, hands in enumerate(handsByType):
        handsByType[i] = sorted(hands, key=functools.cmp_to_key(compareDataByHand2))

    total = 0
    rank = 1
    for hands in handsByType:
        for (hand, bid) in hands:
            total += bid * rank
            rank += 1

    print(total)

secondHalf()
