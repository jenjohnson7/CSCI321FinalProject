""" Jen Johnson
CSCI 321 Spring 17 Final Project
Create a Paired DB Graph from paired reads """

from GenomeToReadPairs import make_read_pairs, Kmer_Node

class DB_Node():
    """ type for holding k-1-mers and follower list """
    def __init__(self, kmer_node, followers, num_incoming):
        self.kmer_node = kmer_node
        self.followers = followers
        self.num_incoming = num_incoming

    def __str__(self):
        return str(self.kmer_node.first + self.kmer_node.second)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

def find_last(read_pairs):
    """ makes overlap graph using kmers to find the last node with no followers
    needed to add the last node to the DB graph """

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

    final_result = 0
    for i in range (0, len(result)):
        if len(result[i])==0:
            final_result = read_pairs[i]

    return final_result

def make_DB(read_pairs, last):
    """ turns read_pairs into a paired DB graph
    stores kmer_nodes in db_nodes with list of followers (kmer_nodes) """

    result = [] # holds db_nodes
    keys = [] # holds kmer_nodes

    for i in range (0, len(read_pairs)):
        first_prefix = read_pairs[i].first[:-1]
        second_prefix = read_pairs[i].second[:-1]
        prefix_node = Kmer_Node(first_prefix, second_prefix)

        first_suffix = read_pairs[i].first[1:]
        second_suffix = read_pairs[i].second[1:]
        suffix_node = Kmer_Node(first_suffix, second_suffix)

        if prefix_node not in keys:
            entry_node = DB_Node(prefix_node, [suffix_node], 0)
            result.append(entry_node)
            keys.append(prefix_node)
        else:
            # if already seen, update the existing entry
            new_entry = DB_Node(prefix_node, [suffix_node], 0)
            index = result.index(str(new_entry))
            previous_followers = result[index].followers
            current_followers = new_entry.followers
            total_followers = previous_followers + current_followers
            result[index].followers = total_followers

    # add last node needed.
    if type(last)!=int:

        first_suffix = last.first[1:]
        second_suffix = last.second[1:]
        suffix_node = Kmer_Node(first_suffix, second_suffix)

        # Adding entry with followers == []
        if suffix_node not in keys:
            last_entry = DB_Node(suffix_node, [], 0)
            result.append(last_entry)
        else:
            new_entry = DB_Node(prefix_node, [], 0)
            index = result.index(str(new_entry))
            previous_followers = result[index].followers
            current_followers = new_entry.followers
            total_followers = previous_followers + current_followers
            result[index].followers = total_followers

    return result

def main():
    print("running")

if __name__ == "__main__":
    main()
