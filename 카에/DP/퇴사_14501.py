import sys
sys.stdin=open("input.txt", "r")

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
dy = [0]*1001

for i in range(n):
    for j in range(i+schedule[i][0], n+1):
        if dy[j] < dy[i]+schedule[i][1]:
            dy[j] =  dy[i]+schedule[i][1]

print(dy[n])