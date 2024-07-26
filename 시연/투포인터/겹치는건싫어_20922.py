N, K = map(int, input().split())

a = list(map(int, input().split()))

max_length = 0
start, end = 0, 0

count = [0] * (max(a) + 1)

while end < N:
    # 현재 숫자의 출현 횟수가 K보다 적다면 윈도우를 확장
    if count[a[end]] < K:
        count[a[end]] += 1
        end += 1
    else:
        # 현재 숫자의 출현 횟수가 K 이상이면 윈도우의 시작점을 이동
        count[a[start]] -= 1
        start += 1
    
    max_length = max(max_length, end - start)

print(max_length)
