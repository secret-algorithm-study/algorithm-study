import sys
sys.stdin=open("input.txt", "r")

def compress(matrix, x, y, n):
    # 현재 부분이 모두 같은 숫자인지 확인
    first_value = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != first_value:
                # 같지 않으면 4개로 나누어서 재귀 호출
                half = n // 2
                return "(" + compress(matrix, x, y, half) + compress(matrix, x, y + half, half) + compress(matrix, x + half, y, half) + compress(matrix, x + half, y + half, half) + ")"
    
    # 모두 같은 숫자라면 그 숫자를 반환
    return first_value

N = int(input())
matrix = [input().strip() for _ in range(N)]

result = compress(matrix, 0, 0, N)
print(result)
