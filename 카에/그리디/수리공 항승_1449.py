import sys
sys.stdin=open("input.txt", "r")

n, tape_len = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()

tape_cnt = 1
# 좌우로 0.5cm를 막아야 한다는 말을 계산 편의상 다르게 생각하면, 한 출발지에서 1cm 떨어진곳에서부터 붙이면 된다는 말이다 😉
tape_start_position = pipe[0]-1

for i in range(1, n):
    if pipe[i] <= tape_start_position + tape_len:
        continue
    else:
        tape_cnt +=1
        tape_start_position = pipe[i]-1

print(tape_cnt)




