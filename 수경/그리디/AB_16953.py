base, dest = map(int, input().split())

cnt = 0

while (dest > base):
  if(dest % 2 == 0): dest = int(dest / 2)
  elif(dest % 10 == 1): dest = int(str(dest)[:-1])
  else: break
  cnt += 1
  
print(cnt + 1) if (dest == base) else print(-1)