import sys
input = sys.stdin.readline

n, x = map(int, input().split())
day = list(map(int, input().split()))


value = sum(day[:x])
max_value = value
max_cnt = 1

if max(day) == 0:
    print('SAD')
    exit(0)

for i in range(x, n):
    value += day[i] # 뒤에 값 더하기
    value -= day[i-x] # 앞에 값 빼기

    if value > max_value:
        max_value = value
        max_cnt = 1
    elif value == max_value:
        max_cnt += 1

print(max_value)
print(max_cnt)