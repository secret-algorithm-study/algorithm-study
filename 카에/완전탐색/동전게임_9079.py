import sys
sys.stdin=open("input.txt", "r")
from collections import deque

# 목표 상태
TARGETS = [
    [['H', 'H', 'H'], ['H', 'H', 'H'], ['H', 'H', 'H']],
    [['T', 'T', 'T'], ['T', 'T', 'T'], ['T', 'T', 'T']]
]

def array_to_string(arr):
    return ''.join([''.join(row) for row in arr])

def flip_state(state, indices):
    new_state = [row[:] for row in state]
    for (i, j) in indices:
        new_state[i][j] = 'H' if new_state[i][j] == 'T' else 'T'
    return new_state

def bfs(start):
    queue = deque([(start, 0)])  # (현재 배열, 연산 횟수)
    visited = {array_to_string(start)}

    # 가능한 모든 조작 인덱스
    operations = [
        [(0, 0), (0, 1), (0, 2)],  # 1st row
        [(1, 0), (1, 1), (1, 2)],  # 2nd row
        [(2, 0), (2, 1), (2, 2)],  # 3rd row
        [(0, 0), (1, 0), (2, 0)],  # 1st column
        [(0, 1), (1, 1), (2, 1)],  # 2nd column
        [(0, 2), (1, 2), (2, 2)],  # 3rd column
        [(0, 0), (1, 1), (2, 2)],  # main diagonal
        [(0, 2), (1, 1), (2, 0)]   # anti diagonal
    ]

    while queue:
        current, steps = queue.popleft()

        if current in TARGETS:
            return steps

        for operation in operations:
            new_state = flip_state(current, operation)
            new_state_str = array_to_string(new_state)
            if new_state_str not in visited:
                visited.add(new_state_str)
                queue.append((new_state, steps + 1))

    return -1  # 모든 경우를 탐색했지만 목표 상태에 도달하지 못한 경우

t = int(input())

for _ in range(t):
    coins = [list(input().split()) for _ in range(3)]
    result = bfs(coins)
    print(result)
