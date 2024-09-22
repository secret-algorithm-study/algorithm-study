import sys
sys.stdin=open("input.txt", "r")


def divide_conquer(idx):  
    if idx == 0:  
        return False  
    if idx % 2:  
        return not divide_conquer(idx // 2)  
    else:  
        return divide_conquer(idx // 2)  
    
K = int(input())

print(1 if divide_conquer(K-1) else 0)