import unittest
from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced
from BalDBToAllECyclesEdges import get_all_e_cycles, get_num_edges

class TestDFS(unittest.TestCase):

    def test_one_path(self):
        k = 3
        d = 1
        filename = "SampleGenome.txt"

        read_pairs = make_read_pairs(filename, k, d)

        overlap = make_overlap(read_pairs)

        DB = make_DB(read_pairs, overlap)

        degree_dict = get_degrees(DB)
        num_edges = get_num_edges(DB)

        balanced_DB = make_balanced(DB, degree_dict)

        all_cycles = get_all_e_cycles(balanced_DB, num_edges)

        # for node in all_cycles:
        #     print(node)

    def test_2_distinct_paths(self):

        test_DB = []
        A_kmer = Kmer_Node("A", "A")
        B_kmer = Kmer_Node("B", "B")
        C_kmer = Kmer_Node("C", "C")
        D_kmer = Kmer_Node("D", "D")
        A_db = DB_Node(A_kmer, [B_kmer, B_kmer])
        test_DB.append(A_db)
        B_db = DB_Node(B_kmer, [C_kmer, D_kmer])
        test_DB.append(B_db)
        C_db = DB_Node(C_kmer, [A_kmer])
        test_DB.append(C_db)
        D_db = DB_Node(D_kmer, [A_kmer])
        test_DB.append(D_db)

        # for i in range(0, len(test_DB)):
        #     print("entry")
        #     current = test_DB[i]
        #     print(current.kmer_node.first +"\t"+ current.kmer_node.second)
        #     print("followers " + str(len(current.followers)))
        #     for current in current.followers:
        #         print(current.first +"\t"+ current.second)

        num_edges = get_num_edges(test_DB)
        all_cycles = get_all_e_cycles(test_DB, num_edges)

        # for node in all_cycles:
        #     print(node)

    def test_2_paths_1_distinct(self):
        test_DB = []
        A_kmer = Kmer_Node("A", "A")
        B_kmer = Kmer_Node("B", "B")
        C_kmer = Kmer_Node("C", "C")
        D_kmer = Kmer_Node("D", "D")
        A_db = DB_Node(A_kmer, [B_kmer, B_kmer, B_kmer])
        test_DB.append(A_db)
        B_db = DB_Node(B_kmer, [C_kmer, D_kmer, A_kmer])
        test_DB.append(B_db)
        C_db = DB_Node(C_kmer, [A_kmer])
        test_DB.append(C_db)
        D_db = DB_Node(D_kmer, [A_kmer])
        test_DB.append(D_db)

        test_degree_dict = get_degrees(test_DB)
        num_edges = get_num_edges(test_DB)

        all_cycles = get_all_e_cycles(test_DB, num_edges)

        for node in all_cycles:
            print(node)
if __name__ == "__main__":
    unittest.main()
