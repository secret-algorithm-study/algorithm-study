n = int(input())
meets = [list(map(int, input().split())) for _ in range(n)]
sortedMeets = sorted(meets, key=lambda x: (x[1], x[0]))

cnt = 0
lastEnd = 0
for start,end in sortedMeets:
  if(start < lastEnd): continue
  cnt += 1
  lastEnd = end
  
print(cnt)