import sys
sys.stdin = open('input.txt', 'r')


string = input().strip()

pikachuToken = ['pi' , 'ka' , 'chu']

index = 0

while index < len(string):
    #플래그
    found = False
    #피카츄 토큰 순회
    for token in pikachuToken:
        #피카츄 토큰으로 시작하는지 체크
        if string[index:].startswith(token):
            index += len(token)
            found = True
            break
    if not found:
        print("NO")
        exit()
            

print("YES")

