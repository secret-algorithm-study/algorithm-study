import sys
sys.stdin=open("input.txt", "r")

# Point!) 임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않는다.

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort()

dy = [0]*100001

for i in range(n):
    if i == 0:
        dy[0] = meetings[0][2]
    elif i == 1:
    # max(회의를 진행하는 경우 , 앞 회의를 진행하는 경우)
        dy[1] = max(meetings[1][2], dy[i-1])
    else:
        dy[i] = max(dy[i-2] + meetings[i][2], dy[i-1])

print(dy[n-1])