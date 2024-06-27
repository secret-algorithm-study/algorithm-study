import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")



n = int(input())                       
height = list(map(int, input().split()))    
growSpeed = list(map(int,input().split())) 


arr = []
total = 0

for i in range(n):                 
    arr.append([height[i], growSpeed[i]])

arr.sort(key = lambda x:x[1])  


for i in range(n):
    total += arr[i][0] + arr[i][1] * i;

print(total)