import sys
sys.stdin=open("input.txt", "r")

n = int(input())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        n = 0
    else:
        result += 1
        n -= 2

if n == 0:
    print(result)
else:
    print(-1)