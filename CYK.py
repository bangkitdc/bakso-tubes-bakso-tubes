# contoh penggunaan
# NP   ->  Det | Nom
# Nom  ->  AP | Nom
# AP   ->  Adv | A
# Det  ->  a | an
# Adv  ->  very | extremely
# AP   ->  heavy | orange | tall
# A    ->  heavy | orange | tall | muscular
# Nom  ->  book | orange | man

# Non-terminal symbols
# non_terminals = ["NP", "Nom", "Det", "AP",
#                   "Adv", "A"]

# Terminal symbols
# terminals = ["book", "orange", "man",
#              "tall", "heavy",
#              "very", "muscular"]

# Rules of the grammar
# R = {
#      "NP": [["Det", "Nom"]],
#      "Nom": [["AP", "Nom"], ["book"],
#              ["orange"], ["man"]],
#      "AP": [["Adv", "A"], ["heavy"],
#             ["orange"], ["tall"]],
#      "Det": [["a"]],
#      "Adv": [["very"], ["extremely"]],
#      "A": [["heavy"], ["orange"], ["tall"],
#            ["muscular"]]
#     }

def cyk(w, cnfGrammar):
    n = len(w)
    T = [[set([]) for i in range(n)] for j in range(n)]

    for i in range(n):
        for variable in cnfGrammar.items():
                for terminal in variable[1]:
                    if len(terminal) == 1 and terminal[0] == w[i]:
                        T[i][i].add(variable[0])

    for l in range(2,n+1):
        for i in range (0,n-l+1):
            j = i+l-1
            for k in range (i,j):
                for variable in cnfGrammar.items():
                    for production in variable[1] :
                        if len(production) == 2 :
                            if(production[0] in T[i][k]) and (production[1] in T[k+1][j]):
                                T[i][j].add(variable[0])

    if "S0" in T[0][n-1] :
        return True
    else:
        return False
