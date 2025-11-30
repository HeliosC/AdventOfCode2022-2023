import numpy as np
import math

def parseData():
    return open('2022/17/input.txt', 'r').read().replace('\n', "")

#ressources = {
#    'ore' : 0,
#    'clay' : 0,
#    'obsidian' : 0,
#    'geode' : 0,
#}

#robots = {
#    'ore' : 1,
#    'clay' : 0,
#    'obsidian' : 0,
#    'geode' : 0,
#}


def firstHalf():
    blueprints = np.array([
        [
            [4, 0, 0, 0],
            [2, 0, 0, 0],
            [3, 14, 0, 0],
            [2, 0, 7, 0]
        ],
        [
            [2, 0, 0, 0],
            [3, 0, 0, 0],
            [3, 8, 0, 0],
            [3, 0, 12, 0]
        ]
    ])
    blueprintScores = []

    for blueprint in blueprints[1:]:
        ressources = np.array([0, 0, 0, 0])
        robots = np.array([1, 0, 0, 0])

        for minute in range(24):
            print("------ minute " + str(minute + 1) + " ------")
            startRobots = robots.copy()
            for i, craft in enumerate(reversed(blueprint)):
                if canCraft(craft, ressources):
                    print("can craft " + str(3-i))
                    if shouldCraft(3-i, craft, ressources, blueprint, startRobots):
                        print("craft " + str(3-i) + " -" + str(craft))
                        ressources -= craft
                        robots[3-i] += 1
                        break

            print("get " + str(startRobots))
            ressources += startRobots
            print("robots = " + str(robots))
            print("ressources = " + str(ressources))

        blueprintScores.append(ressources[-1])
    print("SCORES: " + str(blueprintScores))


def canCraft(craft, ressources):
    for resource in (ressources - craft):
        if resource < 0:
            return False
    return True

def shouldCraft(i, craft, ressources, blueprint, startRobots):
    if(i == 3):
        return True
    elif(i == 0):
        return True
    else:
        stepLeft = np.ceil(max((blueprint[i + 1] - ressources) / startRobots))
        stepLeftIfCraft = np.ceil(max((blueprint[i + 1] + craft - ressources) / startRobots))
        print(str(stepLeft) + " " + str(stepLeftIfCraft))
        return stepLeftIfCraft <= stepLeft

firstHalf()