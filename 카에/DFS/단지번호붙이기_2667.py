import sys
sys.stdin=open("input.txt", "r")

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answer = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
  global cnt
  cnt += 1

  graph[x][y] = 0

  for i in range(4):
    nx = dx[i]+x
    ny = dy[i]+y

    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
      dfs(nx, ny)

for i in range(n):
  for j in range(n):
    cnt = 0
    if graph[i][j] == 1:
      dfs(i, j)
      answer.append(cnt)

answer.sort()
print(len(answer))
for i in answer:
  print(i)