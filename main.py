import sys
import CFGtoCNF
import CYK
import CodeSplitter as split
import threading
import ProgressBar as PB
import splashscreen

# Initialize multithread
t1 = threading.Thread(target=PB.ProgressBar, name='t1')

# Splash screen
splashscreen.splash()
t1.start()

# CFG -> CNF (CFG from .txt)
CNFGrammar = CFGtoCNF.CFGtoCNF("grammar.txt")
filename = sys.argv[1]
print("Please wait! Compiling ...")

# Read testfile (.js)
output = split.splitCode(filename)

# Check with CYK algorithm
flag = CYK.cyk(output, CNFGrammar)

t1.join()
if flag :
    splashscreen.splashAcc()
    print("Accepted Answer!")
else:
    splashscreen.splashError()
    print("Syntax Error!")
