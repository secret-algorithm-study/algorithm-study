from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for i in range(len(dx)):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            continue
        
        if graph[nx][ny] == 0:
            continue

        if graph[nx][ny] == 1:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])