from collections import defaultdict
#import time
def breadth_first_Search(source_node, sink_node, edges):
    queue = []
    queue.append(source_node)
    set_of_visited_nodes = set()
    set_of_visited_nodes.add(source_node)
    #from collections import defaultdict
    #time.sleep(4545
    dict_to_store_p = defaultdict()
    '''Until queue has values'''
    while queue:
        uu = queue.pop(0)
        if uu == sink_node:
            return dict_to_store_p

        for vv, ww in edges[uu].items():
            if vv not in set_of_visited_nodes and ww:
                queue.append(vv)
                set_of_visited_nodes.add(vv)
                dict_to_store_p[vv] = (uu,ww)
    #print("should not print this")
    #time.sleep(2222)
    return None

def aug_path_update(source_node, sink_node, edges, parent, minimum_flow_till_now):
    # print("Inside Augmented path")
    # time.sleep(3333)
    vv = sink_node
    while vv != source_node:#check first
        uu, ww = parent[vv]
        edges[uu][vv] = edges[uu][vv] - minimum_flow_till_now
        edges[vv][uu] = edges[vv][uu] + minimum_flow_till_now
        vv = uu
        #print(vv)
        #time.sleep(22221)

def maximum_flow_graphh(edges, residual_edges):
    residual_vals = []
    for uu,next in edges.items():
        for vv,capacity in next.items():
            check = capacity - residual_edges[uu][vv]
            if check > 0:
                #print("check greater")
                #time.sleep(1111)
                residual_vals.append((uu,vv,check))
    return  residual_vals

def Max_Flow_Dinitz_Algorithm(source_node, sink_node, graph):
    edges = defaultdict(lambda : defaultdict(lambda : 0))
    for uu, vv, ww in graph:
        edges[uu][vv] = max(edges[uu][vv],ww)
        edges[vv][uu] = max(edges[vv][uu], 0)
    import copy
    copy_of_original_edges = copy.deepcopy(edges)
    maximum_flow = 0

    while True:
        parent = breadth_first_Search(source_node,sink_node,edges)
        if parent == None:
            ress = maximum_flow_graphh(copy_of_original_edges, edges)
            return maximum_flow, ress

        min_flow = 1<<30
        vv = sink_node
        while vv != source_node:
            uu, ww = parent[vv]
            min_flow = min(min_flow, ww)
            vv = uu
        #print(maximum_flow," ","Before")
        maximum_flow = maximum_flow + min_flow
        #print("After ", maximum_flow)
        #time.sleep(56645)
        aug_path_update(source_node, sink_node, edges, parent, min_flow)

    return None





'''----------------------------------------------------------------------------------------------------------'''

def dijkstra_with_fat(source_node, sink_node, edges, heapdict):

    '''Create two dictionaries'''
    default_dictionary = defaultdict()
    heap_dictionary = heapdict()
    '''Give def values'''
    heap_dictionary[source_node] = -1<<30
    default_dictionary[source_node] = 1<<30
    set_of_visited_nodes = set()
    parentt = defaultdict()

    '''Run until queue empty'''
    while heap_dictionary != []:
        try:
            uu, ww = heap_dictionary.popitem()
        except:
            return None, 0

        set_of_visited_nodes.add(uu)

        if uu == sink_node:
            return parentt, default_dictionary[uu]

        for vv, weightt in edges[uu].items():
            if vv not in set_of_visited_nodes and weightt:
                default_dictionary[vv] = min(default_dictionary[uu], weightt)
                heap_dictionary[vv] = - default_dictionary[vv]
                parentt[vv] = (uu, weightt)



def Max_Flow_Edmund_Karp_Algorithm(source_node, sink_node, graph):
    #from collections import defaultdict
    '''Set exp to 0 at first'''
    edgess = defaultdict(lambda : defaultdict( lambda : 0))

    '''Choose the max value'''
    for uu, vv, ww in graph:
        edgess[uu][vv] = max(edgess[uu][vv],ww)
        edgess [vv][uu] = max(edgess[vv][uu], 0)
    import copy
    copy_of_original_edges = copy.deepcopy(edgess)
    maximum_flow = 0

    # while True:
    #     parent, minimum_flow = dijkstra_with_fat(source_node, sink_node, edgess)
    #
    #     if parent == None:
    #         ress = maximum_flow_graphh(copy_of_original_edges, edgess)
    #         return maximum_flow, ress
    #     maximum_flow = maximum_flow + minimum_flow
    #     aug_path_update(source_node, sink_node, edgess, parent, minimum_flow)
    import time

    while True:
        from heapdict import heapdict
        parent, minimum_flow = dijkstra_with_fat(source_node, sink_node, edgess, heapdict)
        #print(parent)
        #time.sleep(3333)

        if parent == None:
            ress = maximum_flow_graphh(copy_of_original_edges, edgess)
            return maximum_flow, ress
        #print maximum_flow
        # time.sleep(3333)
        maximum_flow = maximum_flow + minimum_flow
        #print maximum_flow
        # time.sleep(3333)
        aug_path_update(source_node, sink_node, edgess, parent, minimum_flow)

print Max_Flow_Short(0, 3, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
print Max_Flow_Short(0, 4,  [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)])
