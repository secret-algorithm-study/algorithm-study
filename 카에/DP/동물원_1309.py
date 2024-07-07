import sys
sys.stdin=open("input.txt", "r")

n = int(input())

dy = [0]*100001

dy[1] = 3
dy[2] = 7

for i in range(3, n+1):
    dy[i] = (dy[i-2] + (dy[i-1]*2))%9901

print(dy[n])