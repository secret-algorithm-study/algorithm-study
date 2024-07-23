import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
M = int(data[1])

A = list(map(int, data[2:2+N]))
B = list(map(int, data[2+N:]))

n = len(A)
m = len(B)

result = []
i, j = 0, 0

while i < n and j < m:
    if A[i] <= B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1

# 남아 있는 요소들을 결과에 추가
while i < n:
    result.append(A[i])
    i += 1

while j < m:
    result.append(B[j])
    j += 1

# 결과 출력
print(' '.join(map(str, result)))