n = int(input())
meets = [list(map(int, input().split())) for _ in range(n)]
sorted_meets = sorted(meets, key=lambda x: (x[1], x[0]))

cnt = 0
last_end = 0
for start,end in sorted_meets:
  if(start < last_end): continue
  cnt += 1
  last_end = end
  
print(cnt)