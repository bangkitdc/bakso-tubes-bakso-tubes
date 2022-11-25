import sys
import CFGtoCNF
import CYK
import CodeSplitter as split
import threading
import ProgressBar as PB
import splashscreen
import colorama


t1 = threading.Thread(target=PB.ProgressBar, name='t1')

# Splash screen
splashscreen.splash()
t1.start()

# CFG -> CNF (CFG from .txt)
CNFGrammar = CFGtoCNF.CFGtoCNF("grammar.txt")
filename = sys.argv[1]
output = split.splitCode(filename)
print("Please wait! Compiling ...")

# Read testfile (.js)
output = split.splitCode(filename)

# Check with CYK algorithm
flag = CYK.cyk(output, CNFGrammar)

t1.join()
if flag :
    splashscreen.splashAcc()
    print("Accepted "+colorama.Fore.WHITE+"Answer!\n")
else:
    splashscreen.splashError()
    print(colorama.Fore.WHITE+"Syntax"+colorama.Fore.RED+" Error!\n")


