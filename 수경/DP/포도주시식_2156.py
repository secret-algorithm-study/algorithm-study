n = int(input())

wines = [0]
wines.extend(int(input()) for _ in range(n))

dp = [0]*10001

dp[1] = wines[1]

if n==1:
  print(dp[1])
  exit()

dp[2] = wines[1] + wines[2]

if n==2:
  print(dp[2])
  exit()

dp[3] = max(wines[1] + wines[3], wines[2] + wines[3], dp[2])

for i in range(4, n+1):
  a = dp[i-2] + wines[i]
  b = dp[i-3] + wines[i-1] + wines[i]
  c = dp[i-1] # 해당 잔 마시지 않는 경우
  dp[i] = max(a,b,c)

print(max(dp[:n+1]))