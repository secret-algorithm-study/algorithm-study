import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")

a,b = map(int,input().split());

result = 1;

while a != b:
    result += 1;
    current_b = b;
    if(b % 10 == 1):
        b = b // 10;
    elif(b % 2 == 0):
        b = b // 2;
    

    if current_b == b:
        result = -1;
        break



print(result);
