import sys
sys.stdin=open("input.txt", "r")
from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    x, y = q.popleft()

    # Goal
    if x == n-1 and y == m-1:
        print(graph[x][y])
        break
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx, ny))