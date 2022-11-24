import re       #regular expression
import FA as fa

def splitCode(filename):
    f = open(filename, "r")
    inputFile = f.read()
    f.close()

    result = []

    # ignore blanks
    inputFile = inputFile.replace("\n","").split(" ")

    for statement in inputFile:
        if statement != '':
            result.append(statement)    # insert to result
    
    operator = [r'\(', r'\)', r'\[', r'\]', r'\{', r'\}', r'\*', r'\*\*', r'\+', r'\+\+', r'\-', r'\-\-', '%', ',', r'\.', '/', '-', ':', ';', '<', '=', '>', '!=', '==', '>=', '<=', '===', r'\'', r'\"', r'\/\*', r'\*\/',r'\`','null', 'true', 'false', 'for', 'else', 'while', 'break', 'continue', 'function', 'return', 'throw', 'catch', 'finally', 'throw', 'try', 'catch', 'delete', 'class', 'extends', 'from', 'import', 'export', 'switch', 'case', 'default', 'var', 'const']
    operator2 = ['(', ')', '[', ']', '{', '}', '*', '**', '+', '++', '-', '--', '%', ',', '.', '/', '-', ':', ';', '<', '=', '>', '!=', '==', '>=', '<=', '===', "'", '"', r'/*', r'*/', r'\`','null', 'true', 'false', 'for', 'else', 'while', 'break', 'continue', 'function', 'return', 'throw', 'catch', 'finally', 'throw', 'try', 'catch', 'delete', 'class', 'extends', 'from', 'import', 'export', 'switch', 'case', 'default', 'var', 'const'] 

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
            if statement == 'in' or statement == 'if' or statement == 'as' or statement == 'do' or statement == 'let':
                temp.append(statement)
            else:
                if (fa.isValidVariable(statement)):
                    temp.append('a')
                elif (fa.isValidNumber(statement)):
                    temp.append('1')
                elif statement == '':
                    continue
        
    return temp