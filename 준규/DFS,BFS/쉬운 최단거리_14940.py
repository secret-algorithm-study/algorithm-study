import sys
from collections import deque
sys.stdin = open('input.txt', 'r');


n, m = map(int, input().split())
matrix = []
queue = deque([])
visit = [[0]*m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))

    # 목표지점 찾고 Matrix 형성
    for j in range(m):
        if row[j] == 2:
            queue.append((i, j))
            visit[i][j] = 1
            # 목표 지점은 거리 0
            row[j] = 0
        elif row[j] == 0:
            visit[i][j] = 0
    matrix.append(row)


dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 목표지점 부터 각 지점까지의 최단 거리 계산
while queue:
    x, y = queue.popleft()

    #4방향 탐색
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if matrix[nx][ny] == 1 and visit[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                matrix[nx][ny] = matrix[x][y] + 1

# 도달할 수 없는 지점은 -1로 표시
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visit[i][j] == 0:
            matrix[i][j] = -1

for row in matrix:
    for i in row:
        print(i, end=" ")
    print()