""" Jen Johnson
CSCI 321 Spring 17 Final Project
Calls Euler Cycle on balanced paired DB graph """

from GenomeToReads import make_read_pairs, kmer_node
from ReadsToDBGraph import make_overlap, make_DB
from DBGraphToBalDBGraph import get_degrees, make_balanced

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    degree_dict = get_degrees(DB)

    balanced_DB = make_balanced(DB, degree_dict)

    # for i in range(0, len(balanced_DB)):
    #     print("entry")
    #     current = balanced_DB[i]
    #     print(current.kmer_node.first +"\t"+ current.kmer_node.second)
    #     print("followers " + str(len(current.followers)))
    #     for current in current.followers:
    #         print(current.first +"\t"+ current.second)


if __name__ == "__main__":
    main()
