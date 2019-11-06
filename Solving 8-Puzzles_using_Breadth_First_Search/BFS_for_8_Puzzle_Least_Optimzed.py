import sys, time, copy

list_of_solutions_for_all_initial_states = []


class Node_in_BFS_Tree():

    def __init__(self, state_configuration):
        self.parent = None
        self.state_value = state_configuration
        self.distance_to_goal_state = sys.maxsize
        self.path_from_goal_state = ""

    def get_parent(self):
        return self.parent

    def set_paret(self, parent):
        self.parent = parent

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def get_neighbor_of_state_at_idx(idx_in_state_idx, state_space):
    '''Returns a list of neighbor nodes from this parent state'''
    adjacency_list = []

    '''Find the index of 0 within each neighbor's state configuration.'''
    idx_of_0 = state_space[idx_in_state_idx].state_value.index(0)


    '''Check if 0 can be moved left'''
    if idx_of_0 != 0 and idx_of_0 != 3 and idx_of_0 != 6:
        '''Copy to another varibale so that the same '''
        new_state_var = copy.deepcopy(state_space[idx_in_state_idx].state_value)
        new_state_var[idx_of_0], new_state_var[idx_of_0 - 1] = new_state_var[idx_of_0 - 1], new_state_var[idx_of_0]
        adjacency_list.append([Node_in_BFS_Tree(new_state_var), "L"])

    '''Check if 0 can be moved right'''
    if idx_of_0 != 2 and idx_of_0 != 5 and idx_of_0 != 8:

        new_state_var = copy.deepcopy(state_space[idx_in_state_idx].state_value)
        new_state_var[idx_of_0], new_state_var[idx_of_0 + 1] = new_state_var[idx_of_0 + 1], new_state_var[idx_of_0]
        adjacency_list.append([Node_in_BFS_Tree(new_state_var), "R"])

    '''Check if 0 can be moved up'''
    if idx_of_0 != 0 and idx_of_0!= 1 and idx_of_0 != 2:
        new_state_var = copy.deepcopy(state_space[idx_in_state_idx].state_value)
        new_state_var[idx_of_0], new_state_var[idx_of_0 - 3] = new_state_var[idx_of_0 - 3], new_state_var[idx_of_0]
        adjacency_list.append([Node_in_BFS_Tree(new_state_var), "U"])

    '''Check if 0 can be moved down'''
    if idx_of_0 != 6 and idx_of_0 != 7 and idx_of_0 != 8:
        new_state_var = copy.deepcopy(state_space[idx_in_state_idx].state_value)
        new_state_var[idx_of_0], new_state_var[idx_of_0 + 3] = new_state_var[idx_of_0 + 3], new_state_var[idx_of_0]
        adjacency_list.append([Node_in_BFS_Tree(new_state_var), "D"])

    return adjacency_list


def get_shortest_path_for_this_state(goal_state, initial_state , state_space_nodes):
    '''should return the shortest path from goal state to this initial state'''

    '''Set distance from goal to goal == 0.'''
    index_of_goal_state_in_state_space = None
    counter = 0
    for node in state_space_nodes:

        if node.state_value == goal_state.state_value:
            index_of_goal_state_in_state_space = counter
            #index_of_goal_state_in_state_space = state_space_nodes.index()
            break
        counter += 1

    state_space_nodes[index_of_goal_state_in_state_space].distance_to_goal_state = 0

    '''Initialize the queue. Each element will be the index of the state in state space list'''
    FIFS_queue_to_traverse_in_BFS = []

    '''First element in the queue from which we will start traversing is the goal state itself.'''
    FIFS_queue_to_traverse_in_BFS.append(index_of_goal_state_in_state_space)

    while len(FIFS_queue_to_traverse_in_BFS) != 0:
        idx_of_state_to_check = FIFS_queue_to_traverse_in_BFS[0]

        '''Pop the first element from the queue'''
        FIFS_queue_to_traverse_in_BFS.pop(0)

        '''You should get the neighbors of this popped state now'''
        neighbors_returned = get_neighbor_of_state_at_idx(idx_of_state_to_check, state_space_nodes)


        neighbor_counter = 0

        '''Finish appending all 4 neighbors before this for loop completely ends'''
        for i in range(len(neighbors_returned)):

            '''Find the distance to goal from this neighbor to compare with maxsize'''
            this_neighbor_idx = None
            counter = 0

            '''Find the index of this neighbor'''
            for node_ in state_space_nodes:

                if node_.state_value == neighbors_returned[i][0].state_value:
                    this_neighbor_idx = counter
                    break
                counter += 1



            state_space_nodes[this_neighbor_idx].parent = idx_of_state_to_check
            state_space_nodes[this_neighbor_idx].path_from_goal_state = state_space_nodes[idx_of_state_to_check].path_from_goal_state + neighbors_returned[i][1]

            '''Check if the node has already been traversed.'''
            if state_space_nodes[this_neighbor_idx].distance_to_goal_state == sys.maxsize:
                FIFS_queue_to_traverse_in_BFS.append(this_neighbor_idx)
                state_space_nodes[this_neighbor_idx].distance_to_goal_state = state_space_nodes[idx_of_state_to_check].distance_to_goal_state + 1

                '''Check if it is the initial state'''
                if state_space_nodes[this_neighbor_idx].state_value == initial_state.state_value:

                    return state_space_nodes[this_neighbor_idx].path_from_goal_state

        # print("All 4 neighbors should be in this queue.", FIFS_queue_to_traverse_in_BFS)
        # print(state_space_nodes[FIFS_queue_to_traverse_in_BFS[0]].state_value,state_space_nodes[FIFS_queue_to_traverse_in_BFS[1]].state_value,
        #        state_space_nodes[FIFS_queue_to_traverse_in_BFS[2]].state_value,state_space_nodes[FIFS_queue_to_traverse_in_BFS[3]].state_value)
        #

def ShortestPath(goal_state, list_of_initial_states):

    '''Create state space such that each item in the state space list is  a node object'''
    from itertools import permutations
    input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    l = list(permutations(input))
    state_space = []
    for i in l:
        state_space.append(Node_in_BFS_Tree(list(i))) #362880 total states

    '''Convert goal state to a Node object'''
    goal_state = Node_in_BFS_Tree(goal_state)

    '''Convert initial states to solve to Node objects'''
    list_of_initial_states = [ Node_in_BFS_Tree(initial_state) for initial_state in list_of_initial_states]


    '''call a function to solve for each of the initial states'''
    for initial_state in list_of_initial_states:
        ss = copy.deepcopy(state_space)
        shortest_path_for_this_state = get_shortest_path_for_this_state(goal_state, initial_state, ss)
        '''Reverse the path'''
        list_of_solutions_for_all_initial_states.append(shortest_path_for_this_state)

    return list_of_solutions_for_all_initial_states


current_goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
paths = ShortestPath(current_goal_state, [[1,2,3,4,5,6,8,7,0],[1,2,3,4,5,6,8,7,0]]) #[1, 2, 3, 4, 8, 5, 6, 7, 0]]) DRRULLDR
print("The solutions are: ", paths)
