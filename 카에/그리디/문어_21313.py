import sys
sys.stdin=open("input.txt", "r")

n = int(input())

result = [1, 2] * (n // 2)

if n % 2 == 1:
    result.append(3)

print(*result)