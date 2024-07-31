import sys
sys.stdin = open('input.txt', 'r')

variable = input()


def isJava(variable):
    if '_' in variable:
        return False
    if not variable[0].islower():
        return False

    return True

def isCpp(variable):
    # '_'로 시작하는지 체크
    if variable.startswith('_'):
        return False
    
    # '_'로 끝나는지 체크
    if variable.endswith('_'):
        return False
    
    # '__'가 포함되어 있는지 체크
    if '__' in variable:
        return False
    
    # '_'가 적어도 하나 포함되어 있는지 체크
    if '_' not in variable:
        return False
    
    # '_'로 단어를 분리
    words = variable.split('_')
    
    # 각 단어가 모두 소문자인지 체크
    for word in words:
        # 단어가 비어있지 않은지 체크
        if not word:
            return False
        # 단어가 소문자인지 체크
        if not word.islower():
            return False
    
    # 모든 조건을 통과하면 True 반환
    return True


def cppToJava(variable):
    tokens = variable.split('_')

    java = tokens[0]
    for i in range(1, len(tokens)):
    
        java += tokens[i].capitalize()
    return java



def javaToCpp(variable):
    cpp = ''
    for i in range(len(variable)):
        if variable[i].isupper():
            
            cpp += '_' + variable[i].lower()
            
        else:
            cpp += variable[i]
    return cpp



if isJava(variable):
    print(javaToCpp(variable))
elif isCpp(variable):
    print(cppToJava(variable))
else:
    print('Error!')