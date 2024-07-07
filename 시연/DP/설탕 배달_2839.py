
# 직관적인 풀이

N = int(input())
count = 0

while N > 0:
    if N % 5 == 0:
        count += N // 5
        break
    N -= 3
    count += 1

if N < 0:
    print(-1)
else:
    print(count)


# DP로 풀이
N = int(input().strip())

dp = [0] * 5001

if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

for n in range(6, N + 1):
    if dp[n - 3] and dp[n - 5]:
        dp[n] = min(dp[n - 3], dp[n - 5]) + 1
    elif dp[n - 3]:
        dp[n] = dp[n - 3] + 1
    elif dp[n - 5]:
        dp[n] = dp[n - 5] + 1


print(dp[N]) if dp[N] else print(-1)