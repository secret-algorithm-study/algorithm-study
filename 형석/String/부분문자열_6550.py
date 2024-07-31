while True:
    try:
        s, t = input().split()
 
        pos, s_len = 0, len(s)
        for i in range(len(t)):
            if s[pos] == t[i]:
                pos += 1
            if pos == s_len:
                break
 
        if pos == len(s): print("Yes")
        else: print("No")
    except EOFError:
        break