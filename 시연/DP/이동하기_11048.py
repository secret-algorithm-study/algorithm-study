import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]

# 첫 번째 행과 열은 각각 이전 위치에서 현재 위치로 이동하는 단 하나의 경로만 존재
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + maze[i][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + maze[0][j]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i][j] # 세 방향 중 최대값 + 현재 셀의 값 

print(dp[N-1][M-1])