""" Jen Johnson
CSCI 321 Spring 17 Final Project
Produce contigs from paired reads """

from GenomeToReadPairs import make_read_pairs, Kmer_Node
from ReadPairsToDBGraph import make_DB, find_last, DB_Node
from DBGraphToContigs import make_contigs, kmer_node_to_db_node

def get_indegrees(DB):
    """ given input as a list of db_nodes, updates db_node.num_incoming property """

    for node in DB:
        for kmer_follower in node.followers:
            db_follower = kmer_node_to_db_node(kmer_follower, DB)
            db_follower.num_incoming+=1

def genome_to_paired_contigs(k, d, filename):
    """ gets contigs of paired De Bruijn graph
    from read pairs of length 2k+d
    from filename containing genome """

    read_pairs = make_read_pairs(filename, k, d)
    print("made paired read pairs")

    last = find_last(read_pairs)

    DB = make_DB(read_pairs, last)
    print("made paired DB")

    get_indegrees(DB)

    contigs = make_contigs(DB)
    print("made paired contigs")

    return contigs

def main():
    filename = "SampleGenome.txt"

    k = 3
    d = 1

    contigs = genome_to_paired_contigs(k, d, filename)

    print("num contigs")
    print(len(contigs))
    print("len of each contig")
    for contig in contigs:
        print(len(contig))

if __name__ == "__main__":
    main()
