def main():

    intCode = [3,225,1,225,6,6,1100,1,238,225,104,0,1,191,196,224,1001,224,-85,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,45,50,225,1102,61,82,225,101,44,39,224,101,-105,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,102,14,187,224,101,-784,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1001,184,31,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,91,18,225,2,35,110,224,101,-810,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,76,71,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,7,16,225,1102,71,76,224,101,-5396,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,72,87,225,1101,56,77,225,1102,70,31,225,1102,29,15,225,1002,158,14,224,1001,224,-224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,494,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

    x = 0
    modeOne = []
    par = 0
    ans = 0
    
    while intCode[x] != 99:
        print("starting code",intCode[x])

        ans = 0
        modeOne.clear()
        modeOne.append('STOP')

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
            if intCode[x] <= 2:
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
                    print("run once with j = ",j)
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
            result = input("please enter input")
            intCode[intCode[x+1]] = result
            x+=2

        elif intCode[x] == 4:
            if modeOne[0] != 'STOP':
                #print("grabbing from position",x+1)
                print(intCode[x+1])
                if intCode[x+1] != 0:
                    break
            else:
                #print("grabbing from position",intCode[x+1])
                print(intCode[intCode[x+1]])
                if intCode[intCode[x+1]] != 0:
                    break
            x+=2

        else:
            print("STOP")
            break


    #print (intCode)

main()
    

