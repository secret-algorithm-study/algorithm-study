import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')


purpose = input()

bookCount = int(input())

bookTokens = []
bookPrices = []



for _ in range(bookCount):
    price , bookName = input().split()
    bookTokens.append(bookName)
    bookPrices.append(int(price))




# Check 함수
def canMakePurpose(books):
    combinedBooks = ''.join(books)

    for char in purpose:
        if char in combinedBooks:
            combinedBooks = combinedBooks.replace(char, '', 1)
        else:
            return False
    return True



minPrice = float('inf')



for i in range(1, bookCount + 1):
    for comb in combinations(range(bookCount), i):
        selectedBooks = [bookTokens[idx] for idx in comb]
        if canMakePurpose(selectedBooks):
            totalPrice = sum([bookPrices[idx] for idx in comb])
            if totalPrice < minPrice:
                minPrice = totalPrice

print(minPrice if minPrice != float('inf') else -1)