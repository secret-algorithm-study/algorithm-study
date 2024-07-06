import sys
sys.stdin=open("input.txt", "r")

computers_cnt = int(input())
n = int(input())

graph = [[0]*(computers_cnt+1) for _ in range(computers_cnt+1)]
visited = [0]* (computers_cnt+1)
cnt = 0

for _ in range(n):
  x, y = map(int, input().split())

  graph[x][y] = 1
  graph[y][x] = 1

def dfs(vertex):
  global computers_cnt, cnt
  visited[vertex] = 1
  cnt += 1

  for next in range(1, computers_cnt+1):
    if graph[vertex][next] == 1 and visited[next] == 0:
      dfs(next)

dfs(1)
print(cnt-1)



