# 2x + 5y = N일 때 x + y가 최소가 되는 경우의 수

n = int(input())
count = 0

while n>0:
    if n%5 == 0:
        count += int(n/5)
        break
    else:
        n -= 2
        count += 1 

if n < 0:
    print(-1)
else:
    print(count)