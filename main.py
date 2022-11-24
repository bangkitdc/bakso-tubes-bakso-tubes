import sys
import CFGtoCNF
import CYK
import CodeSplitter as split
CNFGrammar = CFGtoCNF.CFGtoCNF("grammarfixfix.txt")

filename = sys.argv[1]
print("Please wait! Compiling ...")

output = split.splitCode(filename)
CYK.cyk(output, CNFGrammar)