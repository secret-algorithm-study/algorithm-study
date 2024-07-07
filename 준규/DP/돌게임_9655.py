import sys
sys.stdin=open("input.txt", "r")

n = int(input());

array = [-1] * 1001;

array[1] = 0; #SK
array[2] = 1; #CY
array[3] = 0; #SK


for i in range(4, n+1):
    if array[i - 1] != 1 or array[i - 3] != 1:
        array[i] = 1;
    else:
        array[i] = 0;

print('SK' if array[n] == 0 else 'CY');

