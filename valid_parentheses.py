def is_valid(s):

    dt = {
        '{' : '}',
        '[' : ']',
        '(' : ')' 
    } 

    stk = []
    
    for i in range(len(s)):
        if s[i] in dt:
            stk.append(s[i])
        elif len(stk) != 0 and dt[stk[-1]] == s[i]:
            stk.pop()
            continue
        else:
            return False
    
    if len(stk) != 0:
        return False
    else:
        return True
            
        

print(is_valid("(("))
