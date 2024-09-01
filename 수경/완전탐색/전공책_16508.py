import sys
sys.stdin=open("input.txt", "r")

import itertools
import collections

t = input()
n = int(input())

books = []
for _ in range(n):
    price, title = input().split()
    books.append((int(price), collections.Counter(title)))
    
combs = []
for r in range(1, n+1):
    combs.extend(list(itertools.combinations(range(n),r)))
    
prices = []
for comb in combs:
    price = 0
    counter = collections.Counter()
    for bookIdx in comb:
        price += books[bookIdx][0]
        counter += books[bookIdx][1]
    
    matched = True
    for c in t:
        if counter[c]:
            counter[c] -= 1
        else:
            matched = False
            
    if matched: prices.append(price)
    
print(sorted(prices)[0] if prices else -1)