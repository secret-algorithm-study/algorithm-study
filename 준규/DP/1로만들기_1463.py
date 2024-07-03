import sys

sys.stdin=open("input.txt", "r")

n = int(input());

dp = [0] * 1000001;

for i in range(2, n+1):

    dp[i] = dp[i-1] + 1;
    mins = [dp[i-1] + 1];
    if i % 2 == 0:
        mins.append(dp[i//2] + 1);
    if i % 3 == 0:
        mins.append(dp[i//3] + 1);

    dp[i] = min(mins);

print(dp[n]);