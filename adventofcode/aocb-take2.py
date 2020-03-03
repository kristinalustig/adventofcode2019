def main():
    

    #full dataset
##    orbits = open("orbits.txt","r")
##    orbits = orbits.read()
##    orbits = orbits.split('\n')


    #practice data set - answer should be 4
    orbits = ['COM)B00','B00)C00','C00)D00','D00)E00','E00)F00','B00)G00','G00)H00','D00)I00','I00)SAN','E00)J00','J00)K00','K00)L00','K00)YOU']

    #variables
    base = 'COM'
    orbitCount = 0
    orbitDetail = []
    orbitStore = []
    answer = []
    branchStart = []
    goals = ['SAN','YOU']
    searchBranch = 0

    orbitNum = orbitCounter(base, orbits, orbitCount, orbitStore, orbitDetail, branchStart)

    print(orbitDetail)
    print(branchStart)

    for x in orbitDetail:
        if x[2] in goals:
            print(orbitDetail.index(x))
            answer.append(chainTravel(orbitDetail.index(x), branchStart, orbitDetail))

    print(answer)
            
            


    #broken down methods
    
#this method takes in raw data and returns semi-ordered lists of branches with connections in arrays
def orbitCounter(base, orbits, orbitCount, orbitStore, orbitDetail, branchStart):

    found = False

    for x in orbits:
        if x[:3] == base:
            #if you've already found one, then you've found yourself a BRANCH
            if found == False:
                orbitCount += 1
                found = True
            else:
                #append the entire branch name to show which direction it's going
                branchStart.append(x[:3])

            #add to the count and then add to the array we'll use later
            orbitStore.append(orbitCount)
            orbitDetail.append([orbitCount-1, x[:3], x[4:]])

            #recursively search down the branch paths to add items
            orbitStore.append(orbitCounter(x[4:], orbits, orbitCount, orbitStore, orbitDetail, branchStart))

    #if we haven't found another thing orbiting something, then that's the end of the branch!
    if found == False:
        return 0
    else:
        return orbitStore

#this method chains backwards through the objects to the closest branch
def chainTravel(start, branchStart, orbitDetail):

    stepCount = 0
    branchFound = False
    toFind = orbitDetail[start][1]
    print(toFind, "searching")

    while branchFound == False:
        for j in orbitDetail:
            if toFind == j[2]:
                toFind = j[1]
                stepCount += 1
            elif toFind in branchStart:
                stepCount += 1
                print(j)
                return [stepCount, j[0]]
                
    
    

main()
        
            
    
