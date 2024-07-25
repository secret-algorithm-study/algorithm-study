import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 숫자 등장 횟수 저장 배열
count = [0] * 100001  
left = 0
max_length = 0

for right in range(n):
    count[arr[right]] += 1
    
    # 현재 숫자가 k번을 초과하여 등장하면, left 포인터를 이동
    while count[arr[right]] > k:
        count[arr[left]] -= 1
        left += 1
    
    # 최대 길이 갱신
    max_length = max(max_length, right - left + 1)

print(max_length)