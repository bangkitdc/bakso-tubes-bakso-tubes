import sys
import CFGtoCNF
import CYK
import CodeSplitter as split
import threading
import ProgressBar as PB
# t1 = threading.Thread(target=PB.ProgressBar, name='t1')
CNFGrammar = CFGtoCNF.CFGtoCNF("grammarfixbrow.txt")

filename = sys.argv[1]
print("Please wait! Compiling ...")

output = split.splitCode(filename)
# t1.start()
# t1.join()
CYK.cyk(output, CNFGrammar)
