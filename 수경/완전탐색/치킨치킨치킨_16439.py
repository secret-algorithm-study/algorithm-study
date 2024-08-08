import sys
sys.stdin=open("input.txt", "r")

import itertools

n,m = map(int,input().split())

prfs = [list(map(int, input().split())) for _ in range(n)]
combs = list(itertools.combinations(range(m), 3))

sums = []
for i,j,k in combs:
    sum = 0
    for prf in prfs:
        sum += max(prf[i],prf[j],prf[k])
    sums.append(sum)

print(max(sums))

