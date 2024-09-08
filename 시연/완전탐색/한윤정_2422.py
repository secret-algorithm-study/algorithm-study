def solve(N, M, bad_combinations):
    bad = [[False] * (N + 1) for _ in range(N + 1)]
    for a, b in bad_combinations:
        bad[a][b] = bad[b][a] = True
    
    def backtrack(start, depth, combination):
        if depth == 3:
            return 1
        
        total = 0
        for i in range(start, N + 1):
            if all(not bad[i][j] for j in combination):
                combination.append(i)
                total += backtrack(i + 1, depth + 1, combination)
                combination.pop()
        return total
    
    return backtrack(1, 0, [])

N, M = map(int, input().split())
bad_combinations = [tuple(map(int, input().split())) for _ in range(M)]

result = solve(N, M, bad_combinations)
print(result)