def main():

    #read the file and put lines in an array
    orbits = open("orbits.txt","r")
    orbits = orbits.read()
    orbits = orbits.split('\n')

    #orbits = ['COM)B00','B00)C00','C00)D00','D00)E00','E00)F00','B00)G00','G00)H00','D00)I00','E00)J00','J00)K00','K00)L00']

    #variables
    ordered = []
    com = 'COM'
    orbitCount = 0
    orbitStore = []
    total = 0

    orbitNum = orbitCounter(com, orbits, orbitCount, orbitStore)

    for x in orbitNum:
        try:
            total += x
        except:
            pass

    print (total)
            

    #if nothing is orbiting a given item, its chain is a branch


    #count the elements before an item in the branch
    #and then count the first items in each list that follows


def orbitCounter(base, orbits, orbitCount, orbitStore):
 
    found = False

    for x in orbits:
        if x[:3] == base:
            if found == False:
                orbitCount += 1
                found = True
                #print(x)

            orbitStore.append(orbitCount)
            #print("going into recursion w ",x[4:]," and orbitCount ",orbitCount)
            orbitStore.append(orbitCounter(x[4:], orbits, orbitCount, orbitStore))
            #print("leaving with ",orbitStore)

    if found == False:
        return 0

    else:
        return orbitStore
                        
    

main()
