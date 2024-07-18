import sys
sys.stdin=open("input.txt", "r")

n,m = map(int, input().strip().split())

d = [(-1,0),(1,0),(0,-1),(0,1)]

g = []
v = [[-1]*m for _ in range(n)]

tx,ty = 0,0

for i in range(n):
    g.append(list(map(int,input().strip().split())))
    for j in range(m):
        if not g[i][j]==2: continue
        tx,ty = i,j

def distance_bfs(x,y):
    q = [(x,y)]
    v[x][y] = 0
    
    while q:
        x,y = q.pop(0)
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            
            if not (0<=nx<n and 0<=ny<m): continue # bound check
            if v[nx][ny] != -1: continue # visited check
            if g[nx][ny] == 0: continue # wall check
            
            v[nx][ny] = v[x][y]+1
            q.append((nx,ny))
            
for i in range(n):
    for j in range(m):
        if not g[i][j]: v[i][j] = 0

distance_bfs(tx,ty)
for i in v: print(*i)