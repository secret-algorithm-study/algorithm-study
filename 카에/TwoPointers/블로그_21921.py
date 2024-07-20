import sys
sys.stdin=open("input.txt", "r")

n, x = map(int, input().split())
visiters = list(map(int, input().split()))

total = 0
cnt = 1
max_visiters = 0 

for i in range(x):
    total += visiters[i]

max_visiters = total

for i in range(x, n):
    total -= visiters[i-x]
    total += visiters[i]

    if total > max_visiters:
        max_visiters = total
        cnt = 1
    elif total == max_visiters:
        cnt += 1

if max_visiters == 0:
    print('SAD')
else:
    print(max_visiters)
    print(cnt)