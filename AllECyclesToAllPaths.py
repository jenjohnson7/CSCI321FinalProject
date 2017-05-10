""" Jen Johnson
CSCI 321 Spring 17 Final Project
Returns all EPaths """

def cycle_to_path(all_cycles, outdegree, indegree, unbalanced):
    """ given a set of euler cycles
    and dictionaries how the balanced graph was made
    returns the a set of euler paths """

    all_paths = []
    for cycle in all_cycles:
        start_index = 0
        if outdegree[0] < outdegree[1]:
            for i in range (0, len(cycle)):
                if cycle[i] == unbalanced[0] and cycle[i+1] == unbalanced[1]:
                    start_index = i
        if outdegree[1] < outdegree[0]:
            for i in range (0, len(cycle)):
                if cycle[i] == unbalanced[1] and cycle[i+1] == unbalanced[0]:
                    start_index = i

        current_path = []
        #get the path from the cycle by splicing the imaginary edge
        current_path += cycle[start_index+1:]
        current_path += cycle[1:start_index+1]
        all_paths.append(current_path)

    return all_paths

def main():
    print("run the other file!!!")

if __name__ == "__main__":
    main()
