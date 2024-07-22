import sys
sys.stdin=open("input.txt", "r")

n = int(input())
solution = list(map(int, input().split()))
solution.sort()

p1 = 0
p2 = n-1
min_solution = sys.maxsize
answer = []

while p1 < p2:
    total = solution[p1] + solution[p2]
    if abs(total) < min_solution:
        answer = [solution[p1], solution[p2]]
        min_solution = abs(total)

    if total < 0:
        p1 +=1
    else:
        p2 -=1

print(*answer)