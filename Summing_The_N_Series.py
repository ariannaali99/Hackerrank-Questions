import math
import os
import random
import re
import sys

def summingSeries(n):
    if(n < 1 or n > 10000000000000000):
        return
    
    summation = n * n 
    summation = summation % (1000000000 + 7)
    return summation
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
