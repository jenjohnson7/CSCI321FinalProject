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

def get_num_edges(DB):
    """ returns the number of edges in the graph """

    num_edges = 0
    for node in DB:
        num_edges += len(node.followers)

    return num_edges

def get_all_e_cycles(DB, num_edges):
    """ uses edges to find Eulerean cycle in a balanced/cyclic DB"""

    all_cycles = []

    path = []
    seen_edges = 0
    seen_and_extra_edges = []

    current_db = DB[0]
    current_kmer = current_db.kmer_node

    while seen_edges != num_edges:
        if len(current_db.followers) !=0:
            path.append(current_db)
            next_kmer = current_db.followers[0]
            current_db.followers.remove(next_kmer)
            if len(current_db.followers) !=0:
                seen_and_extra_edges.append(current_db)
            seen_edges+=1
            current_db = kmer_node_to_db_node(next_kmer, DB)
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
    return path

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

    degree_dict = get_degrees(DB)
    num_edges = get_num_edges(DB)

    balanced_DB = make_balanced(DB, degree_dict)

    # for i in range(0, len(balanced_DB)):
    #     print("entry")
    #     current = balanced_DB[i]
    #     print(current.kmer_node.first +"\t"+ current.kmer_node.second)
    #     print("followers " + str(len(current.followers)))
    #     for current in current.followers:
    #         print(current.first +"\t"+ current.second)

# __________________TEST CASE 1 distinct path
    # all_cycles = get_all_e_cycles(balanced_DB, num_edges)

    # for node in all_cycles:
    #     print(node)

# __________________TEST CASE 2 paths 1 distinct

    # test_DB = []
    # A_kmer = Kmer_Node("A", "A")
    # B_kmer = Kmer_Node("B", "B")
    # C_kmer = Kmer_Node("C", "C")
    # D_kmer = Kmer_Node("D", "D")
    # A_db = DB_Node(A_kmer, [B_kmer, B_kmer])
    # test_DB.append(A_db)
    # B_db = DB_Node(B_kmer, [C_kmer, D_kmer])
    # test_DB.append(B_db)
    # C_db = DB_Node(C_kmer, [A_kmer])
    # test_DB.append(C_db)
    # D_db = DB_Node(D_kmer, [A_kmer])
    # test_DB.append(D_db)

    # for i in range(0, len(test_DB)):
    #     print("entry")
    #     current = test_DB[i]
    #     print(current.kmer_node.first +"\t"+ current.kmer_node.second)
    #     print("followers " + str(len(current.followers)))
    #     for current in current.followers:
    #         print(current.first +"\t"+ current.second)

    # num_edges = get_num_edges(test_DB)
    # all_cycles = get_all_e_cycles(test_DB, num_edges)
    #
    # for node in all_cycles:
    #     print(node)

# __________________TEST CASE 2 distinct paths
    # test_DB = []
    # A_kmer = Kmer_Node("A", "A")
    # B_kmer = Kmer_Node("B", "B")
    # C_kmer = Kmer_Node("C", "C")
    # D_kmer = Kmer_Node("D", "D")
    # A_db = DB_Node(A_kmer, [B_kmer, B_kmer, B_kmer])
    # test_DB.append(A_db)
    # B_db = DB_Node(B_kmer, [C_kmer, D_kmer, A_kmer])
    # test_DB.append(B_db)
    # C_db = DB_Node(C_kmer, [A_kmer])
    # test_DB.append(C_db)
    # D_db = DB_Node(D_kmer, [A_kmer])
    # test_DB.append(D_db)
    #
    # test_degree_dict = get_degrees(test_DB)
    # num_edges = get_num_edges(test_DB)
    #
    # all_cycles = get_all_e_cycles(test_DB, num_edges)

if __name__ == "__main__":
    main()
