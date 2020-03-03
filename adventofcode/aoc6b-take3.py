def main():

    #read the file and put lines in an array
##    orbits = open("orbits.txt","r")
##    orbits = orbits.read()
##    orbits = orbits.split('\n')

    orbits = ['COM)B00','B00)C00','C00)D00','D00)E00','E00)F00','B00)G00','G00)H00','D00)I00','I00)SAN','E00)J00','J00)K00','K00)L00','K00)YOU']

    #variables
    ordered = []
    com = 'COM'
    orbitCount = 0
    orbitStore = []
    total = 0
    orbitDetail = []
    branchStart = []

    orbitNum = orbitCounter(com, orbits, orbitCount, orbitStore, orbitDetail, branchStart)
    
    #start and end points that we need to find
    goals = ['SAN','YOU']

    #format here is '1AAA BBB' where 1 is the orbit count, aaa is the previous, and b is the next
    #print (orbitDetail)
    print(branchStart)

    #this counts the steps
    stepCount = stepCounter(goals, orbitDetail, branchStart)
    print (stepCount)

    #test to make sure we're still assessing the numbers correctly
##    for x in orbitNum:
##        try:
##            total += x
##        except TypeError:
##            pass

    #print (total)

    #print (branchStart)
            

    #count the elements before an item in the branch
    #and then count the first items in each list that follows


def orbitCounter(base, orbits, orbitCount, orbitStore, orbitDetail, branchStart):
 
    found = False

    for x in orbits:
        if x[:3] == base:
            if found == False:
                orbitCount += 1
                found = True

            else:
                
                branchStart.append(x[:3])
                print(x[:3])

            orbitStore.append(orbitCount)
            toAppend = [str(orbitCount-1),str(x[:3]),str(x[4:])]
            orbitDetail.append(toAppend)
            #print("going into recursion w ",x[4:]," and orbitCount ",orbitCount)
            orbitStore.append(orbitCounter(x[4:], orbits, orbitCount, orbitStore, orbitDetail, branchStart))
            #print("leaving with ",orbitStore)

    if found == False:
        
        return 0

    else:
        return orbitStore



def stepCounter(goals, orbitDetail, branchStart):

    stepCount = 0 #number of steps between the start and end
    branchFound = False #did we locate a branch
    searchBranch = 0 #what branch are we gonna search
    elim = [] #what branches are we eliminating from exploration
    startnum = 0
    interim = 0 #interim count as we explore a branch
    stepsFound = False
    loc = 0


    for x in range(len(orbitDetail)-1):
        if (orbitDetail[x][2] in goals):
            print(orbitDetail[x][2])
            goals.remove(orbitDetail[x][2])
            toFind = orbitDetail[x][1]
            break

    while stepsFound == False:

        while branchFound == False:

            

            for j in orbitDetail:

                print("looking for",toFind)
                
                if toFind == j[2]:
                    print("found ",j[2], "seeking", j[1])
                    toFind = j[1]
                    stepCount += 1
                    break
                
            if j[1] in branchStart:
                print ("found a branch")
                branchFound = True
                searchBranch = j[1]
                loc = int(orbitDetail.index(j))
                print(j)
                elim.append(j[2])
                break
                
                    
                
            
        startnum = int(orbitDetail[loc][0])
        g = 1

        print(orbitDetail[loc][2])

        
        try:
            while int(orbitDetail[loc+g][0]) >= (int(startnum) + int(g)):
                print (orbitDetail[loc+g][2])
                if orbitDetail[loc+g][2] in goals:
                    print(orbitDetail[loc+g][2])
                    stepsFound == True
                    print(stepCount, interim)
                    stepCount += interim
                    return stepCount
                else:
                    print("iterate")
                    interim += 1
                    g += 1
        except IndexError:
            print("failed")
            pass

        elim.append(orbitDetail[loc][2])

        branchFound = False
        stepCount = 0
        interim = 0
        print("remove",searchBranch)
        branchStart.remove(searchBranch)
        searchBranch = 0  
                        
    

main()
