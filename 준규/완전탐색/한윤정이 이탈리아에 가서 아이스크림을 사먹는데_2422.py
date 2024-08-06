# import sys
# from itertools import combinations
# sys.stdin = open('input.txt', 'r')


# prohibitions = []
# result = 0
# n , m = map(int, input().split());


# for i in range(m):
#     prohibitions.append(list(map(int, input().split())))


# for comb in combinations(range(1, n + 1), 3):
#     a, b, c = comb
#     is_ok = True
#     for prohibition in prohibitions:
#         if [a, b] == prohibition or [a, c] == prohibition or [b, c] == prohibition:
#             is_ok = False
#             break
#     if is_ok:
#         result += 1
            
            

# print(result)

## 시간초과






import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')


prohibitions = set()
result = 0
n , m = map(int, input().split());

for _ in range(m):
    a, b = map(int, input().split())
    prohibitions.add((a, b))
    prohibitions.add((b, a))


for comb in combinations(range(1, n + 1), 3):
    a, b, c = comb
    if (a, b) not in prohibitions and (a, c) not in prohibitions and (b, c) not in prohibitions:
        result += 1
            
            

print(result)



