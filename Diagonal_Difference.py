import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rows = len(arr)
    columns = len(arr[0])
    rightToLeft = 0
    leftToRight = 0
    
    if(rows == columns):
        for i in range(rows):
            if(arr[i][i] < -100 or arr[i][i] > 100):
                return
            
            else:
                #print(arr[i][i])
                #print(arr[rows-i-1][i])
                rightToLeft += arr[i][i]
                leftToRight += arr[rows-i-1][i]
        #end for loop
    #absolute value
    result = abs(rightToLeft - leftToRight)
    return result
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
