# read CFG Grammar from file
def readCFG(filepath):
    file = open(filepath, 'r').read()
    # split terminals, variables and productions
    terminals = file.split("Variables:")[0]
    variables = file.split("Variables:")[1].split("Productions:")[0]
    prods = file.split("Productions:\n")[1]

    # process terminals, variables, and productions
    terminals = terminals.replace("Terminals:","").replace("\n","").split(' ')
    variables = variables.replace("variables:","").replace("\n","").split(' ')
    prods = prods.replace("Production:","").split('\n')

    newprods = []
    for line in prods:
        key = line.split(" -> ")[0]
        value = line.split(" -> ")[1].split(" | ")
        for term in value:
            newprods.append((key, term.split(' ')))
    
    return terminals, variables, newprods

# return True if production is simple
def isSimpleProduction(terminals, variables ,prod):
	return len(prod[1]) == 1 and prod[0] in variables and prod[1][0] in terminals

# return list of simple production
def simpleProductionDict(terminals, variables, productions):
	result = {}
	for prod in productions:
		if len(prod[1]) == 1 and prod[0] in variables and prod[1][0] in terminals:
			result[prod[1][0]] = prod[0]
	return result

# return True if production is unitary
def isUnitary(prod, variables):
    return len(prod[1]) == 1 and prod[0] in variables and prod[1][0] in variables

# return True if there is any unitary production in productions
def isUnitaryExist(productions, variables):
    for prod in productions:
        if isUnitary(prod, variables): return True
    return False

# eliminate all unitary production in productions
def eliminateUnitary(productions, variables):
    newprods = []
    for prod in productions:
        if isUnitary(prod, variables):
            for iter_prod in productions:
                if prod[1][0] == iter_prod[0] and prod[0] != iter_prod[0]:
                    newprods.append((prod[0], iter_prod[1]))
        else:
            newprods.append(prod)
    return newprods

# generate new variable from existing variable
def generateVar(V):
    if V[-1] == '9':
        return V[:-2] + chr(ord(V[-2])+1) + '1'
    return V[:-2] + V[-2] + chr(ord(V[-1])+1)

# write CNF Grammar to txt file
def displayCNF(CNF, filename):
    result = ""
    for key in CNF:
        result += key + " -> "
        for val in CNF[key]:
            for v in val:
                result += v + " "
            if (val != CNF[key][-1]):
                result += " | "
        result += "\n"
    open(filename, 'w').write(result)

# read CFG Grammar from file then returning the CNF Grammar form
def CFGtoCNF(filepath):
    # load CFG terminals, variables, and productions
    terminals, variables, productions = readCFG(filepath)
    variables.append('S0')
    productions = [('S0', [variables[0]])] + productions

    # process non simple production with only terminals as values
    dict = simpleProductionDict(terminals, variables, productions)
    newprods = []

    for prod in productions:
        if not isSimpleProduction(terminals, variables, prod):
            for term in terminals:
                for index, value in enumerate(prod[1]):
                    if term == value:
                        prod[1][index] = dict[term]
        newprods.append(prod)

    productions = newprods

    # process productions with more than 2 values and adding new variables
    newprods = []
    newvar = "A0"

    for prod in productions:
        k = len(prod[1])
        if k <= 2:
            newprods.append(prod)
        else:
            newvar = generateVar(newvar)
            variables.append(newvar+'1')
            newprods.append((prod[0], [prod[1][0]] + [newvar+'1']))

            for i in range(1,k-2):
                var1 = newvar+str(i)
                var2 = newvar+str(i+1)
                variables.append(var2)
                newprods.append((var1, [prod[1][i], var2]))
            
            newprods.append((newvar+str(k-2), prod[1][k-2:k]))
    
    productions = newprods

    # process all unitary variables
    while isUnitaryExist(productions, variables):
        productions = eliminateUnitary(productions, variables)
    
    # convert processed CFG Grammar to CNF form
    cnf = {}
    for prod in productions:
        if prod[0] in cnf.keys():
            cnf[prod[0]].append(prod[1]) 
        else:
            cnf[prod[0]] = []
            cnf[prod[0]].append(prod[1])

    # write CNF to txt
    displayCNF(cnf, "txt/CNFGrammar.txt")

    # return CNF Grammar
    return cnf
