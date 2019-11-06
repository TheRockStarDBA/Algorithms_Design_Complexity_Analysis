

def reverse(string):
    string = "".join(reversed(string))
    return string
'''----------------------------------------------------------------------------------------------------------'''
'''Helper functions to make deepcopy() faster'''
_dispatcher = {}

def _copy_list(l, dispatch):
    ret = l.copy()
    for idx, item in enumerate(ret):
        cp = dispatch.get(type(item))
        if cp is not None:
            ret[idx] = cp(item, dispatch)
    return ret

def _copy_dict(d, dispatch):
    ret = d.copy()
    for key, value in ret.items():
        cp = dispatch.get(type(value))
        if cp is not None:
            ret[key] = cp(value, dispatch)

    return ret

_dispatcher[list] = _copy_list
_dispatcher[dict] = _copy_dict


def deepcopy(sth):
    cp = _dispatcher.get(type(sth))
    if cp is None:
        return sth
    else:
        return cp(sth, _dispatcher)
'''-------------------------------------------------------------------------------------------------------------'''
def get_neighbor_of_state(state_to_check_config, state_space_configs_dictionary, maxsize, deepcopy):

    '''Returns a list of neighbor nodes from this parent state'''
    neighbors_list = []

    '''Find the index of 0 within each neighbor's state configuration.'''

    items_as_dict = dict(zip(state_to_check_config, range(0, len(state_to_check_config))))
    idx_of_0 = items_as_dict[0]

    #idx_of_0 = state_to_check_config.index(0)

    '''Check if 0 can be moved left'''
    if idx_of_0 != 0:
        if idx_of_0 != 3:
            if idx_of_0 != 6:
                '''Copy to another variable. '''
                new_state_var_config = deepcopy(state_to_check_config)
                new_state_var_config[idx_of_0], new_state_var_config[idx_of_0 - 1] = new_state_var_config[idx_of_0 - 1], new_state_var_config[idx_of_0]

                '''Add this neighbor to the state space dictionary if does not already exist'''
                str_of_new_state_var_config = str(new_state_var_config)
                if str_of_new_state_var_config not in state_space_configs_dictionary:
                    state_space_configs_dictionary[str_of_new_state_var_config] = ("L", maxsize)
                    neighbors_list.append(new_state_var_config)


    '''Check if 0 can be moved right'''
    if idx_of_0 != 2:
            if idx_of_0 != 5:
                if idx_of_0 != 8:

                    new_state_var_config = deepcopy(state_to_check_config)
                    new_state_var_config[idx_of_0], new_state_var_config[idx_of_0 + 1] = new_state_var_config[idx_of_0 + 1], new_state_var_config[idx_of_0]
                    str_of_new_state_var_config = str(new_state_var_config)
                    '''Add this neighbor to the state space dictionary if does not already exist'''
                    if str_of_new_state_var_config not in state_space_configs_dictionary:
                        state_space_configs_dictionary[str_of_new_state_var_config] = ("R", maxsize)
                        neighbors_list.append(new_state_var_config)


    '''Check if 0 can be moved up'''
    if idx_of_0 != 0:
        if idx_of_0!= 1:
            if idx_of_0 != 2:
                new_state_var_config = deepcopy(state_to_check_config)
                new_state_var_config[idx_of_0], new_state_var_config[idx_of_0 - 3] = new_state_var_config[idx_of_0 - 3], new_state_var_config[idx_of_0]
                str_of_new_state_var_config = str(new_state_var_config)
                '''Add this neighbor to the state space dictionary if does not already exist'''
                if str_of_new_state_var_config not in state_space_configs_dictionary:
                    state_space_configs_dictionary[str_of_new_state_var_config] = ("U", maxsize)
                    neighbors_list.append(new_state_var_config)


    '''Check if 0 can be moved down'''
    if idx_of_0 != 6:
        if idx_of_0 != 7:
            if idx_of_0 != 8:
                new_state_var_config = deepcopy(state_to_check_config)
                new_state_var_config[idx_of_0], new_state_var_config[idx_of_0 + 3] = new_state_var_config[idx_of_0 + 3], new_state_var_config[idx_of_0]
                str_of_new_state_var_config = str(new_state_var_config)
                '''Add this neighbor to the state space dictionary if does not already exist'''
                if str_of_new_state_var_config not in state_space_configs_dictionary:
                    state_space_configs_dictionary[str_of_new_state_var_config] = ("D", maxsize)
                    neighbors_list.append(new_state_var_config)

    return neighbors_list


def get_shortest_path_for_this_state(goal_state_config, initial_state_config, state_space_dict, maxsize, deepcopy):
    '''should return the shortest path from goal state to this initial state'''

    '''Add goal state to the state space dictionary'''
    state_space_dict[str(goal_state_config)]= ("", 0)


    '''Initialize the queue. Each element will be the index of the state in state space list'''
    FIFS_queue_to_traverse_in_BFS = []

    '''First element in the queue from which we will start traversing is the goal state itself.'''
    FIFS_queue_to_traverse_in_BFS.append(goal_state_config)

    while len(FIFS_queue_to_traverse_in_BFS) != 0:
        state_to_check_config = FIFS_queue_to_traverse_in_BFS[0]

        '''Pop the first element from the queue'''
        FIFS_queue_to_traverse_in_BFS.pop(0)

        '''You should get the neighbors of this popped state now'''
        neighbors = get_neighbor_of_state(state_to_check_config, state_space_dict, maxsize, deepcopy)

        '''Finish appending all 4 neighbors before this for loop completely ends'''
        for neighbor_config in (neighbors):
            str_of_neighbor_config = str(neighbor_config)

            '''Find the distance to goal from this neighbor to compare with maxsize'''

            state_space_dict[str_of_neighbor_config] =("{}{}".format (state_space_dict[str(state_to_check_config)][0] , state_space_dict[str_of_neighbor_config][0]), state_space_dict[str_of_neighbor_config][1])

            '''Check if the node has already been traversed.'''
            if state_space_dict[str_of_neighbor_config][1] == maxsize:
                FIFS_queue_to_traverse_in_BFS.append(neighbor_config)
                state_space_dict[str_of_neighbor_config] = state_space_dict[str_of_neighbor_config][0], state_space_dict[str_of_neighbor_config][1] + 1

                '''Check if it is the initial state'''
                if neighbor_config == initial_state_config:
                    '''break out of two loops using return'''
                    return state_space_dict[str_of_neighbor_config][0]



def ShortestPath(goal_state_config, list_of_initial_states_config):
    from sys import maxsize

    '''Create state space such that each item in the state space is  a dictionary object'''
    state_space = {}

    '''call a function to solve for each of the initial states'''
    list_of_solutions_for_all_initial_states = [str(reverse(get_shortest_path_for_this_state(goal_state_config, initial_state_config, deepcopy(state_space), maxsize, deepcopy))) for initial_state_config in list_of_initial_states_config]

    return list_of_solutions_for_all_initial_states


current_goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
initial_states = [[2, 4, 7, 1, 5, 3, 0, 8, 6], [0, 1, 6, 8, 4, 2, 5, 7, 3]]
paths = ShortestPath(current_goal_state, initial_states ) #[1, 2, 3, 4, 8, 5, 6, 7, 0]]) DRRULLDR
print("The solutions are: ", paths)
