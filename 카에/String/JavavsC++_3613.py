import sys
sys.stdin=open("input.txt", "r")

s = input()

def check_Java_or_Cpp(s):
    if '_' in s:
        # C++ 형식인지 확인
        if s[0] == '_' or s[-1] == '_' or '__' in s:
            print('Error!')
            return
        for char in s:
            if char.isupper():
                print('Error!')
                return
        return 'CPP'
    else:
        # Java 형식인지 확인
        if s[0].isupper():
            print('Error!')
            return
        for char in s:
            if char == '_':
                print('Error!')
                return
        return 'JAVA'


# snake case -> camel case
def make_java_variable_name(s):
    _s = s.split('_')
    answer = ''

    for i, v in enumerate(_s):
        if i == 0:
            answer += v
        else:
            answer += v.capitalize()
    return answer

# camel case -> snake case
def make_Cpp_variable_name(s):
    idx = 0
    n = len(s)
    answer = ''

    while idx < n:
        if  s[idx].isupper():
            answer += ('_' + s[idx].lower())
            idx+=1
        else:
            answer += s[idx]
            idx+=1

    return answer

lang = check_Java_or_Cpp(s)

if lang == 'CPP':
    print(make_java_variable_name(s))
elif lang == 'JAVA':
    print(make_Cpp_variable_name(s))
