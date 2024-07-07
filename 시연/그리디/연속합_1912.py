n = int(input())
sequence = list(map(int, input().split())) 

max_current = sequence[0]
max_global = sequence[0]

for i in range(1, n):
    # 현재 위치에서 끝나는 최대 부분합 계산
    max_current = max(sequence[i], max_current + sequence[i])
    
    if max_current > max_global:
        max_global = max_current

print(max_global)
