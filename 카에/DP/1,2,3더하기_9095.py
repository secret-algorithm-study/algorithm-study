import sys
sys.stdin=open("input.txt", "r")

t = int(input())

for _ in range(t):
    n = int(input())
    dy = [0]*11
    dy[1] = 1
    dy[2] = 2
    dy[3] = 4

    for i in range(4, n+1):
        dy[i] = dy[i-1] + dy[i-2] + dy[i-3]
    
    print(dy[n])