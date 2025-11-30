import re

def parseData():
    with open('2023/2/input.txt', 'r') as f:
        games = []
        for match in re.finditer(r"Game (\d+): (.*)", f.read()):
            subsets = []
            (id, data) = match.groups()
            for subset in data.split("; "):
                cubes = {
                    "red": 0,
                    "green": 0,
                    "blue": 0
                }
                for cube in subset.split(", "):
                    (quantity, color) = cube.split(' ')
                    match(color):
                        case "red":
                            cubes["red"] = int(quantity)
                        case "green":
                            cubes["green"] = int(quantity)
                        case "blue":
                            cubes["blue"] = int(quantity)
                subsets.append(cubes)
            games.append(subsets)
    return games

maxCubes = {
    "red": 12,
    "green": 13,
    "blue": 14 
}

def firstHalf():    
    games = parseData()
    indexSum = 0
    for i, game in enumerate(games):
        for cubes in game:
            if cubes["red"] > maxCubes["red"] or cubes["green"] > maxCubes["green"] or cubes["blue"] > maxCubes["blue"]:
                break
        else:
            indexSum += (i + 1)
    print(indexSum)

def secondHalf():    
    games = parseData()
    powerSum = 0
    for game in games:
        powerSum += max(cubes["red"] for cubes in game) * max(cubes["green"] for cubes in game) * max(cubes["blue"] for cubes in game)

    print(powerSum)

secondHalf()