def cyk(w, cnfGrammar):
    n =  len(w)
    dp = [[set([]) for i in range(n)] for j in range(n)]

    for i in range(n):
        for var in cnfGrammar.items():
            for terminal in var[1]:
                if len(terminal) == 1 and terminal[0] == w[i]:
                    dp[i][i].add(var[0])
    
    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for var in cnfGrammar.items():
                    for production in var[1]:
                        if len(prod) == 2:
                            if (prod[0] in dp[i][k]) and (prod[1] in dp[k + 1][j]):
                                dp[i][j].add(var[0])
    
    if "S0" in dp[0][n - 1]:
        print("Accepted Answer!")
    else:
        print("Syntax Error!")