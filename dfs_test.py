import unittest
from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced
from BalDBToAllECycles import get_all_e_cycles

class TestDFS(unittest.TestCase):

    def test_one_path(self):
        k = 3
        d = 1
        filename = "SampleGenome.txt"

        read_pairs = make_read_pairs(filename, k, d)

        overlap = make_overlap(read_pairs)

        DB = make_DB(read_pairs, overlap)

        degree_dict = get_degrees(DB)

        balanced_DB = make_balanced(DB, degree_dict)

        all_cycles = get_all_e_cycles(DB)

    # def test_2_distinct_paths(self):
    #
    #
    #
    # def test_2_paths_1_distinct(self):

if __name__ == "__main__":
    unittest.main()
