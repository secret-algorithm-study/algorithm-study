import sys
sys.stdin=open("input.txt", "r")

n = int(input())

# 그리디 -------------------------------------

result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        break
    elif n >= 3:
        n -= 3
        result += 1
    else:
        result = -1
        break

print(result)

# DP  -------------------------------------

# n <= 5000이기 때문에 아래와 같이 초기화
dy = [5001]*5001 
dy[3] = 1
dy[5] = 1

for i in range(6, n+1):
    dy[i] = min(dy[i-3], dy[i-5])+1

print(dy[n] if dy[n] < 5001 else -1) 




