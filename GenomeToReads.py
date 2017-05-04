""" Jen Johnson
CSCI 321 Spring 17 Final Project
Make k, d mers from a genome """

class kmer_node():
    """ type for holding the kmers """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return str(self.first + self.second)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

def make_read_pairs(filename, k, d):
    """ makes each k,d mer into a node
        returns a list of nodes """

    f = open(filename)

    genome = next(f).strip()

    kmers = []

    for i in range (0, len(genome)-(2*k+d)+1):
        first = genome[i:i+k]
        second = genome[i+k+d:i+2*k+d]
        node = kmer_node(first, second)
        kmers.append(node)

    sorted_pairs = sorted(kmers, key = lambda node: node.first)
    return sorted_pairs

def main():

    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

if __name__ == "__main__":
    main()
