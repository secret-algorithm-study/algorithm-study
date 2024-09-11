import sys
sys.stdin=open("input.txt", "r")

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# n = 변의 길이
def cutIntoQuarters(x, y, n):
    global white, blue
    color = paper[y][x]

    for tx in range(x, x+n):
        for ty in range(y, y+n):
            if color != paper[ty][tx]:
                cutIntoQuarters(x, y, n // 2)      
                cutIntoQuarters(x, y + n // 2, n // 2)     
                cutIntoQuarters(x + n // 2, y, n // 2)     
                cutIntoQuarters(x + n // 2, y + n // 2, n // 2) 
                return

    if color == 0: white += 1
    else: blue += 1

white, blue = 0, 0
cutIntoQuarters(0, 0, N)

print(white, blue, sep='\n')