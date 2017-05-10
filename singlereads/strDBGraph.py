#Jen Johnson
#CSCI321
#Problem 13 str to DB graph

import sys
import numpy as np
from kmersOfString import kmers_of_string
from overlap import overlap_graph
from collections import OrderedDict

def str_DBGraph(kmers, graph):
    """ turns an overlap graph into DB graph by gluing identical nodes"""

    result = OrderedDict()
    #keys = nodes, values = set of followers based on prefix/suffix matching

    for i in range (0, len(kmers)):
        # for each kmer, look for repeats in graph
        if result.has_key(kmers[i]):
            #if there are repeats, merge the adj list of followers into a set to prevent repeats
            current_followers_set = set(result[kmers[i]])
            for j in range (0, len(graph[i])):
                current_followers_set.add(graph[i][j])
            result[kmers[i]] = current_followers_set
        else:
            # if there are no repeats, add the followers into a set to prevent repeats
            current_followers_set = set(graph[i])
            result[kmers[i]] = current_followers_set

    keys = result.keys()
    return result, keys

def main():
    print("running")

if __name__=="__main__":
    main()
