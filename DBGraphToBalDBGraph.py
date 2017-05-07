""" Jen Johnson
CSCI 321 Spring 17 Final Project
Turns a paired DB graph into a balanced paired DB graph """

from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB

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

def make_balanced(DB, degree_dict):
    """ input is a list of db_nodes sorted lexicographically by first read in pair
    each node has kmer_node and a follower list of kmer_nodes
    makes the DB graph balanced """

    unbalanced = []
    outdegree = []
    indegree = []

    # find the unbalanced nodes and figure out where the edge should go
    for i in range (0, len(DB)):
        node = DB[i]
        if degree_dict[node]%2==1:
            unbalanced.append(node)
            current_outdegree = len(node.followers)
            outdegree.append(current_outdegree)
            indegree.append(degree_dict[node]-current_outdegree)

    source, sink = -1, -1

    if outdegree[0] < indegree[1]:
        source = unbalanced[0]
        sink = unbalanced[1]
    else:
        source = unbalanced[1]
        sink = unbalanced[0]

    # insert the new edge as a kmer_node in the source's list of followers
    first = sink.kmer_node.first
    second = sink.kmer_node.second
    new_sink = Kmer_Node(first, second)

    index = DB.index(source)
    DB[index].followers.append(new_sink)

    return DB

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    # for i in range(0, len(DB)):
    #     print("entry")
    #     current = DB[i]
    #     print(current.kmer_node.first +"\t"+ current.kmer_node.second)
    #     print("followers " + str(len(current.followers)))
    #     for current in current.followers:
    #         print(current.first +"\t"+ current.second)

    degree_dict = get_degrees(DB)

    # for entry in degree_dict:
    #     print(entry.kmer_node.first + "\t" + entry.kmer_node.second)
    #     print(degree_dict[entry])

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
