def Guvi(number):
    if(number%2==0):
        return "even"
    else:
        return "odd"

<<<<<<< HEAD
#print(Guvi(4))

def stepsToCollatzConjenture(collatzlist):
    return len(collatzlist)

def Collatz_Conjenture(number):
    '''A Python Function for Collatz Conjenture also known by 3n+1 Problem'''
    result = [number]
    while(number > 1):
        if(number % 2):
            number = (3*number)+1
            result.append(number)
        else:
            number = number//2
            result.append(number)
       
    return result




=======
print(Guvi(4))
>>>>>>> 1d04ef881cc3c7deadde5ad64953644901c802a0
