import sys
sys.stdin=open("input.txt", "r")

n ,k = map(int, input().split())
temperatures = list(map(int, input().split()))

total = sum(temperatures[:k])
max_total = total

for i in range(k, n):
    total -= temperatures[i-k]
    total += temperatures[i]

    max_total = max(total, max_total)

print(max_total)