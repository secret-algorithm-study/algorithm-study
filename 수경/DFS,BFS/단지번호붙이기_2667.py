import sys
sys.stdin=open("input.txt", "r")

n = int(input().strip())
m = []

for _ in range(n):
    m.append(list(map(int, input())))
    
d = [(-1,0),(1,0),(0,-1),(0,1)]
v = [[False]*n for _ in range(n)]

def findHouse(x,y):
    q = [(x,y)]
    house_size = 1
    v[r][c] = True # 삽질ㅠ
    
    while q:
        x,y = q.pop(0)
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            
            if not (0 <= nx < n and 0 <= ny < n): continue # bound check
            if not m[nx][ny]: continue # wall check
            if v[nx][ny]: continue # visited check
            
            v[nx][ny] = True
            q.append((nx,ny))
            house_size += 1
            
    return house_size
    
    
houses = []  
for r in range(n):
    for c in range(n):
        if not m[r][c]: continue # wall check
        if v[r][c]: continue # visited check
                
        house_size = findHouse(r,c)
        if not house_size: continue # no house
        
        houses.append(house_size)
        
print(len(houses))
for house in sorted(houses): print(house)