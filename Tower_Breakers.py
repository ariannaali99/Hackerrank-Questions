import math
import os
import random
import re
import sys

def towerBreakers(n, m):
    
    #check constraints
    if(n < 1 or n > 1000000):
        return
    
    if(m < 1 or m > 1000000):
        return
    
    if(m == 1):
        return 2
    
    if(n%2 == 0 and m%2 == 0):
        return 2
    elif(n%2 == 1 and m%2 == 0):
        return 1
    elif(n%2 == 1 and m%2 == 1):
        return 1
    elif(n%2 == 0 and m%2 == 1):
        return 2

#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
