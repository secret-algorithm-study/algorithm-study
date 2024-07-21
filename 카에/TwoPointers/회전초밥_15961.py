import sys
sys.stdin=open("input.txt", "r")

n, d, k, c = map(int, input().split())
belt = list(int(input()) for _ in range(n))
checks = [0]*(d+1)
checks[c]  =1
eat_sushi_cnt = 1
max_eat_sushi_cnt = 0

for i in range(k):
    sushi = belt[i%n]

    if checks[sushi] == 0:
        eat_sushi_cnt +=1
    checks[sushi] += 1

max_eat_sushi_cnt = max(max_eat_sushi_cnt, eat_sushi_cnt)

for i in range(n):
    p1 = belt[i % n]
    p2 = belt[(i+k)%n]

    checks[p1] -= 1
    if checks[p1] == 0:
        eat_sushi_cnt -= 1
    
    if checks[p2] == 0:
        eat_sushi_cnt += 1
    checks[p2] += 1
    max_eat_sushi_cnt = max(max_eat_sushi_cnt, eat_sushi_cnt)

print(max_eat_sushi_cnt)

