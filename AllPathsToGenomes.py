""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all possible Genome Paths """

def compare_strings(path, genomes, k, d):
    """ constructs and compares prefix and suffix strings of the path """
    prefix_string = ""
    suffix_string = ""

    # construct
    for node in path:
        prefix_string+=node.kmer_node.first[0]
        suffix_string+=node.kmer_node.second[-1]

    # compare
    for i, j in zip(range (k+d+1, len(prefix_string)), range(0, len(suffix_string)-k-d-1)):
        if prefix_string[i]!=suffix_string[j]:
            return

    # add the final result to genomes
    final_string = prefix_string
    final_string +=suffix_string[-(k+d+1):]
    genomes.append(final_string)

def filter_paths(all_paths, k, d):
    """ for each path in all paths, calls compare_strings """

    genomes = []

    for path in all_paths:
        compare_strings(path, genomes, k, d)

    return genomes

def main():
    print("run the other file!!!")

if __name__ == "__main__":
    main()
