import sys
sys.stdin = open("/Users/jungyu/Documents/algorithm-study/준규/그리디/input.txt" , "r")

expression = input().strip()


separatedByMinus = expression.split("-")

partialSumList = [];


for exp in separatedByMinus:
    partialSumList.append(sum(map(int, exp.split("+"))));
    

first = partialSumList[0]

result = first - sum(partialSumList[1:])

print(result)





