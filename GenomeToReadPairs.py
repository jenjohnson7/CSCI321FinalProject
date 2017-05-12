""" Jen Johnson
CSCI 321 Spring 17 Final Project
Make k, d mers from a genome """

class Kmer_Node():
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

    num_lines = sum(1 for line in open(filename))
    genome = ""

    f = open(filename)

    # make the full genome string
    for x in range (0, num_lines):
        genome += next(f).strip()

    kmers = []

    for i in range (0, len(genome)-(2*k+d)+1):
        # splice into nodes
        first = genome[i:i+k]
        second = genome[i+k+d:i+2*k+d]
        node = Kmer_Node(first, second)
        kmers.append(node)

    # sort by the first node
    sorted_pairs = sorted(kmers, key = lambda node: node.first)

    f.close()

    return sorted_pairs

def main():
    print("running")

if __name__ == "__main__":
    main()
