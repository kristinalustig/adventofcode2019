def main():

    total = 0

    modules = open('modules.txt', 'r')

    modules = modules.read()

    modules = modules.split('\n')

    for x in modules:
        total += massCalc(x)

    print (total)
    

def massCalc(x):
    
    #print("mass is ", x)
    x = int(x)

    fuel = int(x/3)-2

    if fuel > 0:
        fuel += massCalc(fuel)
    else:
        return 0

    return fuel

main()

