""" Jen Johnson
CSCI 321 Spring 17 Final Project
Create a Paired DB Graph from paired reads """

from GenomeToReads import make_read_pairs
from collections import OrderedDict

def make_overlap(read_pairs):
    """ from input of read_pairs in the form of a list of nodes
        returns an overlap graph in the form of an adj list
        where i-->j where the suffix of both reads in i == prefix of both reads in j"""

    result = []

    for i in range (0, len(read_pairs)):
        first_suffix = read_pairs[i].first[1:]
        second_suffix = read_pairs[i].second[1:]
        followers = []
        for j in range (0, len(read_pairs)):
            first_prefix = read_pairs[j].first[:-1]
            second_prefix = read_pairs[j].second[:-1]
            if first_suffix == first_prefix and second_suffix == second_prefix:
                followers.append(read_pairs[j])
        result.append(followers)
    return result

def make_DB(read_pairs, overlap):
    """ turns an overlap graph into DB graph by gluing identical nodes"""
    result = OrderedDict()

    for i in range (0, len(overlap)):
        if result.has_key(read_pairs[i]):
            current_followers_set = set(result[overlap[i]])
            for j in range (0, len(overlap[i])):
                current_followers_set.add(overlap[i][j])
            result[read_pairs[i]] = current_followers_set
        else:
            current_followers_set = set(overlap[i])
            result[read_pairs[i]] = current_followers_set
    return result

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    # for i in range (0, len(overlap)):
    #     print("entry")
    #     print(read_pairs[i].first + "\t" + read_pairs[i].second)
    #     print("list:")
    #     for j in range (0, len(overlap[i])):
    #         print(overlap[i][j].first + "\t" + overlap[i][j].second + "\n")

    DB = make_DB(read_pairs, overlap)

if __name__ == "__main__":
    main()
