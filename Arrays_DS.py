import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    length = len(a)
    
    #check constraints
    if(length < 1 or length > 1000):
        print("Invalid Length")
    
    newArr = [0]* length
    #iterate through the array
    for i in range(length):
        #iterate backwards
        if(a[length-i-1] < 1 or a[length-i-1] > 10000):
            print("Invalid Element")
        else:
            newArr[i] = a[length-i-1]
    #end for loop
    return newArr
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
