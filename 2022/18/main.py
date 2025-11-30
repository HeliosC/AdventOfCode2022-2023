import sys
input = open('2022/18/input.txt', 'r')

def parseData():
    cubes = []
    for cube in input.readlines():
        (x, y, z) = [int(coord) for coord in cube.replace('\n', "").split(',')]
        cubes.append((x, y, z))
    return cubes

def firstPart():
    faces = set()
    cubes = parseData()
    for (x, y, z) in cubes:
        checkFace(faces, (x - 1/2, y - 1/2, z))
        checkFace(faces, (x - 1/2, y - 1/2, z - 1))

        checkFace(faces, (x - 1/2, y, z - 1/2))
        checkFace(faces, (x - 1/2, y - 1, z - 1/2))

        checkFace(faces, (x, y - 1/2, z - 1/2))
        checkFace(faces, (x - 1, y - 1/2, z - 1/2))

    print(len(faces))
    return cubes, faces

    checkFace(faces, (2 * x - 1, 2 * y - 1, 2 * z))
    checkFace(faces, (2 * x - 1, 2 * y - 1, 2 * z - 2))

    checkFace(faces, (2 * x - 1, 2 * y, 2 * z - 1))
    checkFace(faces, (2 * x - 1, 2 * y - 2, 2 * z - 1))

    checkFace(faces, (2 * x, 2 * y - 1, 2 * z - 1))
    checkFace(faces, (2 * x - 2, 2 * y - 1, 2 * z - 1))


faces = set()
groups = []
def secondPart():
    #global faces, groups
    cubes, faces = firstPart()
    #cubes = [(x * 2, y * 2, z * 2) for (x, y, z) in cubes]
    #print("faces", faces)
    #print("cubes", cubes)

    xmin, ymin, zmin, xmax, ymax, zmax = sys.maxsize, sys.maxsize, sys.maxsize, 0, 0, 0
    for (x, y, z) in cubes:
        if x < xmin:
            xmin = x
        if y < ymin:
            ymin = y
        if z < zmin:
            zmin = z
        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y
        if z > zmax:
            zmax = z

    print("min", xmin, ymin, zmin)
    print("max", xmax, ymax, zmax)

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                yf, zf = y - 1/2, z - 1/2
                xfaces = [[], []]
                for xf in range(xmin - 1, xmax + 1):
                    face = (xf, yf, zf)
                    if face in faces:
                        if xf < x:
                            if face not in xfaces[0]:
                                xfaces[0].append(face)
                        else:
                            if face not in xfaces[1]:
                                xfaces[1].append(face)
                if False and xfaces[0] and len(xfaces[0]) % 2 == 0 and xfaces[1] and len(xfaces[1]) % 2 == 0:
                    print("x", x, y, z)
                    print(xfaces)
                    faces.discard(xfaces[0][-1])
                    faces.discard(xfaces[1][0])

                #print(len(faces))

                xf, zf = x - 1/2, z - 1/2
                yfaces = [[], []]
                for yf in range(ymin - 1, ymax + 1):
                    face = (xf, yf, zf)
                    if face in faces:
                        if yf < y:
                            if face not in yfaces[0]:
                                yfaces[0].append(face)
                        else:
                            if face not in yfaces[1]:
                                yfaces[1].append(face)
                if False and yfaces[0] and len(yfaces[0]) % 2 == 0 and yfaces[1] and len(yfaces[1]) % 2 == 0:
                    print("y", x, y, z)
                    print(yfaces)
                    faces.discard(yfaces[0][-1])
                    faces.discard(yfaces[1][0])

                #print(len(faces))

                #continue
                xf, yf = x - 1/2, y - 1/2
                zfaces = [[], []]
                for zf in range(zmin - 1, zmax + 1):
                    face = (xf, yf, zf)
                    if face in faces:
                        if zf < z:
                            if face not in zfaces[0]:
                                zfaces[0].append(face)
                        else:
                            if face not in zfaces[1]:
                                zfaces[1].append(face)
                if False and zfaces[0] and len(zfaces[0]) % 2 == 0 and zfaces[1] and len(zfaces[1]) % 2 == 0:
                    print("z", x, y, z)
                    print(zfaces)
                    faces.discard(zfaces[0][-1])
                    faces.discard(zfaces[1][0])
                
                if xfaces[0] and len(xfaces[0]) % 2 == 0 and xfaces[1] and len(xfaces[1]) % 2 == 0 and yfaces[0] and len(yfaces[0]) % 2 == 0 and yfaces[1] and len(yfaces[1]) % 2 == 0 and zfaces[0] and len(zfaces[0]) % 2 == 0 and zfaces[1] and len(zfaces[1]) % 2 == 0:
                    print(x, y, z)
                    faces.discard(xfaces[0][-1])
                    faces.discard(xfaces[1][0])
                    faces.discard(yfaces[0][-1])
                    faces.discard(yfaces[1][0])                    
                    faces.discard(zfaces[0][-1])
                    faces.discard(zfaces[1][0])
    print(len(faces))
    return
    while faces:
        #print("while")
        face = faces.pop()
        groups.append([face])
        checkEdges(face)
        #break

    
    for group in groups:
        print("------------------")
        print(group)
        print(len(group))

    print("------------------")
    print(len(groups))


def checkEdges(face):
    global faces, groups
    #print("checkEdges face", face)

    #faces.discard(face)

    (x, y ,z) = face

    #if face not in faces:
    #    return

    edges = {}
    if x % 2 == 0:
        edges = { 
            (x - 1, y - 1, z), (x - 1, y + 1, z), (x - 1, y, z - 1), (x - 1, y, z + 1), 
            (x + 1, y - 1, z), (x + 1, y + 1, z), (x + 1, y, z - 1), (x + 1, y, z + 1), 
        }
    elif y % 2 == 0:
        edges = { 
            (x - 1, y - 1, z), (x + 1, y - 1, z), (x, y - 1, z - 1), (x, y - 1, z + 1), 
            (x - 1, y + 1, z), (x + 1, y + 1, z), (x, y + 1, z - 1), (x, y + 1, z + 1), 
        }
    elif z % 2 == 0:
        edges = { 
            (x - 1, y, z - 1), (x + 1, y, z - 1), (x, y - 1, z - 1), (x, y + 1, z - 1), 
            (x - 1, y, z + 1), (x + 1, y, z + 1), (x, y - 1, z + 1), (x, y + 1, z + 1), 
        }
    else:
        print("OHHHHHHHH")


    edgeInGroups = -1
    for i, group in enumerate(groups):
        if face in group:
            edgeInGroups = i
            break
    else:
        edgeInGroups = len(groups)
        groups.append([face])


    #print("EDGESSSS", edges)
    for edge in edges:
        if edge in faces:

                


            #print("EDGE", edge, edgeInGroups)
            faces.discard(edge)
            if edge not in groups[edgeInGroups]:
                groups[edgeInGroups].append(edge)
            checkEdges(edge)

    #faces.discard(face)

def checkFace(faces, face):
    if face in faces:
        faces.remove(face)
    else:
        faces.add(face)

secondPart()