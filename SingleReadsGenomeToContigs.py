""" Jen Johnson
CSCI 321 Spring 17 Final Project
Genome-->Single Reads-->DBGraph-->Contigs
code take from previous Rosalind problems for Chapter 3 """

def make_reads(filename, k):
    """ produces kmers from a file
    where the entire genome is not on one line """

    num_lines = sum(1 for line in open(filename))
    genome = ""

    f = open(filename)

    # make the full genome string
    for x in range (0, num_lines):
        genome += next(f).strip()

    kmers = []

    # splice to get each kmer
    for i in range (0, len(genome)-k+1):
        node = genome[i:i+k]
        kmers.append(node)

    f.close()

    return kmers

def kmer_DBGraph(kmers):
    """  makes a dictionary where key == prefix, and value == suffix
    combines overlap graph and db graph steps into one """

    result_dict = dict()

    for i in range (0, len(kmers)):
        prefix_key = kmers[i][:-1]
        suffix_value = kmers[i][1:]
        if prefix_key not in result_dict:
            result_dict[prefix_key] = [suffix_value]
        else: #already in dict, update
            existing_suffix = result_dict[prefix_key]
            temp = existing_suffix + [suffix_value]
            result_dict[prefix_key] = temp

    return result_dict

def get_degrees(db_graph):
    """ returns two dictionaries where keys = nodes, values = out or indegrees """

    outdegrees = {}
    indegrees = {}

    #getting the outdegrees
    for entry in db_graph:
        outdegrees[entry]=len(db_graph[entry])

    #getting the indegrees
    for entry in db_graph:
        for follower in db_graph[entry]:
            if follower in indegrees:
                indegrees[follower]+=1
            else:
                indegrees[follower]=1

    #make sure all nodes are in both dictionaries to prevent key errors
    indegree_keys = indegrees.keys()
    outdegree_keys = outdegrees.keys()

    for key in indegree_keys:
        if key not in outdegrees:
            outdegrees[key]=0
    for key in outdegree_keys:
        if key not in indegrees:
            indegrees[key]=0

    return outdegrees, indegrees

def get_contigs(db_graph, outgoing, incoming):
    """ finds the collection of contigs in a Db graph
    db_graph is n an adjacency list
    returns contigs as an array of an array of nodes """

    keys = db_graph.keys()
    paths = []

    for entry in keys:
        #if NOT a 1-in-1-out node...
        if outgoing[entry]!=1 or incoming[entry]!=1:
            # and it has a follower...
            if outgoing[entry]>0:
                # go through these followers...
                for follower in db_graph[entry]:
                    # start a contig
                    current_path = [entry, follower]
                    # extend the contig if followers are 1-in-1-out
                    current_node = follower
                    while outgoing[current_node]==1 and incoming[current_node]==1:
                        #update the current node
                        #always be the first and only follower of current_node
                        #[0] because you need an int, not a list
                        current_node = db_graph[current_node][0]
                        current_path.append(current_node)
                    paths.append(current_path)

    return paths

def string_construct(kmers):
    """ given an array of sorted overlapping nodes
    returns the string by adding the last char of each kmer """

    result = kmers[0]
    for i in range (1, len(kmers)):
        result += kmers[i][-1]
    return result

def genome_to_single_contigs(k, filename):
    """ gets contigs of De Bruijn graph
    from reads of length k
    from filename containing genome """

    reads = make_reads(filename, k)
    print("made single reads")

    db_graph = kmer_DBGraph(reads)
    print("made single DB")

    outgoing, incoming = get_degrees(db_graph)

    paths = get_contigs(db_graph, outgoing, incoming)
    print("made single contigs")

    contigs = []

    for path in paths:
        contigs.append(string_construct(path))

    return contigs

def main():
    k = 3
    filename = "SampleGenome.txt"

    contigs = genome_to_single_contigs(k, filename)

    print("num contigs")
    print(len(contigs))
    print("len of each contig")
    for contig in contigs:
        print(len(contig))
        # print(contig)

if __name__ == "__main__":
    main()
