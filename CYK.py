# contoh
# NP   ->  Det | Nom
# Nom  ->  AP | Nom
# AP   ->  Adv | A
# Det  ->  a | an
# Adv  ->  very | extremely
# AP   ->  heavy | orange | tall
# A    ->  heavy | orange | tall | muscular
# Nom  ->  book | orange | man

# Non-terminal symbols
non_terminals = ["NP", "Nom", "Det", "AP",
                  "Adv", "A"]

# Terminal symbols
terminals = ["book", "orange", "man",
             "tall", "heavy",
             "very", "muscular"]

# Rules of the grammar
R = {
     "NP": [["Det", "Nom"]],
     "Nom": [["AP", "Nom"], ["book"],
             ["orange"], ["man"]],
     "AP": [["Adv", "A"], ["heavy"],
            ["orange"], ["tall"]],
     "Det": [["a"]],
     "Adv": [["very"], ["extremely"]],
     "A": [["heavy"], ["orange"], ["tall"],
           ["muscular"]]
    }

# w = "a very heavy orange book".split()
# n = len(w)

# T = [[set([]) for i in range(n)] for j in range(n)]

# for i in range(n):
#     for LHS, RHS in R.items():  # prodRule = LHS : RHS (1 | 2 | .. | N)
#         for elements in RHS:
#             print(elements)

def cyk(w, cnfGrammar):
    n =  len(w)

    # CYK Table
    T = [[set([]) for j in range(n)] for i in range(n)]

    for j in range(n):
        for LHS, RHS in cnfGrammar.items():  # prodRule = LHS : RHS (1 | 2 | .. | N)
            for elements in RHS:             # elements = [A, B, C]
                # if terminal is found
                if len(elements) == 1 and elements[0] == w[j]:
                    T[j][j].add(LHS)
    
        for i in range(j, -1, -1):
            # iterate over i - (j + 1)
            for k in range(i, j + 1):
                # iterate over the rules
                for LHS, RHS in cnfGrammar.items():
                    for elements in RHS:
                        # if 2 variables is found
                        if len(elements) == 2 and elements[0] in T[i][k] and elements[1] in T[k + 1][j]:
                            T[i][j].add(LHS)

    if "S0" in T[0][n - 1]:
        print("Accepted Answer!")
    else:
        print("Syntax Error!")