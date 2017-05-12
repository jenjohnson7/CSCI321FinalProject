""" Jen Johnson
CSCI 321 Spring 17 Final Project
Paired DeBruijn Graph to reconstruct Salmonella Genome """

from GenomeToReadPairs import make_read_pairs, Kmer_Node
from ReadPairsToDBGraph import make_overlap, make_DB, DB_Node

def get_degrees(DB):
    """ given input as a list of db_nodes, returns the degrees as a dictionary
    used to make DB balanced """

    degree_dict = dict()

    # outdegrees
    for node in DB:
        degree_dict[node] = len(node.followers)

    # indegrees
    for node in DB:
        for follower in node.followers:
            current = degree_dict[follower]
            current += 1
            degree_dict[follower] = current

    return degree_dict

def genome_to_contigs(k, d, filename):
    """ gets contigs of length k from filename """

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    # print(len(DB))
    # for node in DB:
    #     print("entry")
    #     print(node.kmer_node.first + "|" + node.kmer_node.second)
    #     print("followers")
    #     for x in node.followers:
    #         print(x.first + "|" + x.second)

    degree_dict = get_degrees(DB)

    # paths = maximum_nonbranching_path(DB, outgoing, incoming)

    contigs = []

    # for path in paths:
    #     contigs.append(string_construct(path))

    return contigs

def main():
    filename = "SampleGenome.txt"

    k = 3
    d = 1

    contigs = genome_to_contigs(k, d, filename)

    # print("num contigs")
    # print(len(contigs))
    # print("len of each contig")
    # for contig in contigs:
    #     print(len(contig))

if __name__ == "__main__":
    main()
