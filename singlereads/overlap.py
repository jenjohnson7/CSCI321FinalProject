#Jen Johnson
#CSCI321
#Problem 12 overlap graph

import sys
import numpy as np

def overlap_graph(kmers):
    """returns an adj matrix for an overlap graph based on prefixes and suffixes"""

    result = []

    for i in range (0, len(kmers)):
        suffix = kmers[i][1:]
        followers = []
        for j in range (0, len(kmers)):
            prefix = kmers[j][:-1]
            if prefix == suffix:
                followers.append(kmers[j])
        result.append(followers)

    return result

def main():
    print("running")

if __name__=="__main__":
    main()
