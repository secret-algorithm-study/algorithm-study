import sys
sys.stdin=open("input.txt", "r")

n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

day = n
result = 0
arr = []

for i in range(n):
    arr.append((H[i], A[i]))

# 성장 속도가 제일 빠른 애는 제일 마지막 날에 자르면 됨!
arr.sort(key=lambda x:x[1])

for i in range(n):
    target_tree_len = arr[i][0]
    target_tree_speed = arr[i][1]
    # 첫 날에는 target_tree_speed = 0이어야 함
    result += target_tree_len + target_tree_speed * i

print(result)
