import sys
sys.stdin=open("input.txt", "r")

n = int(input())
fitness_equipment = list(map(int, input().split()))
fitness_equipment.sort()

p1 = 0
p2 = n-1 if n % 2 == 0 else n-2
result = [] if n % 2 == 0 else [fitness_equipment[-1]]

while p1 < p2:
    result.append(fitness_equipment[p1]+fitness_equipment[p2])
    p1+=1
    p2-=1
    

print(max(result))