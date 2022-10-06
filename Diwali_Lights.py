import math
import os
import random
import re
import sys

def lights(n):
    
    #checking constraint
    if(n < 0 or n > 10000):
        return 
    
    perm = ((2**n) - 1)
    perm = perm % (100000)
    return perm          
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
