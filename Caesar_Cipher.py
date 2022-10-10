import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    
    if(k < 0 or k > 100):
        print("Invalid Input")
        return
    
    solution = ""
    length = len(s)
    k = k % 26
    
    #check constraints
    if(length < 1 or length > 100):
        print("Invalid String Size")
        return
    
    #iterating through the string
    for i in range(length):
        curr = s[i]
        curr = ord(curr)
        
        #check if any is a space
        if(curr == 32):
            print("Invalid Char")
            return 
    
        #checking if it is a letter
        elif(curr >= 97 and curr <= 122):
            
            shift = (curr + k - 97) % 26
            curr = shift + 97
        
        elif(curr >= 65 and curr <= 90):
            shift = (curr + k - 65) % 26
            curr = shift + 65
            
        solution += chr(curr)        
    return solution
#end function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
