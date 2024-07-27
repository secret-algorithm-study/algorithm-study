import sys
sys.stdin = open('input.txt', 'r')



for line in sys.stdin:
    word = line.strip().split()

    s , t = word[0] , word[1]
    
    s_arr = list(s)
    t_arr = list(t)

    s_index = 0
    result = False
    for i in range(len(t_arr)):
        # S의 문자와 T의 문자가 같은 경우
        if(t_arr[i] == s_arr[s_index] and s_index < len(s_arr)):
            s_index += 1

        # S의 문자 탐색 끝
        if s_index == len(s_arr):
            result = True
            break
            

    if result:
        print('Yes')
    else:
        print('No')