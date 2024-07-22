import sys
sys.stdin = open('input.txt', 'r')

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

# 초기 윈도우 설정
current_sum = sum(visitors[:x])
max_sum = current_sum
max_count = 1

# 슬라이딩 윈도우 적용
for i in range(x, n):
    current_sum += visitors[i] - visitors[i - x]
    if current_sum > max_sum:
        max_sum = current_sum
        max_count = 1
    elif current_sum == max_sum:
        max_count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_count)