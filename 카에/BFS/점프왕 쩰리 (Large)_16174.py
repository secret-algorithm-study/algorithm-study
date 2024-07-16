import sys
sys.stdin=open("input.txt", "r")
from collections import deque

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
q = deque()
q.append((0, 0))
visited[0][0] = True
result = False

while q:
  x, y = q.popleft()
  if x == n-1 and y == n-1:
    result = True
    break
  else: 
    for i in range(2):
      jump = field[x][y]
      nx = dx[i] * jump + x
      ny = dy[i] * jump + y
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
        q.append((nx, ny))
        visited[nx][ny] = True

print('HaruHaru' if result else 'Hing')

