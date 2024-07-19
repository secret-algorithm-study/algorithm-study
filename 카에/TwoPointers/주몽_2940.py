import sys
sys.stdin=open("input.txt", "r")

n = int(input())
m = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()
p1 = 0
p2 = n-1
cnt = 0

while p1 < p2:
    total = ingredients[p1] + ingredients[p2]
    if total == m:
        cnt +=1
        p1 += 1
        p2 -= 1
    elif total < m:
        p1 += 1
    else:
        p2 -= 1

print(cnt)