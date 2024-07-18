import sys
sys.stdin=open("input.txt", "r")
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
q = deque()

r, c, n = map(int, input().split())
grid = [list(input()) for _ in range(r)]

def bfs(q,data):
    while q:
        x, y = q.popleft()
        data[x][y] = '.'
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0 <= nx < r and 0 <= ny < c and data[nx][ny] == 'O':
                data[nx][ny] = '.'

def simulate(time):
    global grid, q
    if time == 1:
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    q.append((i,j))
    elif time % 2 == 1:
        bfs(q,grid)
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':
                    q.append((x,y))
    else:
        grid = [['O']*c for _ in range(r)]

for i in range(1,n+1):
    simulate(i)

for row in grid:
    print(''.join(row))