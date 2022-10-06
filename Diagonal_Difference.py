import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    #get number of rows
    rows = len(arr)
    
    #initializing varibles
    leftright = 0
    rightleft = 0
    result = 0
    
    for i in range(rows):
        leftright += arr[i][i]
        rightleft += arr[i][rows-i-1]
        print(leftright)
        print(rightleft)
    #end for loop
    
    #get abs difference
    result = abs(leftright - rightleft)
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
