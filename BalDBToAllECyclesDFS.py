""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all ECycles """

from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced

def kmer_node_to_db_node(kmer_node, DB):
    """ searches through DB to find db_node == kmer_node
    returns db_node """

    for db_node in DB:
        if db_node.kmer_node == kmer_node:
            return db_node

def depth_first_search(DB, db_start, kmer_start, visited, current_cycle, all_cycles, stack):
    """ calls depth first search """

    while len(stack)!=0:

        current_kmer = stack.pop()
        # print(current_kmer)
        current_db = kmer_node_to_db_node(current_kmer, DB)

        for follower in current_db.followers:
            stack.append(follower)

def get_all_e_cycles(DB):
    """ runs DFS to find all Eulerean cycles in a balanced/cyclic DB"""

    all_cycles = []

    db_start = DB[0]
    kmer_start = db_start.kmer_node

    visited = dict()
    # visited contains kmer_nodes
    for node in DB:
        visited[node.kmer_node] = False
    visited[kmer_start] = True

    current_cycle = []
    current_cycle.append(db_start)
    #cycles contain db_nodes

    stack = [] #contains kmer_nodes
    stack.append(kmer_start)

    depth_first_search(DB, db_start, kmer_start, visited, current_cycle, all_cycles, stack)

    return all_cycles

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    degree_dict = get_degrees(DB)

    balanced_DB = make_balanced(DB, degree_dict)

    for i in range(0, len(balanced_DB)):
        print("entry")
        current = balanced_DB[i]
        print(current.kmer_node.first +"\t"+ current.kmer_node.second)
        print("followers " + str(len(current.followers)))
        for current in current.followers:
            print(current.first +"\t"+ current.second)

    all_cycles = get_all_e_cycles(DB)

    # print("final result")
    # for cycle in all_cycles:
    #     print("new_cycle")
    #     for node in cycle:
    #         print(node)

if __name__ == "__main__":
    main()
