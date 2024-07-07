import sys
sys.stdin=open("input.txt", "r")

n = int(input())

dy = [0] * 1000001

for i in range(2, n+1):
    # 현재 수에서 1을 빼는 경우 
    dy[i] = dy[i-1]+1

    # 현재 수가 2로 나눠 떨어지는 경우
    if i % 2 == 0:
        dy[i] = min(dy[i], dy[i // 2]+1)

    # 현재 수가 3로 나눠 떨어지는 경우
    if i % 3 == 0:
        dy[i] = min(dy[i], dy[i // 3]+1)

print(dy[-1])