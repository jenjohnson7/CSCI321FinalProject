#Jen Johnson
#CSCI321
#Problem 14 kmer DBGraph

import sys
import numpy as np
from overlap import overlap_graph
from strDBGraph import str_DBGraph

def kmer_DBGraph(kmers):
    """  makes a dictionary where key == prefix, and value == suffix """
    result_dict = dict()

    for i in range (0, len(kmers)):
        prefix_key = kmers[i][:-1]
        suffix_value = kmers[i][1:]
        if prefix_key not in result_dict:
            result_dict[prefix_key] = [suffix_value]
        else: #already in dict, update
            existing_suffix = result_dict[prefix_key]
            temp = existing_suffix + [suffix_value]
            result_dict[prefix_key] = temp

    keys = result_dict.keys()

    return result_dict, keys

def main():
    print("running")

if __name__=="__main__":
    main()
