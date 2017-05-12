""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all ECycles """

from GenomeToReadPairs import make_read_pairs, Kmer_Node
from ReadPairsToDBGraph import make_overlap, make_DB, DB_Node
from DBGraphToBalDBGraph import get_degrees, make_balanced

def dfs_all_cycles(DB, num_edges):
    """ runs DFS to find ALL Eulerean cycles in a balanced/cyclic DB """

    all_cycles = []
    start = DB[0]
    seen_edges = 0
    extra_edges = []
    current_cycle = []
    # cycles contain db_nodes

    stack = []
    stack.append(start)
    # stack contains db_nodes

    while len(stack) != 0:
        current = stack.pop()
        # print(current)

        if len(current_cycle) > 0:
            prev = current_cycle[-1]
            print("want to remove " + str(current) + " from " + str(prev))
            prev.followers.remove(current)

        seen_edges +=1
        # print(seen_edges)

        if current == start and seen_edges == num_edges+1:
            print("found a cycle, need to reset to find more cycles")
            current_cycle.append(current)
            for node in current_cycle:
                print(node)
            all_cycles.append(current_cycle)

            # RESET TO FIND MORE CYCLES
            if len(stack)!=0:

                print("Stack")
                for r in stack:
                    print(r)
                print("ExE")
                for x in extra_edges:
                    print(x)

                most_recent_alternative = extra_edges.pop()
                print("MRA " + str(most_recent_alternative))

                count = 0
                temp = []

                #HARDCODED 2?????

                for i in range (len(current_cycle)-1, 0, -1):
                    temp.append(current_cycle[i])
                    current = current_cycle.pop()
                    if current==most_recent_alternative:
                        count+=1
                    if count==2:
                        break

                current_cycle.append(current)

                print("restarting ")
                for node in current_cycle:
                    print(node)

                for i in range (1, len(temp)):
                    temp[i].followers.append(temp[i-1].kmer_node)

                # print("dictionary")
                # for node in DB:
                #     print("entry "+ str(node))
                #     for x in node.followers:
                #         print(x)

                seen_edges = len(current_cycle)
                # print("seen " + str(seen_edges))

        else:
            if len(current.followers) == 0:
                print("need to backtrack ")

                # RESET TO FIND A VALID CYCLE
                temp = []
                temp.append(current)
                while len(current.followers) == 0:
                    current = current_cycle.pop()
                    temp.append(current)
                    seen_edges -= 1

                current_cycle.append(current)

                for i in range (1, len(temp)):
                    temp[i].followers.append(temp[i-1].kmer_node)

            else:
                # normal case
                current_cycle.append(current)
                current_followers = []

                if len(current.followers)>1:
                    extra_edges.append(current)

                for follower in current.followers:
                    db_follower = kmer_node_to_db_node(follower, DB)
                    stack.append(db_follower)

                print("Stack")
                for r in stack:
                    print(r)

    # print("found " + str(len(all_cycles)) + " cycles")
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
    print("run other file")

if __name__ == "__main__":
    main()
