import sys


sys.stdin=open("input.txt", "r")


import math
n = int(input());

dp = [0] * (n+1);



def isSquare(n):
    return int(math.sqrt(n)) ** 2 == n


for i in range(1,n+1):
    if(isSquare(i)):
        dp[i] = 1;
    
    


for i in range(1, n+1):
    if(dp[i] == 0):
        list = [];
        for j in range(1 , int(i**(1/2))+1):
            if(j**2 <= i):
                list.append(dp[i-j**2]);
        dp[i] = min(list) + 1;
           
    

print(dp[n])