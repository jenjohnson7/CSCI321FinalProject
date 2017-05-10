import unittest
from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced
from BalDBToAllECycles import dfs_all_cycles, get_num_edges
from AllECyclesToAllPaths import cycle_to_path
from AllPathsToGenomes import filter_paths

class TestECycles(unittest.TestCase):
    # def test_1_path(self):
    #     print("test 1")
    #     k = 3
    #     d = 1
    #     filename = "SampleGenome.txt"
    #     read_pairs = make_read_pairs(filename, k, d)
    #     overlap = make_overlap(read_pairs)
    #     DB = make_DB(read_pairs, overlap)
    #     degree_dict = get_degrees(DB)
    #     balanced_DB, outdegree, indegree, unbalanced = make_balanced(DB, degree_dict)
    #     num_edges = get_num_edges(balanced_DB)
    #
    #     all_cycles = dfs_all_cycles(balanced_DB, num_edges)
    #
    #     all_paths = cycle_to_path(all_cycles, outdegree, indegree, unbalanced)
    #
    #     genomes = filter_paths(all_paths, k, d)

    # def test_2_distinct_paths(self):
    #     print("test 2")
    #     test_DB = []
    #     A_kmer = Kmer_Node("A", "A")
    #     B_kmer = Kmer_Node("B", "B")
    #     C_kmer = Kmer_Node("C", "C")
    #     D_kmer = Kmer_Node("D", "D")
    #     A_db = DB_Node(A_kmer, [B_kmer, B_kmer])
    #     test_DB.append(A_db)
    #     B_db = DB_Node(B_kmer, [C_kmer, D_kmer])
    #     test_DB.append(B_db)
    #     C_db = DB_Node(C_kmer, [A_kmer])
    #     test_DB.append(C_db)
    #     D_db = DB_Node(D_kmer, [A_kmer])
    #     test_DB.append(D_db)
    #
    #     num_edges = get_num_edges(test_DB)
    #     degree_dict = get_degrees(test_DB)

        # all_cycles = dfs_all_cycles(test_DB, num_edges)

        # for cycle in all_cycles:
        #     print("cycle")
        #     for node in cycle:
        #         print(node)

    def test_2_paths_1_distinct(self):
        print("test 3")
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

        num_edges = get_num_edges(test_DB)
        degree_dict = get_degrees(test_DB)

        all_cycles = dfs_all_cycles(test_DB, num_edges)

        for cycle in all_cycles:
            print("cycle")
            for node in cycle:
                print(node)

if __name__ == "__main__":
    unittest.main()
