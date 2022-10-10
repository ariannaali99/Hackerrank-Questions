#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    
    for i in range(length):
        if(arr[i] < 0):
            negative += 1
        elif(arr[i] == 0):
            zero += 1
        else:
            positive += 1
    
    #get ratio
    positive = positive/length
    negative = negative/length
    zero = zero/length
    
    print(positive)
    print(negative)
    print(zero)
#end function

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
