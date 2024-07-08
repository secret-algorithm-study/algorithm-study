

import sys
sys.stdin=open("input.txt", "r")

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = []

for _ in range(t):
  m, n, k = map(int, input().split())

  graph = [[0]*(n) for _ in range(m)]

  for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

  def dfs(x, y):
    graph[x][y] = 0
    
    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y

      if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
        dfs(nx, ny)
  
  cnt = 0
  for i in range(m):
    for j in range(n):
      if graph[i][j] == 1:
        dfs(i , j)
        cnt += 1
  answer.append(cnt)

for i in answer:
  print(i)