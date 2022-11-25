import sys
import CFGtoCNF
import CYK
import CodeSplitter as split
import threading
import ProgressBar as PB
import splashscreen



t1 = threading.Thread(target=PB.ProgressBar, name='t1')
splashscreen.splash()
t1.start()

CNFGrammar = CFGtoCNF.CFGtoCNF("grammar.txt")
filename = sys.argv[1]
print("Please wait! Compiling ...")
output = split.splitCode(filename)
flag = CYK.cyk(output, CNFGrammar)

t1.join()
if flag :
    splashscreen.splashAcc()
    print("Accepted Answer!")
else:
    splashscreen.splashError()
    print("Syntax Error!")
