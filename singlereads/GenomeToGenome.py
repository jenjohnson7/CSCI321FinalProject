""" Jen Johnson
CSCI 321 Spring 17 Final Project
Genome-->Single Reads-->DBGraph-->ECycle-->EPath-->Genome """

from kmerDBGraph import kmer_DBGraph
from EPath import E_Path, make_degree_dict
from stringConstruct import string_construct

def make_reads(filename, k):
    """ makes each k,d mer into a node
        returns a list of nodes """

    num_lines = sum(1 for line in open(filename))-1

    f = open(filename)
    genome = next(f).strip()
    kmers = []
    for i in range (0, len(genome)-k+1):
        node = genome[i:i+k]
        kmers.append(node)

    f.close()

    return kmers, num_lines

def get_path(reads, num_lines):
    """ single reads to EPath """

    result, keys = kmer_DBGraph(reads)

    num_edges = 0
    for entry in result:
        num_edges+=len(result[entry])

    #get the degrees
    degree_dict = {}
    degree_dict = make_degree_dict(result, degree_dict)

    #call E_Path
    ordered_kmers = E_Path(degree_dict, result, num_edges, num_lines)

    final_path = string_construct(ordered_kmers)

    return final_path

def main():
    k = 3
    filename = "SampleGenome.txt"

    reads, num_lines = make_reads(filename, k)

    path = get_path(reads, num_lines)

    print(path)

if __name__ == "__main__":
    main()
