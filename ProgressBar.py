
from tqdm import tqdm
import time
# Python program to illustrate the concept
# of threading
import threading
import os
  
def ProgressBar():  

  for i in tqdm (range (100), 
                desc="Loading…", 
                ascii=False, ncols=90):
      time.sleep(0.005)

  # print("Complete")


 

 



