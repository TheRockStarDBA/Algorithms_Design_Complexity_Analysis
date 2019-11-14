from collections import defaultdict
import heapq, time

def find_root(parent, vertexx):
    ''''''
    '''Recursively call the parent until the vertex itself is the root of the tree'''
    if parent[vertexx] == vertexx:
        return vertexx
    return find_root(parent, parent[vertexx])

def union_by_rankk(parent_list, rank_list, uu, vv):
    ''''''
    '''find the roots of both the vertices first'''
    root_of_uu = find_root(parent_list, uu)
    root_of_vv = find_root(parent_list, vv)
    '''Do union by rank'''
    if rank_list[root_of_uu] < rank_list[root_of_vv]:
        parent_list[root_of_uu] = root_of_vv
    elif rank_list[root_of_uu] > rank_list[root_of_vv]:
        parent_list[root_of_vv] = root_of_uu
    else:
        parent_list[root_of_vv] = root_of_uu
        rank_list[root_of_uu] += 1
    #print(parent_list)
    #time.sleep(3333)


def finding_verticess_total(undirected_weighted_graph):
    ''''''
    '''Create a dictionary to put all the vertices that exist'''
    default_dictionary = defaultdict(list)
    for uu,vv,weight in undirected_weighted_graph:
        default_dictionary[uu].append((vv,weight))
        default_dictionary[vv].append((uu,weight))
    len_of_dict = len(default_dictionary)
    # print (len_of_dict)
    # time.sleep(5)
    return len_of_dict

def MST_Prim(weighted_undirected_graph):
    ''''''
    '''Create a dictionary'''
    dict_storage = defaultdict(list)

    intialization_values = weighted_undirected_graph[0][0]
    source_values = weighted_undirected_graph[0][0]
    '''Add all values from the graph'''
    for i,j,edge_weight in weighted_undirected_graph:
        dict_storage[i].append((j,edge_weight))
        dict_storage[j].append((i,edge_weight))
    #time.sleep(2222)
    '''Create a list for minimum spanning tree'''
    min_spanning_tree = []
    path_weight_from_vertex = {}
    heap_storage = [(0,intialization_values,source_values)]
    #path_cost = 1
    path_cost = 0
    is_edge_observed = False

    '''Repeat until true'''
    while heap_storage:
        weight, uu, source_values = heapq.heappop(heap_storage)
        if uu in path_weight_from_vertex:
            continue
        else:
            path_weight_from_vertex[uu] = weight
            path_cost += weight
        if is_edge_observed:
            min_spanning_tree.append((source_values,uu))
        is_edge_observed = True
        # print (path_cost)
        # time.sleep(3333)
        for pp, qq in dict_storage[uu]:
            if pp not in path_weight_from_vertex:
                heapq.heappush(heap_storage, (qq,pp,uu))

    return (path_cost,min_spanning_tree)


def MST_Kruskel(undirected_weighted_graph):
    min_spanning_tree = []
    total_sum_of_edges_in_min_span_tree = 0
    idx = 0
    count_of_edges_in_min_span_tree = 0

    '''Sort edges on the basis of the edge weights first'''
    undirected_weighted_graph = sorted(undirected_weighted_graph, key=lambda edgee: edgee[2])
    parent_list = []
    rank_list = []
    number_of_vertices_in_dict = finding_verticess_total(undirected_weighted_graph)

    for node in range(number_of_vertices_in_dict):
        #rank_list.append(0)
        rank_list.append(0)
        parent_list.append(node)

    '''Add the edge in the min spanning tree until we add |V|-1 edges in the tree'''
    while count_of_edges_in_min_span_tree < number_of_vertices_in_dict - 1:
        uu,vv, weightt = undirected_weighted_graph[idx]
        idx = idx + 1
        #time.sleep(3)
        uu = find_root(parent_list, uu)
        vv = find_root(parent_list, vv)
        if uu != vv:
            count_of_edges_in_min_span_tree = count_of_edges_in_min_span_tree + 1
            min_spanning_tree.append((uu, vv))
            total_sum_of_edges_in_min_span_tree =  total_sum_of_edges_in_min_span_tree + weightt
            union_by_rankk(parent_list, rank_list, uu, vv)
    # print(type(min_spanning_tree))
    # print(type(total_sum_of_edges_in_min_span_tree))
    # print(type(min_spanning_tree[0]))
    return (total_sum_of_edges_in_min_span_tree,min_spanning_tree)

# print (MST_Prim([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))