'''-------------------------------------not the best solution------------------------'''

def MST_Prim(weighted_undirected_graph):
    return (0,[(1,2)])

# class Undirected_Graph():
#
#     def __init__(self, tuples_of_edge_vertices_and_edge_weight):
#         import collections
#         self.dict_to_hold = collections.defaultdict(list)
#         self.set_of_vertices = set()
#         '''Create default dict of lists to store the edges and edge weights'''
#         self.graph_edges = []
#
#         '''Create a default dict that will store the parent and rank of each vertex'''
#
#
#         for veritices_and_weight in range(len(tuples_of_edge_vertices_and_edge_weight)):
#             if tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][0] not in self.set_of_vertices:
#                 self.set_of_vertices.add(tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][0])
#
#             if tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][1] not in self.set_of_vertices:
#                 self.set_of_vertices.add(tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][1])
#             '''Add the tuple to the default dict'''
#             self.graph_edges.append(tuples_of_edge_vertices_and_edge_weight[veritices_and_weight])
#
#
#         for vertex in self.set_of_vertices:
#             self.dict_to_hold[str(vertex)] = (vertex, 0)
#             # self.parent.append(vertex)
#             # self.rank.append(0)
#
#
#
#     def find_root_of(self, vertex):
#
#         if self.dict_to_hold[str(vertex)][0] == vertex:
#             return vertex
#         return self.find_root_of(self.dict_to_hold[str(vertex)][0])
#
#
#
#     def find_rank_of(self, vertex):
#         return self.dict_to_hold[str(vertex)][1]
#
#
#     def rank_union(self, u, root_of_u, v, root_of_v):
#
#         if root_of_u == root_of_v:
#             return root_of_u
#
#         if self.find_rank_of(root_of_u) < self.find_rank_of(root_of_v):
#
#             self.dict_to_hold[str(root_of_u)][0] = str(root_of_v)
#
#         elif self.dict_to_hold[str(root_of_u)][1] > self.dict_to_hold[str(root_of_v)][1]:
#
#             self.dict_to_hold[str(root_of_v)] = str(root_of_u),self.dict_to_hold[str(root_of_v)][1]
#         else:
#             self.dict_to_hold[str(root_of_v)] = root_of_u, self.dict_to_hold[str(root_of_v)][1] #= root_of_u
#             self.dict_to_hold[str(root_of_u)] = self.dict_to_hold[str(root_of_u)][0], self.dict_to_hold[str(root_of_u)][1] + 1


def MST_Kruskel(weighted_undirected_graphh):
    class Undirected_Graph_Mine:

        def __init__(self, tuples_of_edge_vertices_and_edge_wts):
            import collections
            self.dict_to_holdd = collections.defaultdict(list)
            self.set_of_verticess = set()
            '''Create default dict of lists to store the edges and edge weights'''
            self.graph_edgess = []

            '''Create a default dict that will store the parent and rank of each vertex'''

            for veritices_and_weights in range(len(tuples_of_edge_vertices_and_edge_wts)):
                if tuples_of_edge_vertices_and_edge_wts[veritices_and_weights][0] not in self.set_of_verticess:
                    self.set_of_verticess.add(tuples_of_edge_vertices_and_edge_wts[veritices_and_weights][0])

                if tuples_of_edge_vertices_and_edge_wts[veritices_and_weights][1] not in self.set_of_verticess:
                    self.set_of_verticess.add(tuples_of_edge_vertices_and_edge_wts[veritices_and_weights][1])
                '''Add the tuple to the default dict'''
                self.graph_edgess.append(tuples_of_edge_vertices_and_edge_wts[veritices_and_weights])

            for vtx in self.set_of_verticess:
                self.dict_to_holdd[str(vtx)] = (vtx, 0)
                # self.parent.append(vertex)
                # self.rank.append(0)

        def find_root_off(self, vtxx):

            if self.dict_to_holdd[str(vtxx)][0] == vtxx:
                return vtxx
            return self.find_root_off(self.dict_to_holdd[str(vtxx)][0])

        def find_rank_off(self, vertex):
            return self.dict_to_holdd[str(vertex)][1]



        # def rank_unionn(self, u, root_of_u, v, root_of_v):
        #
        #     if root_of_u == root_of_v:
        #         return root_of_u
        #
        #     if self.find_rank_off(root_of_u) > self.find_rank_off(root_of_v):
        #         #print(self.dict_to_holdd[str(root_of_v)]) (0, 0)
        #
        #
        #         self.dict_to_holdd[str(root_of_v)] = root_of_u,self.dict_to_holdd[str(root_of_v)][1]#[parent_and_rank[root_of_v] = (root_of_u, self.parent_and_rank[root_of_v][1])
        #
        #     else:
        #
        #         self.dict_to_holdd[str(root_of_u)] = root_of_v, self.dict_to_holdd[str(root_of_u)][1]
        #
        #         if self.dict_to_holdd[str(root_of_u)][1] == self.dict_to_holdd[str(root_of_v)][1]:
        #             self.dict_to_holdd[str(root_of_v)] =  self.dict_to_holdd[str(root_of_v)][0], self.dict_to_holdd[str(root_of_v)][1] + 1
        #


        def rank_unionn(self, u, root_of_uu, v, root_of_vv):

            if root_of_uu == root_of_vv:
                return root_of_uu

            if self.find_rank_off(root_of_uu) < self.find_rank_off(root_of_vv):

                self.dict_to_holdd[str(root_of_uu)] = root_of_vv, self.dict_to_holdd[str(root_of_uu)][1]
                #self.dict_to_holdd[str(root_of_uu)][0] = root_of_vv


            elif self.dict_to_holdd[str(root_of_uu)][1] > self.dict_to_holdd[str(root_of_vv)][1]:

                self.dict_to_holdd[str(root_of_vv)] = str(root_of_uu), self.dict_to_holdd[str(root_of_vv)][1]
            else:
                self.dict_to_holdd[str(root_of_vv)] = root_of_uu, self.dict_to_holdd[str(root_of_vv)][1]  # = root_of_u
                self.dict_to_holdd[str(root_of_uu)] = self.dict_to_holdd[str(root_of_uu)][0], self.dict_to_holdd[str(root_of_uu)][1] + 1

    '''Create a graph from the input'''
    undirected_graphh = Undirected_Graph_Mine(weighted_undirected_graphh)

    '''Create a placeholder to store the weight of the minimum spanning tree'''
    wt_of_min_spanning_tree = 0

    '''Create a list to store the edges in the minimum spanning tree as you find out the edges to include in the minimum spanning tree'''
    list_of_tuples_containing_the_edges_of_min_spanning_tree = []

    '''Sort the graph on the basis of the weights of the edges, for this, sort the default_dict of the graph object on the basis of the third item
     in each item of the default dict list of the graph'''

    undirected_graphh.graph_edgess = sorted(undirected_graphh.graph_edgess, key = lambda arg_of_lambda : arg_of_lambda[2])
    #need this sorted() method from the python library because my mergeSort() is not built to handle such cases as above
    '''Now, starting from the first edge in the sorted default_dict, check of this edge needs to be added to the spanning tree'''
    edge_counterr = 0

    while edge_counterr <= len(undirected_graphh.set_of_verticess)-1:
        uu,vv,edge_weightt = undirected_graphh.graph_edgess[edge_counterr]

        edge_counterr += 1

        '''Check if this edge is already in the spanning tree or not'''
        root_of_uu = undirected_graphh.find_root_off(uu)
        root_of_vv = undirected_graphh.find_root_off(vv)



        if root_of_uu  != root_of_vv:
            wt_of_min_spanning_tree += edge_weightt

            list_of_tuples_containing_the_edges_of_min_spanning_tree.append((uu,vv))
            undirected_graphh.rank_unionn(uu, root_of_uu, vv, root_of_vv)



    #print(undirected_graph.parent_and_rank)
    # print(type(wt_of_min_spanning_tree))
    # print(type(list_of_tuples_containing_the_edges_of_min_spanning_tree))
    # print(type(list_of_tuples_containing_the_edges_of_min_spanning_tree[0]))


    return wt_of_min_spanning_tree,list_of_tuples_containing_the_edges_of_min_spanning_tree


print (MST_Kruskel([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
# print(MST_Kruskel([(0, 1, 5),(0, 2, 3),(3, 0, 6),(1, 3, 7),(2, 1, 4),(2, 3, 5)]))
# x = MST_Kruskel([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)])
# print(x)
# #(0, 1, 5),(0, 2, 3),(3, 0, 6),(1, 3, 7),(2, 1, 4),(2, 3, 5)
#
# print (MST_Kruskel([(1, 2, 20),(1, 3, 50),(1, 4, 70),(1, 5, 90),(2, 3, 30),(3, 4, 40),(4, 5, 60)]))