import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max = -1000
    sum = -1000
    
    #iterating through 2D array
    for i in range(6):  
         
        if(i == 0 or i == 5):
            continue
                     
        for j in range(6):
            
            if(j == 0 or j == 5):
                continue
                
            #find all indexes that need to be added
            #top
            topx1 = abs((j-1)%6)
            topx2 = j%6
            topx3 = (j+1)%6
            topy = abs((i-1)%6)
            
            #bottom x values is the same as top
            boty = (i+1)%6
            
            #middle is current
            #hour glass calculation
            sum = arr[topy][topx1] + arr[topy][topx2] + arr[topy][topx3] + arr[i][j] + arr[boty][topx1] + arr[boty][topx2] + arr[boty][topx3]
            
            if(sum > max):
                max = sum
        #end inner for loop
    #end outer for loop
    return max      
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
