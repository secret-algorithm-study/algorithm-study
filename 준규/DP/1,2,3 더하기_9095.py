import sys
sys.stdin=open("input.txt", "r")


loopCount = int(input());



def calculation(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 2
    elif(n == 3):
        return 4
    else:
        return calculation(n-1) + calculation(n-2) + calculation(n-3)


for i in range(loopCount):
    n = int(input())
    print(calculation(n))

    
        
