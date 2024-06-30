import sys
sys.stdin=open("input.txt", "r")

n = int(input())
dy = [0, 1]

for i in range(2, n+1):
    dy.append(dy[i-1] + dy[i-2])

print(dy[n])