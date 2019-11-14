'''----------------------------------not the best solution----------------------'''
import time

def MST_Prim(weighted_undirected_graph):
    print("")

class Undirected_Graph():
    def __init__(self, tuples_of_edge_vertices_and_edge_weight):
        self.set_of_vertices = set()
        '''Create default dict of lists to store the edges and edge weights'''
        self.graph_edges = []

        '''Create a default dict that will store the parent and rank of each vertex'''
        #self.parent_and_rank = defaultdict(list)
        self.parent_and_rank = []

        for veritices_and_weight in range(len(tuples_of_edge_vertices_and_edge_weight)):
            if tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][0] not in self.set_of_vertices:
                self.set_of_vertices.add(tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][0])

            if tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][1] not in self.set_of_vertices:
                self.set_of_vertices.add(tuples_of_edge_vertices_and_edge_weight[veritices_and_weight][1])
            '''Add the tuple to the default dict'''
            self.graph_edges.append(tuples_of_edge_vertices_and_edge_weight[veritices_and_weight])


        for vertex in range(len(self.set_of_vertices)):
            self.parent_and_rank.append((vertex, 0))




    def find_root_of(self, vertex):

        # while vertex != self.parent_and_rank[vertex][0]:
        #     vertex = self.parent_and_rank[vertex][0]
        # return vertex

        if self.parent_and_rank[vertex][0] == vertex:
            #print("same paremt")
            return vertex
        else:
            #print("different parent")
            return self.find_root_of(self.parent_and_rank[vertex][0])

    def find_rank_of(self, vertex):
        return self.parent_and_rank[vertex][1]

    def rank_union(self, u, root_of_u, v, root_of_v):

        if root_of_u == root_of_v:
            return root_of_u

        if self.find_rank_of(root_of_u) > self.find_rank_of(root_of_v):

            self.parent_and_rank[root_of_v] = (root_of_u, self.parent_and_rank[root_of_v][1])
        else:

            self.parent_and_rank[root_of_u] = (root_of_v,self.parent_and_rank[root_of_u][1])


            if self.parent_and_rank[root_of_u][1] == self.parent_and_rank[root_of_v][1]:
                self.parent_and_rank[root_of_v] = (self.parent_and_rank[root_of_v][0], self.parent_and_rank[root_of_v][1] + 1)



def MST_Kruskel(weighted_undirected_graph):


    '''Create a graph from the input'''
    undirected_graph = Undirected_Graph(weighted_undirected_graph)

    '''Create a placeholder to store the weight of the minimum spanning tree'''
    weight_of_minimum_spanning_tree = 0

    '''Create a list to store the edges in the minimum spanning tree as you find out the edges to include in the minimum spanning tree'''
    list_of_tuples_containing_the_edges_of_min_spanning_tree = []

    '''Sort the graph on the basis of the weights of the edges, for this, sort the default_dict of the graph object on the basis of the third item
     in each item of the default dict list of the graph'''
    undirected_graph.graph_edges = sorted(undirected_graph.graph_edges, key = lambda argument_of_lambda : argument_of_lambda[2])
    #need this sorted() method from the python library because my mergeSort() is not built to handle such cases as above
    '''Now, starting from the first edge in the sorted default_dict, check of this edge needs to be added to the spanning tree'''
    edge_counter = 0

    while edge_counter <= len(undirected_graph.set_of_vertices)-1:
        u,v,edge_weight = undirected_graph.graph_edges[edge_counter]

        edge_counter += 1

        '''Check if this edge is already in the spanning tree or not'''
        root_of_u = undirected_graph.find_root_of(u)
        root_of_v = undirected_graph.find_root_of(v)


        if root_of_u  != root_of_v:
            weight_of_minimum_spanning_tree += edge_weight
            list_of_tuples_containing_the_edges_of_min_spanning_tree.append((u,v))
            undirected_graph.rank_union(u, root_of_u, v, root_of_v)

    #print(undirected_graph.parent_and_rank)
    return (weight_of_minimum_spanning_tree,list_of_tuples_containing_the_edges_of_min_spanning_tree)




x = MST_Kruskel(([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
print(x)

