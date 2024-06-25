import sys
from collections import deque
sys.stdin=open("input.txt", "r")

a, b = map(int, input().split())

# 풀이 1

queue = deque()
queue.append([a, 0])

result = -1

while queue:
    current_num, cnt = queue.popleft()

    if current_num == b:
        result = cnt
        break

    print(queue)
    
    if current_num*2 <= b:
        queue.append([current_num*2, cnt+1])
    if int(str(current_num)+'1') <= b:
        queue.append([int(str(current_num)+'1'), cnt+1])

print(result+1)

# 풀이 2 (풀이 1보다 조금 더 빠름)

result = 0

while b != a:
    if b % 10 == 1:
        b = int(b/10)
        result += 1
    elif b % 2 == 0 and b > 0:
        b = int(b/2)
        result += 1
    else:
        result = -1
        break

print(result+1)

