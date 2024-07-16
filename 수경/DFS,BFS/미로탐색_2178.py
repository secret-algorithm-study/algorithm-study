n,m = map(int, input().split())

g = []

for _ in range(n):
  g.append(list(map(int,input())))

d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
  q = []
  q.append((x,y))

  while q:
    x,y = q.pop(0)

    for dx,dy in d:
      nx = x+dx
      ny = y+dy

      if not (0<=nx<n and 0<=ny<m): continue
      if g[nx][ny]!=1: continue

      g[nx][ny] = g[x][y]+1
      q.append((nx,ny))

  return g[n-1][m-1]

print(bfs(0,0))