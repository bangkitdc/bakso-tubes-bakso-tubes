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
    
    
