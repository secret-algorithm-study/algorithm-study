from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

goalX, goalY = -1, -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            goalX, goalY = i, j
            break
    if goalX != -1:
        break


queue = deque([(goalX, goalY)])
distance = [[-1] * m for _ in range(n)] # -1로 초기화 하는 이유: 0으로 초기화하면 0이면 방문한 것으로 처리되기 때문
distance[goalX][goalY] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]


while queue:
    x, y = queue.popleft()

    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and distance[nx][ny] == -1: 
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end = ' ')
        
    print()