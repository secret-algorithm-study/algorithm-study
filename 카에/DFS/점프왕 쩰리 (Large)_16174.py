import sys
sys.stdin=open("input.txt", "r")

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
visited[0][0] = True
result = False

def dfs(x, y):
  jump = field[x][y]
  for i in range(2):
    nx = dx[i] * jump + x
    ny = dy[i] * jump + y

    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
      visited[x][y] = True
      dfs(nx, ny)


dfs(0,0)
print('HaruHaru' if visited[n-1][n-1] == True else 'Hing')
