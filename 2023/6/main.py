import re
import math

def parseData1():
    with open('2023/6/input.txt', 'r') as f:
        times = [int(time) for time in re.split(r' +', f.readline().replace("\n", ""))[1:]]
        distances = [int(distance) for distance in re.split(r' +', f.readline().replace("\n", ""))[1:]]
        
    return [(times[i], distances[i]) for i in range(len(times))]

def parseData2():
    with open('2023/6/input.txt', 'r') as f:
        time = int("".join(re.split(r' +', f.readline().replace("\n", ""))[1:]))
        distance = int("".join(re.split(r' +', f.readline().replace("\n", ""))[1:]))
        
    return (time, distance)

def waysToWinValue(time, distance):
    return 2 * round(math.sqrt(time**2 - 4*distance) / 2) - (time+1)%2

    decimalValue = math.sqrt(time * time - 4 * distance)
    if time % 2 == 0:
        return 2 * round((decimalValue - 1) / 2) + 1
    else:
        return 2 * round(decimalValue / 2)

def firstHalf():    
    data = parseData1()
    total = 1
    for (time, distance) in data:
        total *= waysToWinValue(time, distance)
    print(total)

def secondHalf():    
    (time, distance) = parseData2()
    print(waysToWinValue(time, distance))

firstHalf()
secondHalf()