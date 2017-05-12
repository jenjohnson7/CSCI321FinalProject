""" Jen Johnson
CSCI 321 Spring 17 Final Project
Paired DeBruijn Graph to reconstruct Salmonella Genome """

from GenomeToReadPairs import make_read_pairs, Kmer_Node
from ReadPairsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced
from BalDBToAllECycles import dfs_all_cycles, get_num_edges
from AllECyclesToAllPaths import cycle_to_path
from AllPathsToGenomes import filter_paths
from editDistance import edit_distance

def main():
    filename = "Salmonella-bongori.txt"

    # k = 100
    # d = 1

    read_pairs, first_genome = make_read_pairs(filename, k, d)
    overlap = make_overlap(read_pairs)
    DB = make_DB(read_pairs, overlap)
    degree_dict = get_degrees(DB)
    balanced_DB, outdegree, indegree, unbalanced = make_balanced(DB, degree_dict)
    num_edges = get_num_edges(balanced_DB)
    all_cycles = dfs_all_cycles(balanced_DB, num_edges)
    all_paths = cycle_to_path(all_cycles, outdegree, indegree, unbalanced)
    genomes = filter_paths(all_paths, k, d)

    success = []
    for genome in genomes:
        result = edit_distance(genome, first_genome)
        success.append(result)

    for value in success:
        print(value)

if __name__ == "__main__":
    main()
