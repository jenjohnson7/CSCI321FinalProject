""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all simple DB graphs """

from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced

def is_simple(graph):
    """ returns True if all nodes in graph have indegree == outdegree == 1 """

    # CHECK THIS

    degree_dict = get_degrees(graph)

    for node in graph:
        outdegree = len(node.followers)
        indegree = degree_dict[node]-outdegree
        if outdegree != 1 or indegree !=1:
            return False

    return True

def are_simple(graphs):
    """ given a list of graphs
    returns True if they are all simple
    returns False complex graph exists """

    #CHECK THIS

    for graph in graphs:
        if not is_simple(graph):
            return False

    return True

def get_complex_graph(graphs):
    """ given a list of graphs
    returns True if they are all simple
    returns False complex graph exists """

    # CHECK THIS. combine with are_simple?

    for graph in graphs:
        if not is_simple(graph):
            return graph

def construct_incoming(graph):
    """ given a graph
    goes through the list of followers and constructs a dictionary of incoming nodes
    where keys are kmer_nodes
    and values are lists of db_nodes """

    result = dict()

    for node in graph:
        for follower in node.followers:
            if follower in result:
                temp = result[follower]
                temp.append(node)
                result[follower] = temp
            else:
                result[follower] = [node]

    return result

def get_complex_node(graph, incoming):
    for kmer_node in incoming:
        if len(incoming[kmer_node]) >1:
            for db_node in graph:
                if kmer_node == db_node.kmer_node:
                    return kmer_node, db_node

def make_new_graph(incoming_node, outgoing_node, current_db, current_graph):
    """ modifies the current complex graph into a simple graph
    incoming node is a db node
    outgoing node is a kmer node """

    result = current_graph

    kmer_temp = Kmer_Node(1, 1)

    for db_node in current_graph:
        # print(db_node)
        if db_node.kmer_node == current_db.kmer_node:
            # print(current_db)
            # print(type(incoming_node.kmer_node))
            # for x in current_db.followers:
            #     print(x)
            # print(type(current_db.followers[0]))
            current_db.followers.remove(outgoing_node)
        if db_node == incoming_node:
            db_node.followers.append(kmer_temp)

    DB_temp = DB_Node(kmer_temp, [outgoing_node])

    result.append(DB_temp)

    return result

def get_all_graphs(DB):
    """ returns an array of all simple DB graphs
    each DB graph is an array of db_nodes """

    result = []
    result.append(DB)

    while not are_simple(result):
        current_graph = get_complex_graph(result)
        incoming = construct_incoming(current_graph)
        current_kmer, current_db = get_complex_node(current_graph, incoming)
        for incoming_node in incoming[current_kmer]:
            for outgoing_node in current_db.followers:
                    new_graph = make_new_graph(incoming_node, outgoing_node, current_db, current_graph)
                    # if connected ???
                    result.append(new_graph)

        result.remove(current_graph)

    return result

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    degree_dict = get_degrees(DB)

    balanced_DB = make_balanced(DB, degree_dict)

    # for i in range(0, len(balanced_DB)):
    #     print("entry")
    #     current = balanced_DB[i]
    #     print(current.kmer_node.first +"\t"+ current.kmer_node.second)
    #     print("followers " + str(len(current.followers)))
    #     for current in current.followers:
    #         print(current.first +"\t"+ current.second)

    all_DB = get_all_graphs(DB)

    # for i in range (0, len(all_DB)):
    #     for i in range(0, len(balanced_DB)):
    #         print("entry")
    #         current = balanced_DB[i]
    #         print(current.kmer_node.first +"\t"+ current.kmer_node.second)
    #         print("followers " + str(len(current.followers)))
    #         for current in current.followers:
    #             print(current.first +"\t"+ current.second)

if __name__ == "__main__":
    main()
