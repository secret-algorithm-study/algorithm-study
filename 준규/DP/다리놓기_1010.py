import sys
sys.stdin=open("input.txt", "r")

# Memory 31120
# Time 116

loopCount = int(input());


for i in range(loopCount):
    n , m = map(int , input().split());

    matrix = [[0 for i in range(m+1)] for j in range(n+1)];
    for i in range (1 , n+1) :
        for j in range (1, m+1):

            if i == 1:
                matrix[i][j] = j;
                continue;
            elif i == j:
                matrix[i][j] = 1;
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1];
    
    print(matrix[n][m])



# Memory 31120
# Time 88

loopCount = int(input());


def factorial(n):
    if n == 1:
        return 1;
    else:
        return n * factorial(n-1);


def factorial2(n) :
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result




for i in range(loopCount):
    n , m = map(int , input().split());
    
    print(factorial2(m) // (factorial2(n) * factorial2(m-n)));




