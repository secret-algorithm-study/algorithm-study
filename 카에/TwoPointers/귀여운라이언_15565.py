import sys
sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
animal_dolls = list(map(int, input().split()))

left = 0
count = 0
min_len = n+1

for right in range(n):
  if animal_dolls[right] == 1:
    count += 1
  
  while count >= k:
    min_len = min(min_len, right-left+1)

    if animal_dolls[left] == 1:
      count -= 1
    left += 1

print(-1 if min_len == n+1 else min_len)

