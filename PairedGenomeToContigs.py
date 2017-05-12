""" Jen Johnson
CSCI 321 Spring 17 Final Project
Paired DeBruijn Graph to reconstruct Salmonella Genome """

from GenomeToReadPairs import make_read_pairs, Kmer_Node
from ReadPairsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToContigs import make_contigs, kmer_node_to_db_node

def get_indegrees(DB):
    """ given input as a list of db_nodes, updates db_node.num_incoming property """

    for node in DB:
        for kmer_follower in node.followers:
            db_follower = kmer_node_to_db_node(kmer_follower, DB)
            db_follower.num_incoming+=1

def genome_to_contigs(k, d, filename):
    """ gets contigs of paired De Bruijn graph
    from read pairs of length 2k+d
    from filename containing genome """

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    get_indegrees(DB)

    contigs = make_contigs(DB)

    return contigs

def main():
    filename = "SampleGenome.txt"

    k = 3
    d = 1

    contigs = genome_to_contigs(k, d, filename)

    print("num contigs")
    print(len(contigs))
    print("len of each contig")
    for contig in contigs:
        print(len(contig))

if __name__ == "__main__":
    main()
