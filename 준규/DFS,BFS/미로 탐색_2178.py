from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

queue = deque()
queue.append((0, 0))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
              


print(maze[n-1][m-1])