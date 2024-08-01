import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(limit1, limit2):
    global result, arr
    for i in range(limit1-1):
        j = 1
        while j < limit2 - 2:
            if arr[i][j] == 'X' and arr[i][j+1] == 'X':
                if arr[i+1][j] == '.' and arr[i+1][j+1] == '.':
                    result +=1
                    j += 2
                    continue
            elif arr[i][j] == '.' and arr[i][j+1] == '.':
                if arr[i+1][j] == 'X' and arr[i+1][j+1] == 'X':
                    result += 1
                    j += 2
                    continue
            j += 1

M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(input().strip()))

result = 0
check(M, N)
arr = list(zip(*arr))
check(N, M)

print(result)