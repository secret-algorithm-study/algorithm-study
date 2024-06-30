import sys
sys.stdin=open("input.txt", "r")

n = int(input())
distances = list(map(int, input().split()))
gas_stations = list(map(int, input().split()))

cheap_price = gas_stations[0]
result = distances[0] * gas_stations[0]

for i in range(1, n-1):
    if cheap_price > gas_stations[i]:
        cheap_price = gas_stations[i]
    
    result += cheap_price * distances[i]

print(result)
