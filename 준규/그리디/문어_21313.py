import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")

n = int(input());

share = n // 2

print('1 2 ' * share) if n % 2 == 0 else print('1 2 ' * share + '3')


