
from tqdm import tqdm
import time

  
def ProgressBar():  
  for i in tqdm (range (100), 
                desc="Loading…", 
                ascii=False, ncols=90,colour='MAGENTA'):
      time.sleep(0.005)

  # print("Complete")


 

 



