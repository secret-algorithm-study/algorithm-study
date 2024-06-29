import sys
sys.stdin=open("input.txt", "r")

n = int(input())
stairs = [0]*301

for i in range(1, n+1):
    stairs[i] = int(input())

dy = [0]*301
dy[1] = stairs[1]
dy[2] = stairs[1] + stairs[2]
dy[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

for i in range(4, n+1):
    dy[i] = max(dy[i-3]+stairs[i-1]+stairs[i], dy[i-2]+stairs[i])

print(dy[n])