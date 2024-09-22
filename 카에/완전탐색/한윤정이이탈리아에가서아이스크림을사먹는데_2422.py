import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
bad_combination = [[False for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    t1, t2 = map(int, input().split())
    bad_combination[t1][t2] = True
    bad_combination[t2][t1] = True

count = 0

def dfs(depth, start, picked_taste):
  global count

  if depth == 3:
    # dfs의 깊이 3이 되었을 때 고른 3가지 맛들이 섞어먹으면 안 되는 조합인지 검사한다
    taste_1, taste_2, taste_3 = picked_taste
    if not bad_combination[taste_1][taste_2] and not bad_combination[taste_1][taste_3] and not bad_combination[taste_2][taste_3]:
      count+=1
  else:
    for i in range(start, n+1):
      dfs(depth+1, i+1, picked_taste+[i])


dfs(0, 1, [])
print(count)
