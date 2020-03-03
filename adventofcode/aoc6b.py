def main():

    #read the file and put lines in an array
    orbits = open("orbits.txt","r")
    orbits = orbits.read()
    orbits = orbits.split('\n')

##    orbits = ['COM)B00','B00)C00','C00)D00','D00)E00','E00)F00','B00)G00','G00)H00','D00)I00','I00)SAN','E00)J00','J00)K00','K00)L00','K00)YOU']

    #variables
    base = 'COM'
    orbitGraph = {}
    
    #start and end points that we need to find (one away from the actual ones)

    start = '6F7'
    end = 'WFF'

    

    for x in orbits:
        if x[4:] not in orbitGraph.keys():
            orbitGraph[x[4:]] = []
        orbitGraph[base] = [i[4:] if i[:3] == base else i[:3] if i[4:] == base else None for i in orbits if (i[:3] == base or i[4:] == base)]
        base = x[:3]

    ans = orbitRoute(orbitGraph,start,end)

    print (len(ans)-1)

def orbitRoute(orbitGraph, start, end, path=[]):

    path = path + [start]

    if start == end:
        return path

    if start not in orbitGraph.keys():
        return None
    
    for node in orbitGraph[start]:
        if node not in path and node != None:
            newpath = orbitRoute(orbitGraph, node, end, path)

            if newpath:
                return newpath
            
    return None
    

main()
