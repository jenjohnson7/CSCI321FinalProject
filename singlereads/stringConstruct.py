#Jen Johnson
#CSCI321
#Problem 11 string_construct

import sys
import numpy as np

def string_construct(kmers):
    result = kmers[0]
    for i in range (1, len(kmers)):
        result += kmers[i][-1]
    return result

def main():
    print("running")

if __name__=="__main__":
    main()
