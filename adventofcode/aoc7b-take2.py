import copy
import asyncio
import time

def main():

    intCoder = [3,8,1001,8,10,8,105,1,0,0,21,38,55,64,89,114,195,276,357,438,99999,3,9,101,3,9,9,102,3,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,101,5,9,9,4,9,99,3,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,5,9,101,5,9,9,102,3,9,9,4,9,99,3,9,101,3,9,9,1002,9,4,9,101,5,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99]  

    digits = [5, 6, 7, 8, 9]
    combos = []
    maxOutput = 0
    e = 0

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

        cont = True
        
        outputA = finder(intCoder[:], z[0])
        outputA.__next__()

        print("change")
        
        outputB = finder(intCoder[:], z[1])
        outputB.__next__()

        print("change")
        
        outputC = finder(intCoder[:], z[2])
        outputC.__next__()

        print("change")
        
        outputD = finder(intCoder[:], z[3])
        outputD.__next__()

        print("change")
        
        outputE = finder(intCoder[:], z[4])
        outputE.__next__()

                                                   

##        a = outputA.send(z[0])
##        #outputA.__next__()
##        print("did a", a)
##        b = outputB.send(z[1])
##        #outputB.__next__()
##        print("did b", b)
##        c = outputC.send(z[2])
##        #outputC.__next__()
##        print("did c", c)
##        d = outputD.send(z[3])
##        #outputD.__next__()
##        print("did d", d)
##        e = outputE.send(z[4])
##        #outputE.__next__()
##        print("did e", e)
##
        while cont == True:
            a = outputA.send(e)
            outputA.__next__()
            print("returned",a)
            b = outputB.send(a)
            outputB.__next__()
            print("returned",b)
            c = outputC.send(b)
            outputC.__next__()
            print("returned",c)
            d = outputD.send(c)
            outputD.__next__()
            print("returned",d)
            e = outputE.send(d)
            outputE.__next__()
            print("returned",e)

        
        if last >= maxOutput:
            maxOutput = last

        print("the answer is",maxOutput)

            
    print("answer is", maxOutput)


def finder(intCode, number):

    print(id(intCode))

    
    x = 0
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

        if intCode[x] == 3:
            number = yield
            print(number)
        
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
            temp = int(temp[-1])
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
                number = yield intCode[x+1]
                x += 2
##                if intCode[x+1] != 0:
##                    break
            else:
                number = yield intCode[intCode[x+1]]
                x += 2
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

        else:
            print("ERROR! this gives you", intCode[x])

        
            
            

    return 99


    #print (intCode)

main()
    


