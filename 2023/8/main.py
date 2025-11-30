import re

def parseData():
    with open('2023/8/input.txt', 'r') as f:
        sequence = f.readline().replace("\n", "")
        f.readline()
        graph = {}
        for match in re.finditer(r"(.{3}) = \((.{3}), (.{3})\)", f.read()):
            (node, l, r) = match.groups()
            graph[node] = {'L' : l, 'R': r}

    return (sequence, graph)

def firstHalf():
    pathLen = 0
    (sequence, graph) = parseData()
    node = "AAA"
    while True:
        for step in sequence:
            node = graph[node][step]
            pathLen += 1
            if(node == "ZZZ"):
                print(pathLen)
                return

def secondHalf():
    pathLen = 0
    (sequence, graph) = parseData()
    nodes = list(filter(lambda key: key[-1] == 'A', graph.keys()))
    nodes = ["CDA"]

    while True:
        for step in sequence:
            newNodes = []
            for node in nodes:
                newNodes.append(graph[node][step])
            pathLen += 1
            nodes = newNodes
            if nodes[0][-1] == 'Z':
                print(nodes[0], pathLen)
            #if all(node[-1] == 'Z' for node in nodes):
            #    print(pathLen)
            #    return
            
# MSA -> XHZ : 14893
# AAA -> ZZZ : 20513
# PKA -> FHZ : 22199
# NBA -> LSZ : 19951
# RHA -> RQZ : 17141
# CDA -> LXZ : 12083

secondHalf()