import sys
sys.stdin=open("input.txt", "r")

n  = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

def polling(n, x, y):
    half = n//2
    if n == 2:
        arr = [graph[x][y], graph[x+1][y], graph[x][y+1], graph[x+1][y+1]]
        arr.sort()
        return arr[-2]

    left_top = polling(half, x, y)
    right_top = polling(half, x+half, y)
    left_bottom = polling(half, x, y+half)
    right_bottom = polling(half, x+half, y+half)
    arr = [left_top, right_top, left_bottom, right_bottom]
    arr.sort()
    return arr[-2]

print(polling(n,0,0))