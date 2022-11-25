import src.CFGtoCNF
import src.CYK
import src.CodeSplitter as split
import src.splashscreen
import sys
import colorama
import threading

# Initialize multithread
t1 = threading.Thread(target=src.splashscreen.ProgressBar, name='t1')

# Splash screen
src.splashscreen.splash()
t1.start()

# CFG -> CNF (CFG from .txt)
CNFGrammar = src.CFGtoCNF.CFGtoCNF("txt/grammar.txt")
filename = "test/" +  sys.argv[1]
output = split.splitCode(filename)
print("Please wait! Compiling ...")

# Read testfile (.js)
output = split.splitCode(filename)

# Check with CYK algorithm
flag = src.CYK.cyk(output, CNFGrammar)

t1.join()
if flag :
    src.splashscreen.splashAcc()
    print("Accepted "+colorama.Fore.WHITE+"Answer!\n")
else:
    src.splashscreen.splashError()
    print(colorama.Fore.WHITE+"Syntax"+colorama.Fore.RED+" Error!\n")
