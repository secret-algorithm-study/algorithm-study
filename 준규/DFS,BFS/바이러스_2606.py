import sys
sys.stdin=open("input.txt", "r")


computerNumber = int(input());
loopCount = int(input());


node = [];
visit = [0] * (computerNumber+1)

for i in range(computerNumber+1):
    node.append([])



for i in range(loopCount):
    a , b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)



def DFS(n) : 
    
    visit[n] = 1

    for i in node[n]:
        if visit[i] == 0:
            DFS(i)    



DFS(1)

print(sum(visit)-1)