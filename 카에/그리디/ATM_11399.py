import sys
sys.stdin=open("input.txt", "r")

n = int(input())
people = list(map(int, input().split()))
people.sort()

time = [people[0]]

for i in range(1, n):
    time.append(time[-1] + people[i])

print(sum(time))