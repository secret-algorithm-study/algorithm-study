n = int(input())

g = []
v = [[False]*n for _ in range(n)]
d = [(1,0),(0,1)]

for _ in range(n):
    g.append(list(map(int, input().split())))
    
def bfs(x,y):
    q = [(x,y)]
    while q:
        x,y = q.pop(0)
        if (x,y)==(n-1,n-1):
            return True
        for dx,dy in d:
            nx = x + dx * g[x][y]
            ny = y + dy * g[x][y]
            if not (0 <= nx < n and 0 <= ny < n): continue
            if v[nx][ny]: continue
            v[nx][ny] = True                
            q.append((nx,ny))
    return False
            
print('HaruHaru' if bfs(0,0) else 'Hing')