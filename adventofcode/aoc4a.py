passCount = 0
num = '158126'
numList = []
adjStart = False
adjEnd = False
increase = True

while num != '624574':
    for x in range(len(num)):
        numList.append(num[x])

    
    for x in range(len(numList)-1):
        if numList[x] == numList[x+1]:
            try:
                if (numList[x-1] != numList[x]):
                    adjStart = True
                    try:
                        if (numList[x+1] != numList[x+2]):
                            adjEnd = True
                            break
                    except IndexError:
                        adjEnd = True
                        #print ("passed on error with",num)
                        break
                else:
                    adjStart = False
            except IndexError:
                #print("start error with ",num)
                pass
            try:
                if (numList[x+1] != numList[x+2]):
                    adjEnd = True
                    if (numList[x-1] != numList[x]):
                        adjStart = True
                        break
                else:
                    adjEnd = False
            except IndexError:
                #print("end error with ",num)
                pass
    for x in range(len(numList)-1):
        if numList[x+1] < numList[x]:
            #print("failed inc")
            increase = False
            break
        
        

    if ((adjStart == True) and (adjEnd == True)) and (increase == True):
        passCount += 1
        #print ("found one!", num)
    

    num = int(num)
    num += 1
    num = str(num)
    adjStart = False
    adjEnd = False
    increase = True
    numList.clear()

print(passCount)


    #are there two adjacent digits?


    #do the digits only increase?
        
    
    
    

