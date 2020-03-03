import copy
import threading
import time

def main():

    intCoder = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]  

    digits = [5, 6, 7, 8, 9]
    combos = []
    maxOutput = 0

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
    
    #print(combos)

    for z in combos:
        
        ampInput = 0
        start = [0, 0, 0, 0, 0]
        last = 0
        ic1 = intCoder.copy()
        ic2 = intCoder.copy()
        ic3 = intCoder.copy()
        ic4 = intCoder.copy()
        ic5 = intCoder.copy()
        intCodes = [ic1, ic2, ic3, ic4, ic5]

        #initialize the amps
        for b in z:
            o = finder(intCodes[z.index(b)], b, z.index(b), start)

        #find the answer through all the iterations
        while ampInput != 99:
            
            for phaser in z:
                print("phaser:", phaser, "input:", ampInput, "index:", z.index(phaser), start)
                last = ampInput
                ampInput = finder(intCodes[z.index(phaser)], ampInput, z.index(phaser), start)

                if ampInput == 99:
                    print(last)
                    break
                
                    

        if last >= maxOutput:
            maxOutput = last

        print("the answer is",maxOutput)

        intCodes.clear()

            
    print("answer is", maxOutput)


def finder(intCode, number, iden, start):

    
    x = start[iden]
    modeOne = []
    par = 0
    ans = 0
    val = False
    rtn = 0

    #print("starting position is",x)
    
    while intCode[x] != 99:
        

        ans = 0
        modeOne.clear()
        modeOne.append('STOP')

        print("input is", intCode[x])

        
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

            #print(modeOne)
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
                intCode[intCode[x+3]] = intCode[intCode[x+1]] + intCode[intCode[x+2]]
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
                intCode[intCode[x+3]] = intCode[intCode[x+1]] * intCode[intCode[x+2]]
            x+=4
            
        #storage instructions
        elif intCode[x] == 3: 
##            if first == True:
##                #print(phaser,"sent to...")
##                first = 'no'
##            elif first == 'no':
##                start[iden] = x+2
####            elif first == False:
####                #print(second,"sent to...")
####                result = second
####                first = True
            if modeOne[0] == 'STOP':
                intCode[intCode[x+1]] = number
            else:
                intCode[x+1] = number
                
            x+=2

        #retrieval instructions
        elif intCode[x] == 4:
            if modeOne[0] != 'STOP':
                #print("grabbing from position",x+1)
                start[iden] = x+2
                return intCode[x+1]
##                if intCode[x+1] != 0:
##                    break
            else:
                #print("grabbing from position",intCode[x+1])
                start[iden] = x+2
                return intCode[intCode[x+1]]
##                if intCode[intCode[x+1]] != 0:
##                    break

        #"jump if true"
        elif intCode[x] == 5:
            if modeOne[0] != 'STOP':
                #print ("modechange")
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
            
            

    return 99


    #print (intCode)

main()
    


