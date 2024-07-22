import sys
sys.stdin=open("input.txt", "r")

n,m = map(int,input().split())

# 이미 정렬된 배열
a = list(map(int, input().split())) 
b = list(map(int, input().split()))

sorted = []

ap,bp = 0,0

while not (ap==len(a) and bp==len(b)):
    if ap==len(a):
        sorted.append(b[bp])
        bp += 1
    elif bp==len(b):
        sorted.append(a[ap])
        ap += 1
    else:
        if a[ap] < b[bp]:
            sorted.append(a[ap])
            ap += 1
        else:
            sorted.append(b[bp])
            bp += 1

print(*sorted) # 187280kb, 2684ms
# print(*sorted(arr)) # 182816kb, 1512ms
