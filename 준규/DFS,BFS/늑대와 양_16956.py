import sys
sys.stdin=open("input.txt", "r")


r , c = map(int, input().split())

matrix = [];

x = [-1 , 1 , 0 , 0]
y = [0 , 0 , -1 , 1]

for i in range(r):
    matrix.append(list(input()))


for i in range(r):
    for j in range(c):
        current = matrix[i][j]
        if current == 'W':
            for k in range(4):
                if( 0<=i + x[k] < r and 0<= j + y[k] < c):
                    if matrix[i+x[k]][j+y[k]] == 'S':
                        print(0)
                        exit(0)
                        

        if current == '.':
            for k in range(4):
                if( 0<=i + x[k] < r and 0<= j + y[k] < c):
                    if matrix[i+x[k]][j+y[k]] == 'W':
                        matrix[i][j] = 'D'
                        

print(1)

for i in matrix:
    print(''.join(i))
