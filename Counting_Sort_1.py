import math
import os
import random
import re
import sys

def countingSort(arr):
    frequencyarr = [0]*100
    length = len(arr)
    
    if(len(arr) < 100 or len(arr) > 1000000):
        return
        
    for i in range(length):
        if(arr[i] < 0 or arr[i] > 99):
            return
        else:
            frequencyarr[arr[i]] += 1
    return frequencyarr    
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
