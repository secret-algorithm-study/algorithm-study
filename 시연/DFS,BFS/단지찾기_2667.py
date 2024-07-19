import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
grid = []
idx = 1
for i in range(n):
    grid.append(list(map(int, data[idx + i])))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
        return 0

    grid[x][y] = -1  # 방문한 집은 -1
    count = 1  # 현재 집

    # 상하좌우
    count += dfs(x + 1, y)
    count += dfs(x - 1, y)
    count += dfs(x, y + 1)
    count += dfs(x, y - 1)

    return count

complexes = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            house_count = dfs(i, j)
            complexes.append(house_count)

complexes.sort()

print(len(complexes))
for count in complexes:
    print(count)
