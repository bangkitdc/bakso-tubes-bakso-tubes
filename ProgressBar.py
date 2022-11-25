
from tqdm import tqdm
import time

#show Progress Bar from your program code 
def ProgressBar(): 
  for i in tqdm (range (100), 
                desc="Loading…", 
                ascii=False, ncols=90,colour='CYAN'):
      time.sleep(0.025)



 

 



