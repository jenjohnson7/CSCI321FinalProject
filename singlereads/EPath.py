#Jen Johnson
#CSCI321
#Problem 16 EPath

import sys
import numpy as np
from ECycle import E_cycle

def make_degree_dict(adj_dict, degree_dict):
    """ uses the adj_dict to calculate degree of each node """
    #getting the outdegrees
    for entry in adj_dict:
        degree_dict[entry]=len(adj_dict[entry])

    #getting the indegrees
    for entry in adj_dict:
        for neighbor in adj_dict[entry]:
            if neighbor in degree_dict:
                current = degree_dict[neighbor]
                current +=1
                degree_dict[neighbor] = current
            else:
                degree_dict[neighbor]=1

    return degree_dict

def E_Path(degree_dict, adj_dict, num_edges, num_lines):
    """ makes the graph balanced, calls E-Cycle, removes imaginary edge"""
    #get the unbalanced nodes that have odd degree
    unbalanced = []
    for entry in degree_dict:
        if degree_dict[entry]% 2 ==1:
            unbalanced.append(entry)

    outdegree = []
    #getting the outdegrees of unbalanced nodes
    for i in range (0, len(unbalanced)):
        node = unbalanced[i]
        if node in adj_dict:
            outdegree.append(len(adj_dict[node]))
        else:
            outdegree.append(0)

    indegree = []
    #getting the indegrees of unbalanced nodes
    for i in range (0, len(unbalanced)):
        indegree.append(degree_dict[unbalanced[i]]-outdegree[i])

    #add the missing edge to adj_dict based on out and indegrees
    for i in range (0, len(unbalanced)):
        if outdegree[i] < indegree[i]:
            source = unbalanced[i]
        else:
            sink = unbalanced[i]

    if source in adj_dict:
        temp = adj_dict[source]
        temp.append(sink)
        adj_dict[source] = temp
    else:
        adj_dict[source] = [sink]

    # call E_cycle on the new adj_dict with added edge
    cycle = E_cycle(adj_dict, num_edges+1, num_lines)

    start_index = 0

    # find the imaginary edge
    if outdegree[0] < outdegree[1]:
        for i in range (0, len(cycle)):
            if cycle[i] == unbalanced[0] and cycle[i+1] == unbalanced[1]:
                start_index = i
    if outdegree[1] < outdegree[0]:
        for i in range (0, len(cycle)):
            if cycle[i] == unbalanced[1] and cycle[i+1] == unbalanced[0]:
                start_index = i

    final_path = []
    #get the path from the cycle by splicing the imaginary edge
    final_path += cycle[start_index+1:]
    final_path += cycle[1:start_index+1]

    return final_path

def main():
    print("Running")

if __name__=="__main__":
    main()
