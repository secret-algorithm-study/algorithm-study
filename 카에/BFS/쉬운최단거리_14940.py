import sys
sys.stdin=open("input.txt", "r")
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = [[-1]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            visited[i][j] = True
            answer[i][j] = 0
            q.append((i ,j))
        elif graph[i][j] == 0:
            visited[i][j] = True
            answer[i][j] = 0


while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            visited[nx][ny] = True
            answer[nx][ny] = answer[x][y]+1
            q.append((nx, ny))

for row in answer:
    print(*row)
