import string

def readGrammar(filepath):
    file = open(filepath, 'r').read()
    terminals = file.split("Variables:")[0]
    variables = file.split("Variables:")[1].split("Productions:")[0]
    prods = file.split("Productions:\n")[1]

    terminals = terminals.replace("Terminals","").replace("\n","").split(' ')
    variables = variables.replace("variables","").replace("\n","").split(' ')
    prods = prods.replace("Production:","").split('\n')

    newprods = []
    for line in prods:
        key = line.split(" -> ")[0]
        value = line.split(" -> ")[1].split(" | ")
        for term in value:
            newprods.append((key, term.split(' ')))
    
    return terminals, variables, newprods


print(readGrammar('grammarfixbrow.txt'))