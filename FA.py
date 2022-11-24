def q1(c):  # input character pertama (start state)
    if (65 <= ord(c) <= 90):        # A - Z
        state = 2
    elif (ord(c) == 95):            # _
        state = 2
    elif (97 <= ord(c) <= 122):     # a - z
        state = 2
    else:
        state = 3
    return state

def q2(c):  # final state
    if (65 <= ord(c) <= 90):        # A - Z
        state = 2
    elif (ord(c) == 95):            # _
        state = 2
    elif (97 <= ord(c) <= 122):     # a - z
        state = 2
    elif (48 <= ord(c) <= 57):      # 0 - 9
        state = 2
    else:
        state = 3
    return state

def q3(c):  # input character yang salah (dead state)
    state = 3
    return state

def isValidVariable(s):
    state = 1
    for i in range(len(s)):
        if (state == 1):
            state = q1(s[i])
        if (state == 2):
            state = q2(s[i])
        if (state == 3):
            state = q3(s[i])
    if (state == 2): # final state
        return True
    else:
        return False

def q4(c):  # input character pertama (start state)
    if (48 <= ord(c) <= 57):        # 0 - 9
        state = 5
    else:
        state = 6
    return state

def q5(c):  # final state
    if (48 <= ord(c) <= 57):
        state = 5
    else:
        state = 6
    return state

def q6(c): # input character yang salah (dead state)
    state = 6
    return state

def isValidNumber(s):
    state = 4
    for i in range(len(s)):
        if (state == 4):
            state = q4(s[i])
        if (state == 5):
            state = q5(s[i])
        if (state == 6):
            state = q6(s[i])
    if (state == 5): # final state
        return True
    else:
        return False