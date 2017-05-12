""" Jen Johnson
CSCI 321 Spring 17 Final Project
calculates the edit distance between two genomes """

from itertools import product
from enum import IntEnum
import numpy as np
from Bio.SubsMat import MatrixInfo

def global_alignment(seq1, seq2, scoring, indel):
    """ returns the global alignment
    Code from CSCI321 Spring 17 Professor Linderman """

    n, m = len(seq1)+1, len(seq1)+1
    scores = np.zeros((n,m), dtype=np.int)

    for i in range(1, n):
        scores[i,0] = scores[i-1,0] + indel
    for j in range(1, m):
        scores[0,j] = scores[0,j-1] + indel

    for i in range(1, n):
        for j in range(1, m):
            incoming = (scores[i-1,j-1] + scoring[seq1[i-1], seq2[j-1]],
                        scores[i-1,j] + indel,
                        scores[i,j-1] + indel
                        )
            index = np.argmax(incoming)
            scores[i, j] = incoming[index]
    return scores[n-1, m-1]

def edit_distance(seq1, seq2):
    """ returns the edit distance
    Code from CSCI321 Spring 17 Professor Linderman """

    NUCLEOTIDES = "ACTG"
    edit_distance_matrix = {}
    for key in product(NUCLEOTIDES, NUCLEOTIDES):
        if key[0] == key[1]:
            # Matches have 0 edits
            edit_distance_matrix[key] = 0
        else:
            # Everything else is -1
            edit_distance_matrix[key] = -1
    score = global_alignment(seq1, seq2, edit_distance_matrix, -1)

    return -score

if __name__ == '__main__':
    print("run other file")
