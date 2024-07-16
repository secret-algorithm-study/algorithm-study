from collections import deque

n = int(input())  # 게임 구역의 크기 N
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 이동 가능한 방향은 오른쪽과 아래 뿐
dx = [0, 1]
dy = [1, 0]

queue = deque([(0, 0)])  # 출발점 (0, 0)
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

while queue:
    x, y = queue.popleft()
    
    if board[x][y] == -1:
        print("HaruHaru")
        exit()

    move_distance = board[x][y]

    for i in range(2):  # 2가지 방향만 검사
        nx, ny = x + dx[i] * move_distance, y + dy[i] * move_distance

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            queue.append((nx, ny))
            visited[nx][ny] = True

print("Hing")
