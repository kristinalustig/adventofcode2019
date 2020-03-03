
def main():

    intCode = [3,8,1001,8,10,8,105,1,0,0,21,38,55,64,89,114,195,276,357,438,99999,3,9,101,3,9,9,102,3,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,101,5,9,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,5,9,101,5,9,9,102,3,9,9,4,9,99,3,9,101,3,9,9,1002,9,4,9,101,5,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99]  

    digits = [0, 1, 2, 3, 4]
    combos = []
    maxOutput = 0
    phase = 0
    second = 0

    for u in digits:
        for v in digits:
            for w in digits:  
                for x in digits:        
                    for y in digits:
                        if u not in [v, w, x, y]:
                            if v not in [u, w, x, y]:
                                if x not in [u, v, w, y]:
                                    if y not in [u, v, w, x]:
                                        combos.append([u, v, w, x, y])
    
    print(combos)
    

    for z in combos:
        for a in z:
            second = finder(intCode, a, second)
        if second > maxOutput:
            maxOutput = second
        print(maxOutput)
        maxOutput = 0
        second = 0

    print(maxOutput)
        

    
                
    


def finder(intCode, phaser, second):



    x = 0
    modeOne = []
    par = 0
    ans = 0
    val = False
    rtn = 0
    first = True
    
    while intCode[x] != 99:
        #print("starting code",intCode[x])

        ans = 0
        modeOne.clear()
        modeOne.append('STOP')

        print("input is",x)

        
        #Test to see if we're using parameter modes
        if intCode[x] > 100:
            modeOne.clear()
            #look at the numbers after the first two numbers (R to L)
            temp = str(intCode[x])
            for y in range(len(temp)-1):
                #print("loop starts at ",y)
                #print(temp[len(temp)-1-y])
                if temp[len(temp)-3-y] == '1':
                    if (len(temp)-3-y) >= 0:
                        modeOne.append(True)
                    else:
                        break
                else:
                    modeOne.append(False)
            #if it's only gone through two iterations, add the trailing 0
            intCode[x] = int(temp[-1])
            if (intCode[x] <= 2) or (intCode[x] >= 7):
                #print("emergency addition")
                modeOne.append(False)
                if len(modeOne) <= 2:
                    modeOne.append(False)

            print(modeOne)
            #print(intCode[x])
                
        #for addition instructions
        if intCode[x] == 1:
            if modeOne[0] != 'STOP':
                for j in range (0, 2):
                    #print("run once with j = ",j)
                    if modeOne[j] == True:
                        ans += intCode[x+1+j]
                        #print("true")
                    else:
                        #print("false")
                        ans += intCode[intCode[x+1+j]]
##                if modeOne[2] == True:
##                    intCode[x+3] = ans
##                else:
##                    intCode[intCode[x+3]] = ans
                intCode[intCode[x+3]] = ans
            else:
                intCode[intCode[x+3]] = int(intCode[intCode[x+1]]) + int(intCode[intCode[x+2]])
            x+=4

        #for multiplication instructions
        elif intCode[x] == 2:
            ans = 1
            if modeOne[0] != 'STOP':
                for j in range (0, 2):
                    if modeOne[j] == True:
                        ans = ans * intCode[x+1+j]
                    else:
                        ans = ans * intCode[intCode[x+1+j]]
                intCode[intCode[x+3]] = ans
            else:
                intCode[intCode[x+3]] = int(intCode[intCode[x+1]]) * int(intCode[intCode[x+2]])
            x+=4
            
        #storage instructions
        elif intCode[x] == 3:
            if first == True:
                result = phaser
            else:
                result = second
                first = True
            intCode[intCode[x+1]] = result
            x+=2

        #retrieval instructions
        elif intCode[x] == 4:
            if modeOne[0] != 'STOP':
                #print("grabbing from position",x+1)
                return intCode[x+1]
                if intCode[x+1] != 0:
                    break
            else:
                #print("grabbing from position",intCode[x+1])
                return intCode[intCode[x+1]]
                if intCode[intCode[x+1]] != 0:
                    break
            x+=2

        #"jump if true"
        elif intCode[x] == 5:
            if modeOne[0] != 'STOP':
                if modeOne[0] == True:
                    if intCode[x+1] != 0:
                        if modeOne[1] == True:
                            x = intCode[x+2]
                        else:
                            x = intCode[intCode[x+2]]
                    else:
                        x += 3
                else:
                    if intCode[intCode[x+1]] != 0:
                        if modeOne[1] == True:
                            x = intCode[x+2]
                        else:
                            x = intCode[intCode[x+2]]
                    else:
                        x += 3
            else:
                if intCode[intCode[x+1]] != 0:
                    x = intCode[intCode[x+2]]
                else:
                    x += 3
                        
                        
        #"jump if false"
        elif intCode[x] == 6:
            if modeOne[0] != 'STOP':
                if modeOne[0] == True:
                    if intCode[x+1] == 0:
                        if modeOne[1] == True:
                            x = intCode[x+2]
                        else:
                            x = intCode[intCode[x+2]]
                    else:
                        x += 3
                else:
                    if intCode[intCode[x+1]] == 0:
                        if modeOne[1] == True:
                            x = intCode[x+2]
                        else:
                            x = intCode[intCode[x+2]]
                    else:
                        x += 3
            else:
                if intCode[intCode[x+1]] == 0:
                    x = intCode[intCode[x+2]]
                else:
                    x += 3    
            
        #checks for less than
        elif intCode[x] == 7:

            #grabbing the correct positions
            if modeOne[0] != 'STOP':

                if modeOne[0] == True:
                    para1 = intCode[x+1]
                else:
                    para1 = intCode[intCode[x+1]]
                if modeOne[1] == True:
                    para2 = intCode[x+2]
                else:
                    para2 = intCode[intCode[x+2]]

            else:
                para1 = intCode[intCode[x+1]]
                para2 = intCode[intCode[x+2]]


            #grabbing the correct value to place
            if para1 < para2:
                rtn = 1
            else:
                rtn = 0

            
            #placing the value in the correct place
            if modeOne[0] != 'STOP':
                if modeOne[2] == True:
                    intCode[x+3] = rtn
                else:
                    intCode[intCode[x+3]] = rtn
            else:
                intCode[intCode[x+3]] = rtn
        
            x += 4
            
        #Checks for equality
        elif intCode[x] == 8:

            #grabbing the correct positions
            if modeOne[0] != 'STOP':

                if modeOne[0] == True:
                    para1 = intCode[x+1]
                else:
                    para1 = intCode[intCode[x+1]]
                if modeOne[1] == True:
                    para2 = intCode[x+2]
                else:
                    para2 = intCode[intCode[x+2]]

            else:
                para1 = intCode[intCode[x+1]]
                para2 = intCode[intCode[x+2]]


            #grabbing the correct value to place
            if para1 == para2:
                rtn = 1
            else:
                rtn = 0

            
            #placing the value in the correct place
            if modeOne[0] != 'STOP':
                if modeOne[2] == True:
                    intCode[x+3] = rtn
                else:
                    intCode[intCode[x+3]] = rtn
            else:
                intCode[intCode[x+3]] = rtn
        
            x += 4
            
            

        else:
            print("STOP")
            break


    #print (intCode)

main()
    


