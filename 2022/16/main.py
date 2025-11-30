import re
import math
import sys
import itertools

REGEX = r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)"

def parseData():
    valves = {}
    with open('2022/16/input.txt', 'r') as f:
        for match in re.finditer(REGEX, f.read()):
            (id, flowRate, tunnels) = match.groups()
            valves[id] = {
                'flowRate': int(flowRate),
                'tunnels': tunnels.split(", ")
            }
    return valves

nodes = {
    'S': { 
        'T': 8,
        'E': 10,
        'L': 5,
        'N': 8
    },
    'T': {
        'S': 8,
        'E': 4
    },
    'E': {
        'T': 4,
        'S': 10,
        'L': 8,
        'M': 10
    },
    'L': {
        'E': 8,
        'S': 5,
        'N': 2,
        'M': 7
    },
    'N': {
        'L': 2,
        'S': 8,
        'M': 4
    },
    'M': {
        'N': 4,
        'L': 7,
        'E': 10
    }
}

def firstHalf():
    nodes = parseData()
    valves = list(filter(lambda node: nodes[node]['flowRate'] != 0, nodes))
    print(valves)
    weigths = {'AA': {}}

    for node in (path := dijkstra('AA', nodes)):
        if node in valves:
            weigths['AA'][node] = path[node]

    for valve in valves:
        weigths[valve] = {}
        for node in (path := dijkstra(valve, nodes)):
            if node in valves:
                weigths[valve][node] = path[node]

    #for node in weigths:
    #    print(node, weigths[node])

    
    result = visitNextNodes(['AA'], set(valves), 30, nodes, weigths, 0)
    print(result[0][:10])


    #print(len(list(itertools.permutations([i for i in range(12)]))))

    #result = visitNextNodes2(['AA'], set(valves), weigths)

    #index = result[0].index((['AA', 'JJ', 'BB', 'CC'], ['AA', 'DD', 'HH', 'EE']))
    #index = result[0].index(['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC'])
    print("-----")
    #print(result)
    #print(len(result))

    #deep0('AA', set(valves), nodes, weigths)
    #deep1('AA', set(valves), nodes, weigths)


def visitNextNodes(path, valvesLeft, timeLeft, nodes, weigths, score):
    currentNode = path[-1]
    #print(path)

    newPath = []
    scores = []
    for valve in valvesLeft:
        remainingTime = timeLeft - weigths[currentNode][valve] - 1
        #print(currentNode, valve, remainingTime, valvesLeft)
        if True or remainingTime > 0:
            if len(valvesLeft) == 1:
                newPath += [path + [valve]]
                scores += [score + remainingTime * nodes[valve]['flowRate']]
                #scores += [score + [(remainingTime, nodes[valve]['flowRate'])]]
            else:
                newValvesLeft = valvesLeft.copy()
                newValvesLeft.discard(valve)
                result = visitNextNodes(path + [valve], newValvesLeft, remainingTime, nodes, weigths, score + remainingTime * nodes[valve]['flowRate'])
                #result = visitNextNodes(path + [valve], newValvesLeft, remainingTime, nodes, weigths, score + [(remainingTime, nodes[valve]['flowRate'])])
                newPath += result[0]
                scores += result[1]
        else:
            newPath += [path]
            #scores += [score]
            scores += [score]

    #print("END", newPath)
    #print("END")

    return newPath, scores

def visitNextNodes2(path, valvesLeft, weigths):
    paths = []
    for valve in valvesLeft:
        if ((lenv := len(valvesLeft)) > 9):
            print('M', lenv, valve)

        if len(valvesLeft) == 1:
            paths += [path + [valve]]
        else:
            newValvesLeft = valvesLeft.copy()
            newValvesLeft.discard(valve)
            visitNextNodes2(path + [valve], newValvesLeft, weigths)
            #paths += visitNextNodes2(path + [valve], newValvesLeft, weigths)

    return #paths

def deep0(start, valvesLeft, nodes, weigths):
    pahtMe = [start]
    pathElephant = [start]

    timeLeftMe = 26
    timeLeftElephant = 26

    score = 0

    while valvesLeft:
        currentNodeMe = pahtMe[-1]
        currentNodeElephant = pathElephant[-1]

        maxPotentialMe = 0
        maxPotentialTimeMe = 0
        maxPotentialValveMe = ""

        maxPotentialElephant = 0
        maxPotentialTimeElephant = 0
        maxPotentialValveElephant = ""
        
        for valve in valvesLeft:
            newTimeMe = timeLeftMe - (weigths[currentNodeMe][valve] + 1)
            newPotentialMe = newTimeMe * nodes[valve]['flowRate']
            if newPotentialMe > maxPotentialMe:
                maxPotentialMe = newPotentialMe
                maxPotentialTimeMe = newTimeMe
                maxPotentialValveMe = valve

            newTimeElephant = timeLeftElephant - (weigths[currentNodeElephant][valve] + 1)
            newPotentialElephant = newTimeElephant * nodes[valve]['flowRate']
            if newPotentialElephant > maxPotentialElephant:
                maxPotentialElephant = newPotentialElephant
                maxPotentialTimeElephant = newTimeElephant
                maxPotentialValveElephant = valve

        if maxPotentialMe >= maxPotentialElephant:
            pahtMe += [maxPotentialValveMe]
            timeLeftMe = maxPotentialTimeMe
            score += maxPotentialMe

            valvesLeft.discard(maxPotentialValveMe)
            #print('Me', maxPotentialValveMe, maxPotentialTimeMe, maxPotentialMe)
        else:
            pathElephant += [maxPotentialValveElephant]
            timeLeftElephant = maxPotentialTimeElephant
            score += maxPotentialElephant

            valvesLeft.discard(maxPotentialValveElephant)
            #print('El', maxPotentialValveElephant, maxPotentialTimeElephant, maxPotentialElephant)

        print('Me', currentNodeMe, maxPotentialValveMe, maxPotentialTimeMe, maxPotentialMe)
        print('El', currentNodeElephant, maxPotentialValveElephant, maxPotentialTimeElephant, maxPotentialElephant)
        print("------")

def deep1(start, valvesLeft, nodes, weigths):
    pahtMe = [start]
    pathElephant = [start]

    timeLeftMe = 26
    timeLeftElephant = 26

    score = 0

    while valvesLeft:
        currentNodeMe = pahtMe[-1]
        currentNodeElephant = pathElephant[-1]

        maxPotentialMe = 0
        maxPotentialDeepMe = 0
        maxPotentialTimeMe = 0
        maxPotentialValveMe = ""

        maxPotentialElephant = 0
        maxPotentialDeepElephant = 0
        maxPotentialTimeElephant = 0
        maxPotentialValveElephant = ""


        for valve in valvesLeft:
            newTimeMe = timeLeftMe - (weigths[currentNodeMe][valve] + 1)
            newPotentialMe = newTimeMe * nodes[valve]['flowRate']
            newPotentialDeepMe = newPotentialMe + calculateMaxNodePotential(valve, newTimeMe, valvesLeft, nodes, weigths, 11, 0)
            if newPotentialDeepMe > maxPotentialDeepMe:
                maxPotentialDeepMe = newPotentialDeepMe
                maxPotentialMe = newTimeMe * nodes[valve]['flowRate']
                maxPotentialTimeMe = newTimeMe
                maxPotentialValveMe = valve

            newTimeElephant = timeLeftElephant - (weigths[currentNodeElephant][valve] + 1)
            newPotentialElephant = newTimeElephant * nodes[valve]['flowRate']
            newPotentialDeepElephant = newPotentialElephant + calculateMaxNodePotential(valve, newTimeElephant, valvesLeft, nodes, weigths, 11, 0)
            if newPotentialDeepElephant > maxPotentialDeepElephant:
                maxPotentialDeepElephant = newPotentialDeepElephant
                maxPotentialElephant = newPotentialElephant
                maxPotentialTimeElephant = newTimeElephant
                maxPotentialValveElephant = valve

        if maxPotentialMe >= maxPotentialElephant:
            if maxPotentialMe == 0:
                valvesLeft = set()
                continue

            pahtMe += [maxPotentialValveMe]
            timeLeftMe = maxPotentialTimeMe
            score += maxPotentialMe

            valvesLeft.discard(maxPotentialValveMe)
            #print('Me', maxPotentialValveMe, maxPotentialTimeMe, maxPotentialMe)
        else:
            pathElephant += [maxPotentialValveElephant]
            timeLeftElephant = maxPotentialTimeElephant
            score += maxPotentialElephant

            valvesLeft.discard(maxPotentialValveElephant)
            #print('El', maxPotentialValveElephant, maxPotentialTimeElephant, maxPotentialElephant)

        #print('Me', currentNodeMe, maxPotentialValveMe, maxPotentialTimeMe, maxPotentialMe)
        #print('El', currentNodeElephant, maxPotentialValveElephant, maxPotentialTimeElephant, maxPotentialElephant)
        #print("------")

    print(pahtMe)
    print(pathElephant)
    print(score)

def calculateMaxNodePotential(valve, timeLeft, valvesLeft, nodes, weigths, deep, previousmaxPotential):
    maxPotential = 0

    for nextValve in valvesLeft:
        if valve == nextValve:
            continue

        newTime = timeLeft - (weigths[valve][nextValve] + 1)
        if deep == 1:
            newPotential = newTime * nodes[valve]['flowRate']
        else:
            newValvesLeft = valvesLeft.copy()
            newValvesLeft.discard(valve)
            deep -= 1
            newPotential = calculateMaxNodePotential(nextValve, newTime, newValvesLeft, nodes, weigths, deep, previousmaxPotential)


        if newPotential > maxPotential:
            maxPotential = newPotential

    return maxPotential


def dijkstra(start, nodes):
    unvisited = set(nodes.keys())
    weigths = {}
    for node in unvisited:
        weigths[node] = sys.maxsize

    weigths[start] = 0
    unvisited.discard(start)
    currentNode = start

    while unvisited:
        for nextNode in nodes[currentNode]['tunnels']:
            newWeigth = weigths[currentNode] + 1
            if newWeigth < weigths[nextNode]:
                weigths[nextNode] = newWeigth

        minWeigth = sys.maxsize
        for node in unvisited:
            if weigths[node] < minWeigth:
                minWeigth = weigths[node]
                currentNode = node

        unvisited.discard(currentNode)

    #print(weigths)
    #print(paths)
    return weigths

#dijkstra('M')
firstHalf()