import sys
sys.stdin=open("input.txt", "r")

# Two Pointers

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1 = 0
p2 = 0
answer = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        answer.append(a[p1])
        p1+=1
    else:
        answer.append(b[p2])
        p2+=1

if p1 < n:
    answer.extend(a[p1:])
elif p2 < m:
    answer.extend(b[p2:])

print(*answer)

# 일반

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = a+b
answer.sort()
print(*answer)

