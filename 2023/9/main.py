def parseData():
    with open('2023/9/input.txt', 'r') as f:
        data = []
        for line in f.readlines():
            data.append([int(value) for value in line.replace("\n", "").split(" ")])
    return data

def firstHalf():
    extrapolatedValuesSum = 0
    data = parseData()
    for history in data:
        sequence = history
        sequences = [sequence]
        while not containsSameValue(sequence):
            newSequence = []
            for i in range(len(sequence) - 1):
                newSequence.append(sequence[i+1] - sequence[i])
            sequences.append(newSequence)
            sequence = newSequence

        extrapolatedValue = sum([sequence[-1] for sequence in sequences])
        extrapolatedValuesSum += extrapolatedValue
    print(extrapolatedValuesSum)

def secondHalf():
    extrapolatedValuesSum = 0
    data = parseData()
    for history in data:
        sequence = history
        sequences = [sequence]
        while not containsSameValue(sequence):
            newSequence = []
            for i in range(len(sequence) - 1):
                newSequence.append(sequence[i+1] - sequence[i])
            sequences.append(newSequence)
            sequence = newSequence

        extrapolatedValue = sum([sequence[0] * (-1)**i for i, sequence in enumerate(sequences)])
        extrapolatedValuesSum += extrapolatedValue
    print(extrapolatedValuesSum)

def containsSameValue(list):
    firstValue = list[0]
    for item in list:
        if item != firstValue:
            return False
    else:
        return True
            
secondHalf()