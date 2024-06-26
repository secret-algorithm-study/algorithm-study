import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")

n = int(input().strip())

times = [list(map(int, input().split())) for _ in range(n)]

sortedTimes = sorted(times, key=lambda x: (x[1], x[0]))

startTime = 0;

result = 0;


for sortedTime in sortedTimes:
    if(startTime <= sortedTime[0]):
        startTime = sortedTime[1];
        result += 1;

print(result)



