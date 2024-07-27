import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = sys.maxsize

left = 0
right = 0
one_count = 1 if arr[0] == 1 else 0

while right < n:
    if one_count < k:
        right += 1
        if right < n and arr[right] == 1:
            one_count += 1
    else:
        answer = min(answer, right - left + 1)
        if arr[left] == 1:
            one_count -= 1
        left += 1

print(-1 if answer == sys.maxsize else answer)
