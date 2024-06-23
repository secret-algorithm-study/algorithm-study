import sys
sys.stdin=open("input.txt", "r")

n =  int(input())
todo_list = input()

colors = {
    'B': 0,
    'R': 0
}

colors[todo_list[0]] = 1

for i in range(1, n):
    if todo_list[i] != todo_list[i-1]:
        colors[todo_list[i]] += 1

print(min(colors['B'], colors['R'])+1)