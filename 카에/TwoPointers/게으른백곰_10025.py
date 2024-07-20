import sys
sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())

pails = [0]* 1000001
end_pail_position = 0

for _ in range(n):
    g, x = map(int, input().split())
    pails[x] = g
    end_pail_position = max(end_pail_position, x)

moving_area = k*2+1
total = sum(pails[:moving_area])
max_ices = total

for i in range(moving_area, end_pail_position+1):
    total -= pails[i-moving_area]
    total += pails[i]
    max_ices = max(max_ices, total)

print(max_ices)