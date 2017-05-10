""" Jen Johnson
CSCI 321 Spring 17 Final Project
Turns a paired DB graph into a balanced paired DB graph """

from GenomeToReadPairs import make_read_pairs, Kmer_Node
from ReadPairsToDBGraph import make_overlap, make_DB

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
    makes the DB graph balanced
    returns the data structures used so that they don't have to be recalculated
    when removing the edge """

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

    return DB, outdegree, indegree, unbalanced

def main():
    print("running")
if __name__ == "__main__":
    main()
