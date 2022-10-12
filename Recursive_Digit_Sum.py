import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
   #check size of string
   length = len(n)
   print(n)
   
   if(length == 1 or k == 0):
    return n

   else:
        newString = ''
        sum = 0
        for i in range(length):
            if(n[i] == '1'):
                sum += 1
            elif(n[i] == '2'):
                sum += 2
            elif(n[i] == '3'):
                sum += 3
            elif(n[i] == '4'):
                sum += 4
            elif(n[i] == '5'):
                sum += 5
            elif(n[i] == '6'):
                sum += 6
            elif(n[i] == '7'):
                sum += 7
            elif(n[i] == '8'):
                sum += 8
            elif(n[i] == '9'):
                sum += 9
        #end for loop
        newString = str(sum)
        return superDigit(newString, k-1)
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
