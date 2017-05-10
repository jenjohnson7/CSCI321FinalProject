#Jen Johnson
#CSCI321
#Problem 15 Ecycle

import sys
import numpy as np
from multiprocessing import Queue

def E_cycle(adj_dict, num_edges, num_lines):
    """ finds an Eulerean cycle, given that the graph input is balanced and well connected"""

    #current_node = 0 #arbitrarily choose node 0 to start

    #set current_node as key in adj_dict when using strings instead of node numbers
    current_list = next (iter (adj_dict.values()))
    current_node = current_list[0]

    path = []
    seen_edges = 0
    seen_and_extra_edges = [] #for backtracking

    while seen_edges != num_edges:
        if len(adj_dict[current_node]) != 0:
            #if there is another outgoing edge
            path.append(current_node)
            next_node = adj_dict[current_node][0] #get the next unseen edge
            adj_dict[current_node].remove(next_node)
            #remove edge so that it won't be visited twice
            if len(adj_dict[current_node]) !=0:
                #if there is another outgoing edge, add it to backtracking list
                seen_and_extra_edges.append(current_node)
            seen_edges +=1
            current_node = next_node
        else:
            #made a bad choice, need to start a new sub-cycle
            #print(seen_and_extra_edges)
            #print(path)
            current_node = seen_and_extra_edges[0]
            seen_and_extra_edges.remove(current_node)

            #put the previous sub-cycle into the path
            temp_path = []
            new_start = path.index(current_node)
            temp_path = path[new_start:] #from the restart node to the end
            temp_path += path[:new_start] #from the beginning to the restart node
            path = temp_path

    #append the last elt
    source = path[0]
    path+=[source]
    return path

def main():
    print("running")

if __name__=="__main__":
    main()
