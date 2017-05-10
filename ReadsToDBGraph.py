""" Jen Johnson
CSCI 321 Spring 17 Final Project
Create a Paired DB Graph from paired reads """

from GenomeToReads import make_read_pairs, Kmer_Node

class DB_Node():
    """ type for holding k-1-mers and follower list """
    def __init__(self, kmer_node, followers):
        self.kmer_node = kmer_node
        self.followers = followers

    def __str__(self):
        return str(self.kmer_node.first + self.kmer_node.second)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

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
            # if prefix == suffix for both first and second, the nodes are adj
            first_prefix = read_pairs[j].first[:-1]
            second_prefix = read_pairs[j].second[:-1]
            if first_suffix == first_prefix and second_suffix == second_prefix:
                followers.append(read_pairs[j])

        result.append(followers)

    return result

def make_DB(read_pairs, overlap):
    """ turns an overlap graph into DB graph
    stores kmer_nodes in db_nodes with list of followers (kmer_nodes) """

    result = []
    keys = []

    for i in range (0, len(read_pairs)):

        first_prefix = read_pairs[i].first[:-1]
        second_prefix = read_pairs[i].second[:-1]
        key_node = Kmer_Node(first_prefix, second_prefix)

        followers = []

        if len(overlap[i])==0:
            # the last node 
            first_suffix = read_pairs[i].first[1:]
            second_suffix = read_pairs[i].second[1:]
            final = Kmer_Node(first_suffix, second_suffix)
            followers.append(final)

        for j in range (0, len(overlap[i])):
            current_first = overlap[i][j].first[:-1]
            current_second = overlap[i][j].second[:-1]
            current_node = Kmer_Node(current_first, current_second)

            if current_node not in followers:
                followers.append(current_node)

        if key_node not in keys:
            entry_node = DB_Node(key_node, followers)
            result.append(entry_node)
            keys.append(key_node)
        else:
            # if already seen, update the existing entry
            new_entry = DB_Node(key_node, followers)
            index = result.index(str(new_entry))
            previous_followers = result[index].followers
            current_followers = new_entry.followers
            total_followers = previous_followers + current_followers
            result[index].followers = total_followers

    last_node = DB_Node(final, [])
    result.append(last_node)

    return result

def main():
    k = 3
    d = 1
    filename = "SampleGenome.txt"

    read_pairs = make_read_pairs(filename, k, d)

    overlap = make_overlap(read_pairs)

    DB = make_DB(read_pairs, overlap)

if __name__ == "__main__":
    main()
