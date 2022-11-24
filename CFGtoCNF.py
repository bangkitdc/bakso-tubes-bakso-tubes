def readCFG(filepath):
    file = open(filepath, 'r').read()
    terminals = file.split("Variables:")[0]
    variables = file.split("Variables:")[1].split("Productions:")[0]
    prods = file.split("Productions:\n")[1]

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

def isSimple(terminals, variables ,prod):
	return len(prod[1]) == 1 and prod[0] in variables and prod[1][0] in terminals

def setupDict(terminals, variables, productions):
	result = {}
	for prod in productions:
		if len(prod[1]) == 1 and prod[0] in variables and prod[1][0] in terminals:
			result[prod[1][0]] = prod[0]
	return result

def isUnitary(prod, variables):
    return len(prod[1]) == 1 and prod[0] in variables and prod[1][0] in variables

def isUnitaryExist(productions, variables):
    for prod in productions:
        if isUnitary(prod, variables): return True
    return False

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

def generateVar(V):
    if V[-1] == '9':
        return V[:-2] + chr(ord(V[-2])+1) + '1'
    return V[:-2] + V[-2] + chr(ord(V[-1])+1)


def CFGtoCNF(filepath):
    
    terminals, variables, productions = readCFG(filepath)
    variables.append('S0')
    productions = [('S0', [variables[0]])] + productions
    dict = setupDict(terminals, variables, productions)

    newprods = []
    newvar = "AA0"
    for prod in productions:
        if isSimple(terminals, variables, prod):
            newprods.append(prod)
        else:
            for term in terminals:
                for index, value in enumerate(prod[1]):
                    if term == value and not term in dict:
                        newvar = generateVar(newvar)
                        dict[term] = newvar
                        variables.append(dict[term])
                        newprods.append((dict[term], [term]))
                        prod[1][index] = dict[term]
                    elif term == value:
                        prod[1][index] = dict[term]
            newprods.append( (prod[0], prod[1]) )

    productions = newprods

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

    while isUnitaryExist(productions, variables):
        productions = eliminateUnitary(productions, variables)
    
    cnf = {}
    for prod in productions:
        if prod[0] in cnf.keys():
            cnf[prod[0]].append(prod[1]) 
        else:
            cnf[prod[0]] = []
            cnf[prod[0]].append(prod[1])

    return cnf
