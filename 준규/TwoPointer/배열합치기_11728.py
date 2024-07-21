import sys
sys.stdin = open('input.txt', 'r')


n , m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))


aIndex = 0
bIndex = 0
result = []

while aIndex != n or bIndex != m:

    
    if aIndex == n:
        result.append(b[bIndex])
        bIndex += 1
    elif bIndex == m:
        result.append(a[aIndex])
        aIndex += 1
    else:
        if a[aIndex] < b[bIndex] :
            result.append(a[aIndex])
            aIndex += 1
        else:
            result.append(b[bIndex])
            bIndex += 1



print(' '.join(map(str, result)))



