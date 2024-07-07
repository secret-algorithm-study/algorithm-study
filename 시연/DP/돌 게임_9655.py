# 직관적인 풀이

N = int(input())
 
if N % 2 == 0 :
    print("CY")
else:
    print("SK")

# n이 짝수이면 CY, 홀수이면 SK가 이김


# DP로 풀이
N = int(input())
dp = [0] * 1001 # 0 ~ 1000까지의 수를 저장할 리스트

dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, N+1):
    if dp[i - 1] == 0 or dp[i - 3] == 0:
        dp[i] = 1  # 상근이가 이기는 경우
    else:
        dp[i] = 0  # 창영이가 이기는 경우

if dp[N] == 1:
    print("SK")
else:
    print("CY")
