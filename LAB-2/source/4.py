import numpy as np      #importing
import random
from collections import Counter
a=np.random.random_integers(0,20,15)        #randomly taking 15 numbers from 0 to 20
print(a)                                    #printing the randomly generated numbers
print(Counter(a))                           #printing the each number and their frequency
print(Counter(a).most_common(1)[0])         #number with maximum number of occurances
