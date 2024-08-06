from collections import deque

masks = [
    0b111000000,
    0b000111000,
    0b000000111, 
    0b100100100, 
    0b010010010, 
    0b001001001,  
    0b100010001, 
    0b001010100   
]

def bitmask(bit_board):
    q = deque([(bit_board, 0)])
    visited = [bit_board]
    
    while q:
        cur_bit_board, count = q.popleft()
        
        if cur_bit_board == 0 or cur_bit_board == 0b111111111:
            return count
        
        for mask in masks:
            new_bit_board = cur_bit_board ^ mask
            if new_bit_board not in visited:
                visited.append(new_bit_board)
                q.append((new_bit_board, count + 1))
    
    return -1

T = int(input())

for _ in range(T):
    board = [input().split() for _ in range(3)]
    
    bit_board = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'T':
                bit_board |= (1 << (8 - (i * 3 + j)))

    print(bitmask(bit_board))