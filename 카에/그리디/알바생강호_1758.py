import sys
sys.stdin=open("input.txt", "r")

n = int(input())
customers = [int(input()) for _ in range(n)]
customers.sort(reverse=True)

tips = 0

for i in range(n):
    total = customers[i] - (i+1-1)
    if total > 0:
        tips += total

print(tips)