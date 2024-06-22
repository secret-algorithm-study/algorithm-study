import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")

n = int(input());

total_coin_num = 0;
 
while (n > 0) :
    # 5로 나누어 떨어지는 경우
    if(n % 5 == 0) :
        total_coin_num += n // 5
        n = 0;
        break;
    # 5로 나누어 떨어지지 않는 경우
    n -= 2
    total_coin_num += 1


print(total_coin_num) if n == 0 else print(-1)

