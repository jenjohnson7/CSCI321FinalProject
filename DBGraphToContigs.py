""" Jen Johnson
CSCI 321 Spring 17 Final Project
Paired DeBruijn Graph to reconstruct Salmonella Genome """

def kmer_node_to_db_node(kmer_node, DB):
    """ returns db_node with db_node.kmer_node == kmer_node """
    for node in DB:
        if node.kmer_node == kmer_node:
            return node

def make_contigs(db_graph):
    """ finds the collection of contigs in a DG graph from the form of db_nodes
    with current node kmer_node, followers as a list of kmer_nodes, and num_incoming """

    paths = []

    for node in db_graph:
        #if NOT a 1-in-1-out node...
        if len(node.followers)!=1 or node.num_incoming!=1:
            # and it has a follower...
            if len(node.followers)>0:
                # go through these followers...
                for kmer_follower in node.followers:
                    # start a contig
                    db_follower = kmer_node_to_db_node(kmer_follower, db_graph)
                    current_path = [node, db_follower]
                    # extend the contig if followers are 1-in-1-out
                    current_node = db_follower
                    while len(current_node.followers)==1 and node.num_incoming==1:
                        #update the current node
                        #always be the first and only follower of current_node
                        #[0] because you need an int, not a list
                        current_node = kmer_node_to_db_node(current_node.followers[0], DB)
                        current_path.append(current_node)
                    paths.append(current_path)

    return paths
def main():
    print("running")

if __name__ == "__main__":
    main()
