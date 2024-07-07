n = int(input())

dp = [0]*5001

dp[3] = 1
dp[5] = 1

for i in range(6,n+1):
  a = dp[i-3]
  b = dp[i-5]
  
  if a==0 and b==0:
    dp[i] = 0
    continue
  
  if a==0: k=b
  elif b==0: k=a
  else: k = min(a,b)
  
  dp[i] = k+1
  
print(dp[n]) if dp[n]!=0 else print(-1)