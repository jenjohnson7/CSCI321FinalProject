""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all ECycles """

from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced

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

def get_num_edges(DB):
    """ returns the number of edges in the graph """
    num_edges = 0
    for i in range (0, len(DB)):
        num_edges += len(DB[i].followers)

    return num_edges

def kmer_node_to_db_node(kmer_node, DB):
    """ searches through DB to find db_node == kmer_node
    returns db_node """

    for db_node in DB:
        if db_node.kmer_node == kmer_node:
            return db_node

def get_all_graphs(DB, incoming):
    """ makes all simple graphs in DB """

    all_graphs = []
    all_graphs.append(DB)

    seen_and_complex = []
    for kmer_node in incoming:
        if len(incoming[kmer_node])>=3:
            seen_and_complex.append(kmer_node)

    for kmer_node in seen_and_complex:
        for incoming_node in incoming[kmer_node]:
            DB_current = kmer_node_to_db_node(kmer_node, DB)
            for outgoing_node in DB_current.followers:
                temp_graphs = []
                for graph in all_graphs:
                    new_graph = make_new_graph(incoming_node, outgoing_node, DB_current, graph)
                    temp_graphs.append(new_graph)
                    all_graphs.remove(graph)
                    all_graphs +=temp_graphs

    print("len " + str(len(all_graphs)))

    for graph in all_graphs:
        print("graph")
        for entry in graph:
            print("entry " + str(entry))
            for node in entry.followers:
                print("follower " + str(node))

    return all_graphs

def make_new_graph(incoming_node, outgoing_node, current_DB, current_graph):
    """ modifies the current complex graph into a simple graph
    incoming node is a db node
    outgoing node is a kmer node """

    result = current_graph

    kmer_temp = current_DB.kmer_node

    for db_node in current_graph:
        # print(db_node)
        if db_node == current_DB:
            if outgoing_node in db_node.followers:
                db_node.followers.remove(outgoing_node)
        if db_node == incoming_node:
            db_node.followers.append(kmer_temp)

    DB_temp = DB_Node(kmer_temp, [outgoing_node])

    result.append(DB_temp)
    return result

def get_e_cycles(all_graphs, incoming):
    """ uses num_edges to find a Eulerean cycle in DB
    uses incoming to find all cycles in DB """

    all_cycles = []

    for graph in all_graphs:

        num_edges = get_num_edges(graph)

        path = []
        seen_edges = 0
        seen_and_extra_edges = []

        current_db = graph[0]
        current_kmer = current_db.kmer_node

        while seen_edges != num_edges:
            if len(current_db.followers) !=0:
                path.append(current_db)
                next_kmer = current_db.followers[0]
                current_db.followers.remove(next_kmer)
                if len(current_db.followers) !=0:
                    seen_and_extra_edges.append(current_db)
                seen_edges+=1
                current_db = kmer_node_to_db_node(next_kmer, graph)
            else:
                current_db = seen_and_extra_edges[0]
                seen_and_extra_edges.remove(current_db)

                temp_path = []
                new_start = path.index(current_db)
                temp_path = path[new_start:]
                temp_path += path[:new_start]
                path = temp_path

        source = path[0]
        path+=[source]

    if path not in all_cycles:
        all_cycles.append(path)

    return all_cycles

def main():
    print("run the other file!!!")

if __name__ == "__main__":
    main()
