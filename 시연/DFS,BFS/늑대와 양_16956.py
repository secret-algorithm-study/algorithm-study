
R, C = map(int, input().split())
pasture = [list(input().strip()) for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(R):
    for c in range(C):
        if pasture[r][c] == 'S':
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if pasture[nr][nc] == 'W': # 늑대
                        print(0)
                        exit()
                    elif pasture[nr][nc] == '.': # 빈 곳
                        pasture[nr][nc] = 'D'

print(1)
for row in pasture:
    print(''.join(row))
