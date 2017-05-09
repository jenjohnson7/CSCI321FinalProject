""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all ECycles """

from GenomeToReads import make_read_pairs, Kmer_Node
from ReadsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced

def dfs_all_cycles(DB, num_edges):
    """ runs DFS to find ALL Eulerean cycles in a balanced/cyclic DB """

    all_cycles = []

    start = DB[0]
    print("start node " + str(start))
    print("num_edges " + str(num_edges))

    seen_edges = 0

    current_cycle = []
    # cycles contain db_nodes

    stack = []
    stack.append(start)
    # stack contains db_nodes

    while len(stack) != 0:

        current = stack.pop()

        if len(current_cycle) >0:
            prev = current_cycle[-1]
            print("want to remove " + str(current) + " from " + str(prev))
            prev.followers.remove(current)
            print("just removed " + str(current) + " from " + str(prev))

        print("just added " +str(current))

        seen_edges +=1

        print(str(seen_edges) + " edges")

        if current == start and seen_edges == num_edges+1:
            print("found a cycle")
            current_cycle.append(current)
            if current_cycle not in all_cycles:
                all_cycles.append(current_cycle)

            # RESET TO PREVIOUS TO FIND MORE CYCLES
            new_start = stack.pop()
            while new_start != current:
                current = current_cycle.pop()
                prev = current_cycle[-1]
                prev.followers.append(current)
                seen_edges -=1

        else:
            if len(current.followers) == 0:
                print(stack[0])
                print("Current_cycle")
                for node in current_cycle:
                    print(node)

                # RESET TO FIND A VALID CYCLE: HOW TO RE-ADD AFTER?????
                print("need to backtrack")
                while len(current.followers) == 0:
                    current = current_cycle.pop()
                    prev = current_cycle[-1]
                    prev.followers.append(current)
                    seen_edges -= 1

                print(num_edges)
                print(current)

            else:
                current_cycle.append(current)
                current_followers = []
                print(str(len(current.followers)) + " followers to append")

                for follower in current.followers:
                    db_follower = kmer_node_to_db_node(follower, DB)
                    stack.append(db_follower)
                    print("follower " + str(follower) + " of " + str(current) + " appended")

    print("found " + str(len(all_cycles)) + " cycles")
    return all_cycles

def kmer_node_to_db_node(kmer_node, DB):
    """ searches through DB to find db_node == kmer_node
    returns db_node """

    for db_node in DB:
        if db_node.kmer_node == kmer_node:
            return db_node

def get_num_edges(DB):
    """ returns the number of edges in the graph """
    num_edges = 0
    for i in range (0, len(DB)):
        num_edges += len(DB[i].followers)

    return num_edges

def main():
    print("run the other file!!!")

if __name__ == "__main__":
    main()
