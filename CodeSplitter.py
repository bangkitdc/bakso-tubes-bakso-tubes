import re       #regular expression
import FA as fa

def splitCode(filename):
    f = open(filename, "r")
    inputFile = f.read()
    f.close()

    result = []

    # ignore blanks
    inputFile = inputFile.split(" ")
    for statement in inputFile:
        if statement != '':
            result.append(statement)    # insert to result
    
    operator = [r'\(', r'\)', r'\[', r'\]', r'\{', r'\}', r'\*', r'\*\*', r'\+', r'\+\+', r'\-', r'\-\-', '%', ',', '/', '-', ':', ';', '<', '=', '>', '!=', '==', '>=', '<=', '===', r'\'', r'\"', r'\/\*', r'\*\/',r'\`','null', 'true', 'false', 'for', 'if', 'else', 'while', 'do', 'break', 'continue', 'function', 'return', 'throw', 'catch', 'finally', 'throw', 'try', 'catch', 'delete', 'class', 'extends', 'from', 'import', 'export', 'switch', 'case', 'default', 'var', 'let', 'const', 'as', 'in', 'and', '\n']
    operator2 = ['(', ')', '[', ']', '{', '}', '*', '**', '+', '++', '-', '--', '%', ',', '/', '-', ':', ';', '<', '=', '>', '!=', '==', '>=', '<=', '===', "'", '"', r'/*', r'*/', r'\`','null', 'true', 'false', 'for', 'if', 'else', 'while', 'do', 'break', 'continue', 'function', 'return', 'throw', 'catch', 'finally', 'throw', 'try', 'catch', 'delete', 'class', 'extends', 'from', 'import', 'export', 'switch', 'case', 'default', 'var', 'let', 'const', 'as', 'in', 'and', '\n'] 

    # Split the string for each op and statement
    for op in operator:
        temp = []
        for statement in result:
            elmt = re.split(r'[A..z]*(' + op + r')[A..z]*', statement)

            for splitted in elmt:
                temp.append(splitted)
        result = temp
    
    # check list
    temp = []

    for statement in result:
        if statement in operator2:
            temp.append(statement)
        else:
            if (fa.isValidVariable(statement)):
                temp.append('a')
            elif (fa.isValidNumber(statement)):
                temp.append('-1')
            elif statement == '':
                continue
    
    for i in range(len(temp)):
        if temp[i] == '\n':
            temp[i] = 'newline'
        
    print(temp)
    return temp
