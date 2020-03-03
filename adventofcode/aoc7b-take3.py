import copy

def main():

    intCoder = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]  

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

    #create a separate "computer" for each amplifier
    computers = [intCoder[:], intCoder[:], intCoder[:], intCoder[:], intCoder[:]]


    #for each combination of possible inputs:
    for z in combos:
        e = 0
        
        #initialize the generators
        computerA = finder(computers[0])
        computerB = finder(computers[1])
        computerC = finder(computers[2])
        computerD = finder(computers[3])
        computerE = finder(computers[4])

        #travel to their first "input" point
        print("setup a")
        computerA.__next__()
        print("setup b")
        computerB.__next__()
        print("setup c")
        computerC.__next__()
        print("setup d")
        computerD.__next__()
        print("setup e")
        computerE.__next__()

        #pass their phase as their first input, as well as the first round of actual input
        print("phase a")
        computerA.send(z[0])
##        print("RUNNING COMPUTER A receiving", e)
##        a = computerA.send(e)

        print("phase b")
        computerB.send(z[1])
##        print("RUNNING COMPUTER B receiving", a)
##        b =  computerB.send(a)
            
        print("phase c")
        computerC.send(z[2])
##        print("RUNNING COMPUTER C receiving", b)
##        c = computerC.send(b)
        
        print("phase d")
        computerD.send(z[3])
##        print("RUNNING COMPUTER D receiving", c)
##        d = computerD.send(c)
        
        print("phase e")
        computerE.send(z[4])
##        print("RUNNING COMPUTER E receiving", d)
##        e = computerE.send(d)

        #start the computer
        print("starting loop...")
        while e != 99:
            print("RUNNING COMPUTER A with", e)
            a = computerA.send(e)  
            print("RUNNING COMPUTER B with", a)
            b = computerB.send(a)
            print("RUNNING COMPUTER C with", b)
            c = computerC.send(b)
            print("RUNNING COMPUTER D with", c)
            d = computerD.send(c)
            print("RUNNING COMPUTER E with", d)
            e = computerE.send(d)
            
        
        last = computerE.__next__()

        if last >= maxOutput:
            maxOutput = last

        print("the answer is ",maxOutput)
        


def finder(intCode):

    #declaring/clearing variables for the first time this is called
    x = 0
    modeOne = []
    prev = 0
    
    #keep going until we get a "halt" instruction
    while intCode[x] != 99:

        print(x, "is the index")

        print("code is now", intCode[x])

        modeOne.clear()

#Test to see if we're changing parameter modes
        if intCode[x] > 100:
            temp = str(intCode[x])
            for y in range(len(temp)-2):
                #tests the hundreds place to see if it's a '1', then the thousands
                if temp[len(temp)-3-y] == '1':
                    if (len(temp)-3-y) >= 0:
                        modeOne.append(True)
                    else:
                        break
                else:
                    modeOne.append(False)
            temp = int(temp[-1]) #grabs just the instruction w/o codes
            #checks for the leading 0 that is implied
            if temp <= 2 or temp >= 7:
                modeOne.append(False)
                if len(modeOne) <= 2:
                    modeOne.append(False)
        
        #Parameter modes are all default
        else:
            modeOne.append('STOP')
            temp = intCode[x]
    
            
#Logic for 3 Parameter Items
        if temp <= 2 or temp >= 7:
        
            if modeOne[0] != 'STOP':
                if modeOne[0] == True:
                    if modeOne[1] == True:
                        if modeOne[2] == True:
                            #TRUE, TRUE, TRUE
                            intCode[x+3] = compute3(temp, intCode[x+1], intCode[x+2])
                        else:
                            #TRUE, TRUE, FALSE
                            intCode[intCode[x+3]] = compute3(temp, intCode[x+1], intCode[x+2])
                    else:
                        if modeOne[2] == True:
                            #TRUE, FALSE, TRUE
                            intCode[x+3] = compute3(temp, intCode[x+1], intCode[intCode[x+2]])
                        else:
                            #TRUE, FALSE, FALSE
                            intCode[intCode[x+3]] = compute3(temp, intCode[x+1], intCode[intCode[x+2]])
                else:
                    if modeOne[1] == True:
                        if modeOne[2] == True:
                            #FALSE, TRUE, TRUE
                            intCode[x+3] = compute3(temp, intCode[intCode[x+1]], intCode[x+2])
                        else:
                            #FALSE, TRUE, FALSE
                            intCode[intCode[x+3]] = compute3(temp, intCode[intCode[x+1]], intCode[x+2])
                    else:
                        #FALSE, FALSE, TRUE
                        intCode[x+3] = compute3(temp, intCode[intCode[x+1]], intCode[intCode[x+2]])
            else:
                #FALSE, FALSE, FALSE
                intCode[intCode[x+3]] = compute3(temp, intCode[intCode[x+1]], intCode[intCode[x+2]])

            x += 4 #increments to the next instruction


## INPUT TO STORAGE
        elif temp == 3:
            print("yielding... at 3")
            number = yield "wait"
            print("received!", number)
            if modeOne[0] == 'STOP':
                intCode[intCode[x+1]] = number
            else:
                intCode[x+1] = number
            x+=2
            

## STORAGE TO OUTPUT
        elif temp == 4:
            if modeOne[0] != 'STOP':
                prev = intCode[x+1]
                print("sending", intCode[x+1])
                yield intCode[x+1]
            else:
                prev = intCode[intCode[x+1]]
                print("sending", intCode[intCode[x+1]])
                yield intCode[intCode[x+1]]
            print("picking back up with temp at",temp)
            x+=2

## JUMP IF TRUE OR FALSE   
        elif temp == 5 or temp == 6:
            if modeOne[0] != 'STOP':
                if modeOne[0] == True:
                    if intCode[x+1] != 0 and temp == 5:
                        if modeOne[1] == True:
                            #TRUE, TRUE
                            x = intCode[x+2]
                        else:
                            #TRUE, FALSE
                            x = intCode[intCode[x+2]]
                    elif intCode[x+1] == 0 and temp == 6:
                        if modeOne[1] == True:
                            #TRUE, TRUE
                            x = intCode[x+2]
                        else:
                            #TRUE, FALSE
                            x = intCode[intCode[x+2]]
                    else:
                        x+=3
                else:
                    if intCode[intCode[x+1]] != 0 and temp == 5:
                        if modeOne[1] == True:
                            #FALSE, TRUE
                            x = intCode[x+2]
                        else:
                            #FALSE, FALSE
                            x = intCode[intCode[x+2]]
                    elif  intCode[intCode[x+1]] == 0 and temp == 6:
                        if modeOne[1] == True:
                            #FALSE, TRUE
                            x = intCode[x+2]
                        else:
                            #FALSE, FALSE
                            x = intCode[intCode[x+2]]
                    else:
                        x+=3
            else:
                if intCode[intCode[x+1]] != 0 and temp == 5:
                    x = intCode[intCode[x+2]]
                elif intCode[intCode[x+1]] == 0 and temp == 6:
                    x = intCode[intCode[x+2]]
                else:
                    x+=3

        #If the code wasn't captured by the previous if and elif, something's wrong.
        else:
            print("Error! your input was not valid:", temp)

    print("it's over!")
    yield 99
    return prev
            


######INSTRUCTION LIST#########
def compute3(temp, insA, insB):

    #print("computing", temp, "with vars", insA, insB)
                    
    ## ADDITION
    if temp == 1:
        return (insA + insB)
               
    ## MULTIPLICATION
    elif temp == 2:
        return (insA * insB)

    ## IF LESS THAN
    elif temp == 7:
        if insA < insB:
            return 1
        else:
            return 0
        
    ## IF EQUAL TO
    elif temp == 8:
        if insA == insB:
            return 1
        else:
            return 0

main()


    
        
        
        
