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
import threading
import ProgressBar as PB
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

# n = len(w)

# T = [[set([]) for i in range(n)] for j in range(n)]

# for i in range(n):
#     for LHS, RHS in R.items():  # prodRule = LHS : RHS (1 | 2 | .. | N)
#         for elements in RHS:
#             print(elements)

def cyk(w, cnfGrammar):
    n = len(w)
    T = [[set([]) for i in range(n)] for j in range(n)]
    t1 = threading.Thread(target=PB.ProgressBar, name='t1')
    # t1.start()
    for i in range(n):
        for var in cnfGrammar.items():
                for termin in var[1]:
                    if len(termin) == 1 and termin[0] == w[i]:
                        T[i][i].add(var[0])

    for l in range(2,n+1):
        for i in range (0,n-l+1):
            j = i+l-1
            for k in range (i,j):
                for var in cnfGrammar.items():
                    for prod in var[1] :
                        if len(prod) == 2 :
                            if(prod[0] in T[i][k]) and (prod[1] in T[k+1][j]):
                                T[i][j].add(var[0])

    # t1.join()
    if "S0" in T[0][n-1] :
        return True
        # print("Accepted Answer!")
    else:
        return False
        # print("Syntax Error!")
