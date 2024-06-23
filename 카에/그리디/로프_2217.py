import sys
sys.stdin=open("input.txt", "r")

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

result = []

for i in range(n):
    result.append((i+1) * ropes[i])

print(max(result))